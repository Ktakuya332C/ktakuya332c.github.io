# Pytorch Distributed Checkpoint Internals

Distributed checkpoint is a feature introduced to PyTorch some time ago, allowing developers to easily implement parallel checkpointing in a format that is independent of the cluster topology. To accomodate various checkpoint formats and checkpointing algorithms, distributed checkpoint is implemented in a very flexible and modular way that we can tweak the behavior of the checkpointing with minimal code changes. For example, NVIDIA/Megatron-LM leverages the modularity of the distributed checkpoint implementation in PyTorch to provide its own implementation of distributed checkpointing mechanism optimized for their models.

Although the code looks modular and flexible, the documents and tutorials only focuses on the most surface level APIs, and its internals are scarcely documented. This post tries to provide a very rough guide to the internals of distributed checkpoint implementation, to someone who wants to modify some parts of the behaviors of distributed checkpoint, and to future me who probably forget all the implementation details I now hold in mind.

Rougly speaking, the implementation of the distributed checkpoint mainly consists of two classes, namely Planner (planner.py) and Storage (storage.py). Each process in a distributed process group has its own planner and storage, and they coordinate to save/load a checkpoint. The responsiblity of Planner is to determine what to save/load in each process by exchanging information globally across all the planners, and the one of Storage is to actually save/load tensors or bytes onto the disk/memory. These classes exchange information by some structs (dataclass) like SavePlan, LoadPlan, WriteItem, ReadItem, Metadata, and others.

I will try to describe the saving procedure first, and later loading side.

## Saving procedure

TBWcd 

## Notes
- This document is based on [PyTorch 2.7.1](https://github.com/pytorch/pytorch/tree/v2.7.1/torch/distributed/checkpoint). All the paths are relative to `torch/distributed/checkpoint` except explicitly mentioned otherwise. 

