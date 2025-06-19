# Pytorch Distributed Checkpoint Internals

Distributed checkpoint is a feature introduced to PyTorch some time ago, allowing developers to easily implement parallel checkpointing in a format that is independent of the cluster topology. Although the code looks modular and flexible, the documents and tutorials only focuses on the most surface level APIs, and its internals are scarcely documented. This post tries to provide a very rough guide to the internals of distributed checkpoint implementation, to someone who wants to modify some parts of the behaviors of distributed checkpoint, and to future me who probably forget all the implementation details I now hold in mind.

Rougly speaking, the implementation of the distributed checkpoint mainly consists of two classes, namely Planner (planner.py) and Storage (storage.py). Each process in a distributed process group has its own planner and storage, and they coordinate to save/load a checkpoint. The responsiblity of Planner is to determine what to save/load in each process by exchanging information globally across all the planners, and the one of Storage is to actually save/load tensors or bytes onto the disk/memory. These classes exchange information by some structs (dataclass) like SavePlan, LoadPlan, WriteItem, ReadItem, Metadata, and others.

I will try to describe the saving procedure first, and later the loading side.

## Saving procedure

To save a model with distributed checkpointing, each process must instantiate one subclass of StorageWriter (storage.py) and SavePlanner (planner.py) each before starting the actual saving. Usually, FileSystemWriter (filesystem.py) and DefaultSavePlanner (default_planner.py) would be chosen automatically when the caller didn't specify instances explicitly. From here on, I suppose the caller didn't specify the instances explicitly, and FileSystemWriter and DefaultSavePlanner are chosen and instantiated.

When a caller kicks `save` function (state_dict_saver.py), the planner and storage writer on each process coordinates to save the model roughly following the next diagram.

<img src="/20250616-dcp-internals/figure1.png" width="50%" />

## Loading procedure

<img src="/20250616-dcp-internals/figure2.png" width="50%" />

## Notes
- This document is based on [PyTorch 2.7.1](https://github.com/pytorch/pytorch/tree/v2.7.1/torch/distributed/checkpoint). All the paths are relative to `torch/distributed/checkpoint` except explicitly mentioned otherwise. 

