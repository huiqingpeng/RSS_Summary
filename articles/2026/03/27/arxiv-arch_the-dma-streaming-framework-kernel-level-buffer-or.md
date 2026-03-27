---
title: "The DMA Streaming Framework: Kernel-Level Buffer Orchestration for High-Performance AI Data Paths"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.10030"
published: "2026-03-27"
fetched: "2026-03-28T07:09:08.133249"
---

Computer Science > Hardware Architecture
[Submitted on 26 Feb 2026 (v1), last revised 25 Mar 2026 (this version, v2)]
Title:The DMA Streaming Framework: Kernel-Level Buffer Orchestration for High-Performance AI Data Paths
View PDF HTML (experimental)Abstract:AI transport libraries move bytes efficiently, but they commonly assume that buffers are already correctly allocated, placed, shared, registered, and safe under completion and teardown pressure. This paper presents dmaplane, a Linux kernel module that makes this missing layer explicit as buffer orchestration. dmaplane exposes a stable kernel UAPI via /dev/dmaplane and composes ring-based command channels, DMA buffer lifecycle management, dma-buf export for cross-device sharing, a kernel-space RDMA engine, NUMA-aware allocation and verification, credit-based flow control, low-overhead observability, and GPU memory integration via PCIe BAR pinning. We evaluate orchestration sensitivity with measurements of NUMA cross-node penalties at DRAM scale, completion-safe flow control under sustained RDMA load, and GPU BAR mapping tiers versus cudaMemcpy. We also demonstrate end-to-end disaggregated inference by transferring KV-cache chunks between two machines using RDMA WRITE WITH IMMEDIATE and reconstructing tensor views on the receiver. RDMA measurements use Soft-RoCE; we distinguish measured results from provider-independent properties by construction.
Submission history
From: Marco Graziano [view email][v1] Thu, 26 Feb 2026 23:44:02 UTC (149 KB)
[v2] Wed, 25 Mar 2026 18:56:49 UTC (149 KB)
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
