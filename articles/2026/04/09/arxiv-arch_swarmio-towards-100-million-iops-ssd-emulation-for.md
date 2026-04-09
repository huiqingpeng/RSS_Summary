---
title: "SwarmIO: Towards 100 Million IOPS SSD Emulation for Next-generation GPU-centric Storage Systems"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2604.06668"
published: "2026-04-09"
fetched: "2026-04-10T07:04:50.974338"
---

Computer Science > Hardware Architecture
[Submitted on 8 Apr 2026]
Title:SwarmIO: Towards 100 Million IOPS SSD Emulation for Next-generation GPU-centric Storage Systems
View PDF HTML (experimental)Abstract:GPU-initiated I/O has emerged as a key mechanism for achieving high-throughput storage access by leveraging massive GPU thread-level parallelism, while recent industry trends point toward SSDs optimized for ultra-high random-read IOPS. Together, these trends are enabling the emergence of IOPS-optimized, GPU-centric storage systems. Despite this momentum, no existing framework enables quantitative end-to-end evaluation of storage systems optimized for GPU-initiated I/O. While conventional SSD emulators provide a promising path toward end-to-end modeling in traditional storage systems, they face three key challenges in this GPU-centric setting: limited frontend scalability for ingesting massive request streams, high software overhead in emulating GPU-initiated I/O control and data paths, and excessive timing-model maintenance overhead at extremely high I/O request rates. We propose SwarmIO, an SSD emulator for massively parallel, GPU-centric storage. SwarmIO faithfully models IOPS-optimized SSDs at target performance levels of up to 40 MIOPS, achieving a 303.9x speedup over the state-of-the-art baseline SSD emulator under GPU-initiated I/O. We further demonstrate its utility through a vector search case study, showing that increasing SSD IOPS from 2.5 MIOPS to 40 MIOPS yields an average end-to-end speedup of up to 9.7x.
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
