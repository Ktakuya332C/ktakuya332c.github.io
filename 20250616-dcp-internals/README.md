# Pytorch Distributed Checkpoint Internals

Distributed checkpoint is a feature introduced to PyTorch some time ago, allowing developers to easily implement parallel checkpointing in a format that is independent of the cluster topology. Although the code looks modular and flexible, the documents and tutorials only focuses on the most surface level APIs, and its internals are scarcely documented. This post tries to provide a very rough guide to the internals of distributed checkpoint implementation, to someone who wants to modify some parts of the behaviors of distributed checkpoint, and to future me who probably forget all the implementation details I now hold in mind.

Rougly speaking, the implementation of the distributed checkpoint mainly consists of two classes, namely Planner (planner.py) and Storage (storage.py). Each process in a distributed process group has its own planner and storage, and they coordinate to save/load a checkpoint. The responsiblity of Planner is to determine what to save/load in each process by exchanging information globally across all the planners, and the one of Storage is to actually save/load tensors or bytes onto the disk/memory. These classes exchange information by some structs (dataclass) like SavePlan, LoadPlan, WriteItem, ReadItem, Metadata, and others.

I will try to describe the saving procedure first, and later the loading side.

## Saving procedure

To save a model with distributed checkpointing, each process must instantiate one subclass of StorageWriter (storage.py) and SavePlanner (planner.py) each before starting the actual saving. Usually, FileSystemWriter (filesystem.py) and DefaultSavePlanner (default_planner.py) would be chosen automatically when the caller didn't specify instances explicitly. From here on, I suppose the caller didn't specify the instances explicitly, and FileSystemWriter and DefaultSavePlanner are chosen and instantiated.

When a caller kicks `save` function (state_dict_saver.py), the planner and storage writer on each process coordinates to save the model. Usually, the caller only passes the state dict of the model and checkpoint_id to the `save` function. The procedure roughly follows the next diagram.

<img src="/20250616-dcp-internals/figure1.png" width="50%" />

At first, each process starts to setup themselves by calling `set_up_planner` of Planner and `set_up_storage_writer` of StorageWriter. These methods usually do a very little : `set_up_planner` of DefaultSavePlanner setup metadata of the state dict for later use, and `set_up_storage_writer` of FileSystemWriter does nothing.

Then, they proceed to create an object so called `local_plan` of type SavePlan (planner.py). `local_plan` essentially is a proposal by each process that specifies which parts of the model parameters the process is responsible to save. This proposal will be revised by the coordinator (Process 1 in the above figure) in a later step. The proposal is expressed as an instance of SavePlan (planner.py), which basically is a list of WriteItem (planner.py). WriteItem expresses a portion of the state dict, specifying the path to the tensor in the state dict, and its offset and size of the sub-tensor the WriteItem is responsible for.

The coordinator process (Process 1 in the above figure) then gathers the `local_plan`s each process created, adjust each plan, and create some metadata that requires global view of the whole plans. For example, `create_global_plan` of DefaultSavePlanner deduplicates the WriteItems, and creates Metadata (metadata.py) that will be used in the loading procedure. `prepare_global_plan` of FileSystemWriter assigns a prefix each process use to save a file (`__{i}_` with rank i), that requires global view of the whole plans because it must be different from each other.

Lastly, the coordinator distributes the adjusted plan to each process, and each process starts the actual saving of the state dict. Planner in each process is allowed to modify the plan once again at this time, but usually they do little. StorageWriter kicks the actual saving process, which writes tensors and bytes following the SavePlan each process is assigned to. After the writing completes, the result of all the writes are gathered into the coordinator, and the coordinator puts some end marks to the checkpoint, which is `.metadata` file in case of FileStorageWriter.

## Loading procedure

<img src="/20250616-dcp-internals/figure2.png" width="50%" />

## Notes
- This document is based on [PyTorch 2.7.1](https://github.com/pytorch/pytorch/tree/v2.7.1/torch/distributed/checkpoint). All the paths are relative to `torch/distributed/checkpoint` except explicitly mentioned otherwise. 

