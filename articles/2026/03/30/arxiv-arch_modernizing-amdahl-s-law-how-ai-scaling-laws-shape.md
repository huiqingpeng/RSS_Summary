---
title: "Modernizing Amdahl's Law: How AI Scaling Laws Shape Computer Architecture"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.20654"
published: "2026-03-30"
fetched: "2026-03-31T07:17:27.633982"
---

Computer Science > Distributed, Parallel, and Cluster Computing
[Submitted on 21 Mar 2026 (v1), last revised 27 Mar 2026 (this version, v2)]
Title:Modernizing Amdahl's Law: How AI Scaling Laws Shape Computer Architecture
View PDFAbstract:Classical Amdahl's Law assumes a fixed decomposition between serial and parallel work and homogeneous replication; historically, it bounds how much parallel speedup is attainable. Modern systems instead combine specialized accelerators with programmable compute, tensor datapaths, and evolving pipelines, while empirical scaling laws shift which stages absorb marginal compute. The central tension is therefore not the serial-versus-parallel split alone, but resource allocation across heterogeneous hardware, given efficiency differences, and workload structures that determine how effectively additional compute can be converted into value. We reformulate Amdahl's Law for modern heterogeneous systems with scalable workloads. The analysis yields a finite collapse threshold: beyond a critical scalable fraction, specialization becomes suboptimal for any efficiency advantage of specialized hardware over programmable compute, and optimal specialized investment falls to zero, a phase transition rather than an asymptotic tail. We use this framework to interpret increasing GPU programmability and why domain-specific AI accelerators have not displaced GPUs.
Submission history
From: Chien-Ping Lu [view email][v1] Sat, 21 Mar 2026 05:19:18 UTC (2,153 KB)
[v2] Fri, 27 Mar 2026 03:27:27 UTC (2,155 KB)
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
