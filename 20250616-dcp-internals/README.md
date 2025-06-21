# PyTorch Distributed Checkpoint Internals

Distributed checkpointing is a feature introduced to PyTorch that enables developers to implement parallel checkpointing in a way that’s agnostic to the cluster topology. While the implementation appears modular and flexible, the official documentation and tutorials only cover the high-level APIs, and internal details are largely undocumented. This post provides a rough guide to the internals of PyTorch’s distributed checkpointing system — aimed at both those who want to tweak its behavior, and my future self who will probably forget the details I currently remember.

Broadly speaking, the implementation revolves around two core components: `Planner` (in `planner.py`) and `Storage` (in `storage.py`). Each process in a distributed group has its own planner and storage instance, and they coordinate to save or load checkpoints. The planner decides what each process is responsible for saving or loading, by communicating across the entire process group. The storage handles the actual writing and reading of tensors or bytes to and from disk or memory. These components interact through structured data types (defined as dataclasses), such as `SavePlan`, `LoadPlan`, `WriteItem`, `ReadItem`, `Metadata`, and others.

We'll first look at how saving works, followed by the loading process.

---

## Saving

To save a model using distributed checkpointing, each process must instantiate a subclass of both `StorageWriter` (from `storage.py`) and `SavePlanner` (from `planner.py`) before saving begins. Typically, `FileSystemWriter` (from `filesystem.py`) and `DefaultSavePlanner` (from `default_planner.py`) are chosen automatically if not explicitly specified by the user. For the rest of this explanation, we'll assume the default choices are used.

When the user calls the `save` function (in `state_dict_saver.py`), the planner and storage writer on each process coordinate to perform the save. Usually, the user only passes the model's `state_dict` and a `checkpoint_id` to this function. The general flow is illustrated in the diagram below:

<img src="/20250616-dcp-internals/figure1.png" width="50%" />

Initially, each process sets itself up via the `set_up_planner` method of `Planner` and the `set_up_storage_writer` method of `StorageWriter`. These setup methods do very little. For instance, `DefaultSavePlanner` sets up metadata for the `state_dict`, while `FileSystemWriter` does essentially nothing at this stage.

Next, each process generates a `local_plan` of type `SavePlan` — essentially a proposal describing which parts of the model it will be responsible for saving. This is created using the `create_local_plan` method. A `SavePlan` is essentially a list of `WriteItem`s, each of which defines a segment of the model (by path, offset, and size) that the process will write.

The coordinator process (typically rank 1, as shown in the diagram) then gathers all the `local_plan`s, refines them, and creates global metadata. For example, `DefaultSavePlanner.create_global_plan` deduplicates `WriteItem`s and generates a `Metadata` (from `metadata.py`) that will later be used during loading. Meanwhile, `FileSystemWriter.prepare_global_plan` assigns unique file prefixes (e.g. `__{i}_` for rank `i`) to ensure there are no conflicts.

Once the plans are finalized, the coordinator redistributes them to each process. At this point, each process may further adjust its plan using the `finish_plan` method (though usually this step is a no-op). The `StorageWriter` then begins writing tensors and bytes to disk according to its assigned `SavePlan`. If `FileSystemWriter` is used, this step is multi-threaded. After writing completes, the coordinator collects the results and writes a final `.metadata` file to mark the end of the checkpoint.

---

## Loading

Loading also requires one instance each of `LoadPlanner` and `StorageReader`, typically `DefaultLoadPlanner` and `FileSystemReader` if unspecified.

When the user invokes the `load` function (in `state_dict_loader.py`), the planner and reader work together to load the model’s parameters back into memory, as shown below:

<img src="/20250616-dcp-internals/figure2.png" width="50%" />

The process begins by reading the metadata file via `read_metadata`. This file contains information about the stored tensors and bytes, including their structure, types, and how they were split across processes when saving. Since distributed checkpointing can save a single tensor in chunks across multiple processes, this metadata is essential for proper reconstruction.

After a minimal setup via `set_up_planner` and `set_up_storage_reader`, each process calls `create_local_plan` to propose how it will load its assigned data. This plan, of type `LoadPlan`, is essentially a list of `ReadItem`s, each of which describes which part of the checkpoint should be loaded into which part of the model’s `state_dict`.

Although `create_global_plan` and `prepare_global_plan` exist to modify plans with global awareness, the default implementations (`DefaultLoadPlanner` and `FileSystemReader`) do nothing in these methods. Instead, they simply aggregate the `local_plans`, approve them, and send them back to each process.

Finally, each process optionally refines its plan using `finish_plan` (again, a no-op by default), and the `StorageReader` performs the actual read operation based on the assigned `LoadPlan`. The reading itself is done in parallel across processes, though each process reads in a single thread. Once all reading is complete, the `load` function returns, and the `state_dict` should be fully populated with the restored values.

## Notes

* This document is based on [PyTorch v2.7.1](https://github.com/pytorch/pytorch/tree/v2.7.1/torch/distributed/checkpoint). All file paths mentioned are relative to `torch/distributed/checkpoint`, unless otherwise specified.
