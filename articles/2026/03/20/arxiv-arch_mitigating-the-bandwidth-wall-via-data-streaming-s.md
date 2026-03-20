---
title: "Mitigating the Bandwidth Wall via Data-Streaming System-Accelerator Co-Design"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.19057"
published: "2026-03-20"
fetched: "2026-03-20T12:04:28.887451"
---

Computer Science > Hardware Architecture
[Submitted on 19 Mar 2026]
Title:Mitigating the Bandwidth Wall via Data-Streaming System-Accelerator Co-Design
View PDF HTML (experimental)Abstract:Transformers have revolutionized AI in natural language processing and computer vision, but their large computation and memory demands pose major challenges for hardware acceleration. In practice, end-to-end throughput is often limited by paged data movement and interconnect bandwidth rather than raw MAC count. This work proposes a unified system-accelerator co-design approach for transformer inference that jointly optimizes a matrix accelerator and its system integration through paged streaming dataflows and explicit overlap of compute and transfer. On the hardware side, we introduce MatrixFlow, a loosely coupled 16x16 systolic-array accelerator with a page-aligned block matrix multiplication method using 4 KB tiles, a small on-chip buffer of about 20 KB, and a pipelined schedule of DMA, compute, and DMA-out to utilize interconnect bandwidth efficiently. On the system side, we develop Gem5-AcceSys, an extension of the gem5 full-system simulator that explores standard interconnects such as PCIe and configurable memory hierarchies including Direct Memory, Direct Cache, and Device Memory modes with SMMU/TLB effects. We evaluate the co-design using gem5 simulations on representative transformer models including BERT and ViT across multiple data types and system setups. Results show up to 22x end-to-end speedup over a CPU-only baseline and 5x to 8x gains over state-of-the-art loosely and tightly coupled accelerators. We further show that a standard PCIe-based host-memory design can achieve about 80 percent of the performance of on-device HBM. Overall, paged streaming and pipeline overlap, rather than large local SRAMs, are the most effective levers for efficient transformer inference under realistic system constraints.
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
