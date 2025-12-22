# Distribueted Training Resources

A list of documents and videos useful for understanding distributed training systems.

General
- (2025, Book) [The Ultra-Scale Playbook](https://huggingface.co/spaces/nanotron/ultrascale-playbook)
- (2025, Paper) [Insights into DeepSeek-V3: Scaling Challenges and Reflections on Hardware for AI Architectures](https://arxiv.org/abs/2505.09343)
- (2024, Paper) [DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models](https://arxiv.org/abs/2401.06066)
- (2024, Paper) [The Llama 3 Herd of Models](https://arxiv.org/abs/2407.21783)
- (2024, Paper) [MegaScale: Scaling Large Language Model Training to More Than 10,000 GPUs](https://arxiv.org/abs/2402.15627)

3D Parallelism
- (2024, Paper) [Hardware Scaling Trends and Diminishing Returns in Large-Scale Distributed Training](https://arxiv.org/abs/2411.13055)
- (2024, Paper) [Domino: Eliminating Communication in LLM Training via Generic Tensor Slicing and Overlapping](https://arxiv.org/abs/2409.15241)
- (2024, Paper) [SimpleFSDP: Simpler Fully Sharded Data Parallel with torch.compile](https://arxiv.org/abs/2411.00284)
- (2024, Paper) [Efficient Parallelization Layouts for Large-Scale Distributed Model Training](https://arxiv.org/abs/2311.05610)
- (2024, Blog) [Introducing Async Tensor Parallelism in PyTorch](https://discuss.pytorch.org/t/distributed-w-torchtitan-introducing-async-tensor-parallelism-in-pytorch/209487/1)
- (2023, Paper) [Zero Bubble Pipeline Parallelism](https://arxiv.org/abs/2401.10241)
- (2023, Paper) [AMSP: Reducing Communication Overhead of ZeRO for Efficient LLM Training](https://arxiv.org/abs/2311.00257)
- (2023, Paper) [PyTorch FSDP: Experiences on Scaling Fully Sharded Data Parallel](https://arxiv.org/abs/2304.11277)
- (2022, Video) [Ultimate Guide to Scaling ML Models](https://www.youtube.com/watch?v=hc0u4avAkuM)
- (2022, Video) [BigScience BLOOM 3D Parallelism explained](https://www.youtube.com/watch?v=pTChDs5uD8I)
- (2021, Paper) [Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM](https://arxiv.org/abs/2104.04473)
- (2019, Paper) [ZeRO: Memory Optimizations Toward Training Trillion Parameter Models](https://arxiv.org/abs/1910.02054)

Mixed Precision
- (2025, Paper) [Quartet: Native FP4 Training Can Be Optimal for Large Language Models](https://arxiv.org/abs/2505.14669)
- (2025, Paper) [Recipes for Pretraining LLMs with MXFP8](https://arxiv.org/abs/2506.08027)
- (2025, Paper) [Pretraining Large Language Models with NVFP4](https://arxiv.org/abs/2509.25149)
- (2024, Paper) [The Era of 1-bit LLMs: All Large Language Models are in 1.58 Bits](https://arxiv.org/abs/2402.17764)
- (2022, Paper) [FP8 Formats for Deep Learning](https://arxiv.org/abs/2209.05433)
- (2019, Paper) [Hybrid 8-bit Floating Point (HFP8) Training and Inference for Deep Neural Networks](https://papers.nips.cc/paper_files/paper/2019/hash/65fc9fb4897a89789352e211ca2d398f-Abstract.html)

Long Context Training
- (2025, Blog) [CAD: Disaggregating Core Attention for Efficient Long-context Language Model Training](https://hao-ai-lab.github.io/blogs/distca/)
- (2025, Paper) [ByteScale: Efficient Scaling of LLM Training with a 2048K Context Length on More Than 12,000 GPUs](https://arxiv.org/abs/2502.21231)
- (2025, Paper) [HelixPipe: Efficient Distributed Training of Long Sequence Transformers with Attention Parallel Pipeline Parallelism](https://arxiv.org/abs/2507.00394)
- (2024, Paper) [When Precision Meets Position: BFloat16 Breaks Down RoPE in Long-Context Training](https://arxiv.org/abs/2411.13476)
- (2023, Paper) [Ring Attention with Blockwise Transformers for Near-Infinite Context](https://arxiv.org/abs/2310.01889)
- (2023, Paper) [DeepSpeed Ulysses: System Optimizations for Enabling Training of Extreme Long Sequence Transformer Models](https://arxiv.org/abs/2309.14509)
- (2022, Paper) [Reducing Activation Recomputation in Large Transformer Models](https://arxiv.org/abs/2205.05198)

Mixture of Experts
- (2025, Paper) [MoE Parallel Folding: Heterogeneous Parallelism Mappings for Efficient Large-Scale MoE Model Training with Megatron Core](https://arxiv.org/abs/2504.14960)
- (2024, Paper) [Scattered Mixture-of-Experts Implementation](https://arxiv.org/abs/2403.08245)
- (2022, Paper) [MegaBlocks: Efficient Sparse Training with Mixture-of-Experts](https://arxiv.org/abs/2211.15841)

Checkpointing
- (2023, Paper) [GEMINI: Fast Failure Recovery in Distributed Training with In-Memory Checkpoints](https://dl.acm.org/doi/10.1145/3600006.3613145)
- (2023, Paper) [Gemini: A Family of Highly Capable Multimodal Models](https://arxiv.org/abs/2312.11805)

Cross Data Center Training
- (2025, Paper) [Collective Communication for 100k+ GPUs](https://arxiv.org/abs/2510.20171v1)
- (2025, Blog) [Turbocharge LLM Training Across Long-Haul Data Center Networks with NVIDIA Nemo Framework](https://developer.nvidia.com/blog/turbocharge-llm-training-across-long-haul-data-center-networks-with-nvidia-nemo-framework/)
- (2025, Blog) [Streaming DiLoCo with overlapping communication](https://arxiv.org/abs/2501.18512)
- (2024, Blog) [DiPaCo: Distributed Path Composition](https://arxiv.org/abs/2403.10616)
- (2023, Paper) [DiLoCo: Distributed Low-Communication Training of Language Models](https://arxiv.org/abs/2311.08105)

Infrastructure
- (2024, Paper) [Fire-Flyer AI-HPC: A Cost-Effective Software-Hardware Co-Design for Deep Learning](https://arxiv.org/abs/2408.14158)
- (2024, Paper) [Revisiting Reliability in Large-Scale Machine Learning Research Clusters](https://arxiv.org/abs/2410.21680)
- (2024, Blog) [100,000 H100 Clusters: Power, Network Topology, Ethernet vs InfiniBand, Reliability, Failures, Checkpointing](https://newsletter.semianalysis.com/p/100000-h100-clusters-power-network)
- (2022, Paper) [Pathways: Asynchronous Distributed Dataflow for ML](https://arxiv.org/abs/2203.12533)

Practical Tips
- (2024, Blog) [A practitioner's guide to testing and running large GPU clusters for training generative AI models](https://www.together.ai/blog/a-practitioners-guide-to-testing-and-running-large-gpu-clusters-for-training-generative-ai-models)
- (Github) [Machine Learning Engineering Open Book](https://github.com/stas00/ml-engineering)
- (2024, Blog) [Training great LLMs entirely from ground up in the wilderness as a startup](https://www.yitay.net/blog/training-great-llms-entirely-from-ground-zero-in-the-wilderness)
