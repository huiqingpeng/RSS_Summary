---
title: "NCCL EP: Towards a Unified Expert Parallel Communication API for NCCL"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.13606"
published: "2026-03-25"
fetched: "2026-03-26T07:08:05.399299"
---

Computer Science > Distributed, Parallel, and Cluster Computing
[Submitted on 13 Mar 2026 (v1), last revised 24 Mar 2026 (this version, v2)]
Title:NCCL EP: Towards a Unified Expert Parallel Communication API for NCCL
View PDF HTML (experimental)Abstract:Mixture-of-Experts (MoE) architectures have become essential for scaling large language models, driving the development of specialized device-initiated communication libraries such as DeepEP, Hybrid-EP, and others. These libraries demonstrate the performance benefits of GPU-initiated RDMA for MoE dispatch and combine operations.
This paper presents NCCL EP (Expert Parallelism), a ground-up MoE communication library built entirely on NCCL's Device API. NCCL EP provides unified ncclEpDispatch and ncclEpCombine primitives with both C and Python interfaces, supporting Low-Latency (LL) mode for inference decoding and High-Throughput (HT) mode for training and inference prefill. LL targets small batch sizes (1-128 tokens) using direct all-to-all RDMA+NVLink mesh connectivity with double-buffered communication for overlapping dispatch and combine phases. HT targets large batches (4096+ tokens) using hierarchical communication that aggregates tokens within NVLink domains before inter-node RDMA transmission. Both modes leverage Device API for both intra- and inter-node communications, taking advantage of its topology awareness and optimized GPU-initiated implementation.
We evaluate NCCL EP on an H100-based cluster across multi-node configurations, demonstrating competitive LL kernel performance and presenting end-to-end results with vLLM integration. By building MoE communication natively within NCCL, NCCL EP provides a supported path for expert parallelism on current and emerging NVIDIA platforms.
Submission history
From: Aamir Shafi [view email][v1] Fri, 13 Mar 2026 21:28:22 UTC (16,630 KB)
[v2] Tue, 24 Mar 2026 00:05:55 UTC (12,332 KB)
Current browse context:
cs.DC
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
Papers with Code (What is Papers with Code?)
ScienceCast (What is ScienceCast?)
Demos
Recommenders and Search Tools
Influence Flower (What are Influence Flowers?)
CORE Recommender (What is CORE?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
