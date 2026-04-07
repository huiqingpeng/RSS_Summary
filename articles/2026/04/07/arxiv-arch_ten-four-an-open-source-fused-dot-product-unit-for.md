---
title: "Ten-Four: An Open-Source Fused Dot Product Unit for Mixed-Precision GPGPU Tensor Cores"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2512.00053"
published: "2026-04-07"
fetched: "2026-04-08T07:02:26.482421"
---

Computer Science > Hardware Architecture
[Submitted on 19 Nov 2025 (v1), last revised 5 Apr 2026 (this version, v2)]
Title:Ten-Four: An Open-Source Fused Dot Product Unit for Mixed-Precision GPGPU Tensor Cores
View PDF HTML (experimental)Abstract:Efficient mixed-precision matrix multiply accumulate (MMA) operations are critical for accelerating deep learning workloads on GPGPUs. However, existing open-source dot product implementations for Tensor Cores rely on discrete arithmetic units, leading to high latency, accumulated rounding errors, and poor resource utilization. To address these challenges, we propose Ten-Four, a scalable mixed-precision fused dot product unit that integrates both the floating-point and integer arithmetic pipelines within a single fused architecture, implemented as part of the open-source RISC-V-based Vortex GPGPU's Tensor Core Unit extension. Our design supports low-precision multiplication in FP16/BF16/FP8/BF8/INT8/INT4 formats and higher-precision accumulation in FP32/INT32, with native support for Microscaling (MX) and sparse lane clock-gating for dynamic power reduction, while matching NVIDIA Tensor Core's numerical accuracy. Ten-Four achieves 4-cycle operation latency at 262.325 MHz Fmax, delivering 134.308 GFLOPS peak throughput per Tensor Core on the AMD Xilinx Alveo U55C FPGA, demonstrating ~3.1x performance improvement over an equivalent Berkeley HardFloat-based implementation at less than 60% the area cost.
Submission history
From: Nikhil Rout [view email][v1] Wed, 19 Nov 2025 15:57:09 UTC (154 KB)
[v2] Sun, 5 Apr 2026 15:41:28 UTC (372 KB)
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
