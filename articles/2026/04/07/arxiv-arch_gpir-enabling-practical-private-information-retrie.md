---
title: "GPIR: Enabling Practical Private Information Retrieval with GPUs"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2604.04696"
published: "2026-04-07"
fetched: "2026-04-08T07:02:24.996381"
---

Computer Science > Cryptography and Security
[Submitted on 6 Apr 2026]
Title:GPIR: Enabling Practical Private Information Retrieval with GPUs
View PDF HTML (experimental)Abstract:Private information retrieval (PIR) allows private database queries but is hindered by intense server-side computation and memory traffic. Modern lattice-based PIR protocols typically involve three phases: ExpandQuery (expanding a query into encrypted indices), RowSel (encrypted row selection), and ColTor (recursive "column tournament" for final selection). ExpandQuery and ColTor primarily perform number-theoretic transforms (NTTs), whereas RowSel reduces to large-scale independent matrix-matrix multiplications (GEMMs). GPUs are theoretically ideal for these tasks, provided multi-client batching is used to achieve high throughput. However, batching fundamentally reshapes performance bottlenecks; while it amortizes database access costs, it expands working sets beyond the L2 cache capacity, causing divergent memory behaviors and excessive DRAM traffic.
We present GPIR, a GPU-accelerated PIR system that rethinks kernel design, data layout, and execution scheduling. We introduce a stage-aware hybrid execution model that dynamically switches between operation-level kernels, which execute each primitive operation separately, and stage-level kernels, which fuse all operations within a protocol stage into a single kernel to maximize on-chip data reuse. For RowSel, we identify a performance gap caused by a structural mismatch between NTT-driven data layouts and tiled GEMM access patterns, which is exacerbated by multi-client batching. We resolve this through a transposed-layout GEMM design and fine-grained pipelining. Finally, we extend GPIR to multi-GPU systems, scaling both query throughput and database capacity with negligible communication overhead. GPIR achieves up to 305.7x higher throughput than PIRonGPU, the state-of-the-art GPU implementation.
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
