---
title: "A Survey of Neural Network Variational Monte Carlo from a Computing Workload Characterization Perspective"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.18126"
published: "2026-03-20"
fetched: "2026-03-20T12:03:59.223959"
---

Computer Science > Hardware Architecture
[Submitted on 18 Mar 2026]
Title:A Survey of Neural Network Variational Monte Carlo from a Computing Workload Characterization Perspective
View PDF HTML (experimental)Abstract:Neural Network Variational Monte Carlo (NNVMC) has emerged as a promising paradigm for solving quantum many-body problems by combining variational Monte Carlo with expressive neural-network wave-function ansätze. Although NNVMC can achieve competitive accuracy with favorable asymptotic scaling, practical deployment remains limited by high runtime and memory cost on modern graphics processing units (GPUs). Compared with language and vision workloads, NNVMC execution is shaped by physics-specific stages, including Markov-Chain Monte Carlo sampling, wave-function construction, and derivative/Laplacian evaluation, which produce heterogeneous kernel behavior and nontrivial bottlenecks. This paper provides a workload-oriented survey and empirical GPU characterization of four representative ansätze: PauliNet, FermiNet, Psiformer, and Orbformer. Using a unified profiling protocol, we analyze model-level runtime and memory trends and kernel-level behavior through family breakdown, arithmetic intensity, roofline positioning, and hardware utilization counters. The results show that end-to-end performance is often constrained by low-intensity elementwise and data-movement kernels, while the compute/memory balance varies substantially across ansätze and stages. Based on these findings, we discuss algorithm--hardware co-design implications for scalable NNVMC systems, including phase-aware scheduling, memory-centric optimization, and heterogeneous acceleration.
Current browse context:
cs.AR
Change to browse by:
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
