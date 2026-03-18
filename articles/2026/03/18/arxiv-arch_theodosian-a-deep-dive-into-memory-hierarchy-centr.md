---
title: "Theodosian: A Deep Dive into Memory-Hierarchy-Centric FHE Acceleration"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2512.18345"
published: "2026-03-18"
fetched: "2026-03-18T15:32:04.065668"
---

Computer Science > Cryptography and Security
[Submitted on 20 Dec 2025 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:Theodosian: A Deep Dive into Memory-Hierarchy-Centric FHE Acceleration
View PDF HTML (experimental)Abstract:Fully homomorphic encryption (FHE) enables secure computation on encrypted data, mitigating privacy concerns in cloud and edge environments. However, due to its high compute and memory demands, extensive acceleration research has been pursued across diverse hardware platforms, especially GPUs. In this paper, we perform a microarchitectural analysis of CKKS, a popular FHE scheme, on modern GPUs. Focusing on the memory hierarchy, we demonstrate that dominant kernels remain bound by the on-chip L2 cache despite its high bandwidth, exposing a persistent inner memory wall beyond the conventional off-chip DRAM bottleneck. Further, we reveal that the overall CKKS throughput is constrained by low per-kernel hardware utilization, caused by insufficient intra-kernel parallelism. Motivated by these findings, we introduce Theodosian, a set of complementary, memory-aware optimizations that improve cache efficiency and reduce runtime overheads. Theodosian achieves 1.45--1.83x performance improvements over a highly optimized baseline, Cheddar, across representative CKKS workloads. On an RTX 5090, we reduce the bootstrapping latency for 32,768 complex numbers from 22.1ms to 15.2ms, and further to 12.8ms with additional algorithmic optimizations, establishing a new state-of-the-art GPU performance to the best of our knowledge.
Submission history
From: Jung Ho Ahn [view email][v1] Sat, 20 Dec 2025 12:18:29 UTC (506 KB)
[v2] Tue, 17 Mar 2026 07:24:08 UTC (496 KB)
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
