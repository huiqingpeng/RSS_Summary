---
title: "ENEC: A Lossless AI Model Compression Method Enabling Fast Inference on Ascend NPUs"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2604.03298"
published: "2026-04-07"
fetched: "2026-04-08T07:02:16.190526"
---

Computer Science > Hardware Architecture
[Submitted on 28 Mar 2026]
Title:ENEC: A Lossless AI Model Compression Method Enabling Fast Inference on Ascend NPUs
View PDF HTML (experimental)Abstract:The rapid scaling of Large Language Models presents significant challenges for their deployment and inference, particularly on resource-constrained specialized AI hardware accelerators such as Huawei's Ascend NPUs, where weight data transfer has become a critical performance bottleneck. While lossless compression can preserve model accuracy and reduce data volume, existing lossless compression algorithms exhibit extremely low throughput when ported to the Ascend NPU architecture. In this paper, we propose ENEC, a novel lossless compression method specifically customized for AI model weights and optimized for Ascend Neural Processing Units. ENEC adopts a block-based fixed-length encoding scheme and incorporates a series of NPU-specific optimizations: bit-width quantization with hierarchical halving bit-packing, vectorized branch-free integer transformation, and dependency-decoupled intra-segment scan for efficient prefix-sum computation. Experimental results demonstrate that ENEC outperforms existing state-of-the-art NPU compressors in both compression ratio and throughput. Compared to leading GPU solutions, ENEC achieves a 3.43X higher throughput than DietGPU and a 1.12X better compression ratio than nvCOMP. By reducing weight transmission overhead, ENEC significantly improves end-to-end inference performance, achieving up to a 6.3X speedup. On Ascend NPUs, ENEC is the first open-source lossless compression algorithm for model weights that achieves performance comparable to state-of-the-art GPU compressors, offering an effective solution for deploying large-scale AI models.
Current browse context:
cs.AR
References & Citations
export BibTeX citation
Loading...
Bibliographic and Citation Tools
Bibliographic Explorer (What is the Explorer?)
Connected Papers (What is Connected Papers?)
Litmaps (What is Litmaps?)
scite Smart Citations (What are Smart Citations?)
Code, Data and Media Associated with this Article
alphaXiv (What is alphaXiv?)
CatalyzeX Code Finder for Papers (What is CatalyzeX?)
DagsHub (What is DagsHub?)
Gotit.pub (What is GotitPub?)
Hugging Face (What is Huggingface?)
ScienceCast (What is ScienceCast?)
Demos
Recommenders and Search Tools
Influence Flower (What are Influence Flowers?)
CORE Recommender (What is CORE?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
