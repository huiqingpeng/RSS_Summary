---
title: "Per-Bank Memory Bandwidth Regulation for Predictable and Performant Real-Time System"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.26054"
published: "2026-03-30"
fetched: "2026-03-31T07:06:14.970122"
---

Computer Science > Hardware Architecture
[Submitted on 27 Mar 2026]
Title:Per-Bank Memory Bandwidth Regulation for Predictable and Performant Real-Time System
View PDF HTML (experimental)Abstract:Modern multicore system-on-chips (SoCs) share off-chip DRAM across cores, where bank-level interference can significantly degrade performance and threaten real-time guarantees. While prior work has focused on per-core bandwidth regulation, these approaches treat main memory as a monolithic resource and overlook DRAM's inherent bank-level parallelism.
We show that DRAM interference is fundamentally a bank-level phenomenon. We characterize the guaranteed bandwidth of modern DRAM, demonstrate that it remains effectively constant across generations, and show how this limitation can be exploited by single-bank attacks. These results highlight the need for bank-aware memory management for predictable and efficient real-time systems.
We design and implement a novel per-bank memory bandwidth regulator in an open-source RISC-V SoC and evaluate it using FireSim with both synthetic and real-world workloads. Our evaluation demonstrates that per-bank regulation effectively mitigates adversarial bank contention and achieves a 5.74x average throughput improvement for best-effort workloads over traditional bank-oblivious approaches while providing the same-level of performance isolation guarantees for real-time workloads.
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
