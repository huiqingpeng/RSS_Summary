---
title: "DeepStack: Scalable and Accurate Design Space Exploration for Distributed 3D-Stacked AI Accelerators"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2604.04750"
published: "2026-04-07"
fetched: "2026-04-08T07:02:21.955374"
---

Computer Science > Hardware Architecture
[Submitted on 6 Apr 2026]
Title:DeepStack: Scalable and Accurate Design Space Exploration for Distributed 3D-Stacked AI Accelerators
View PDF HTML (experimental)Abstract:Advances in hybrid bonding and packaging have driven growing interest in 3D DRAM-stacked accelerators with higher memory bandwidth and capacity. As LLMs scale to hundreds of billions or trillions of parameters, distributed inference across multiple 3D chips becomes essential. With cross-stack co-design increasingly critical, we propose DeepStack, an accurate and efficient performance model and tool to enable early-stage system-hardware co-design space exploration (DSE) for distributed 3D-stacked AI systems. At the hardware level, DeepStack captures fine-grained 3D memory semantics such as transaction-aware bandwidth, bank activation constraints, buffering limitations, and thermal-power modeling. At the system level, DeepStack incorporates comprehensive parallelization strategies and execution scheduling for distributed LLM inference. With novel modeling techniques such as dual-stage network abstraction and tile-level compute-communication overlap, we achieve up to 100,000x faster runtime over state-of-the-art simulators at comparable accuracy, cross-validated against our in-house 3D designs, NS-3 backend (2.12%), and vLLM serving on 8xB200 GPUs (12.18%). With hierarchical design space search, DeepStack enables efficient exploration over 2.5x10^14 design points spanning 3D-stacked DRAM layers, DRAM vertical connectivity, interconnect, compute-memory allocation, and distributed scheduling. Compared with baseline designs, DeepStack achieves up to 9.5x higher throughput through co-optimized parallelism and 3D architecture search. Our DSE further reveals that batch size drives a more fundamental architectural divide than the prefill/decode distinction, and that parallelism strategy and hardware architecture are tightly coupled -- incomplete schedule search leads to permanently suboptimal silicon irrecoverable by software tuning. We intend to open source DeepStack to support future research.
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
