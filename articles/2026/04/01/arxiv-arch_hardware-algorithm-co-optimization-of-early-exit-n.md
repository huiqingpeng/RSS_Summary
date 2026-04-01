---
title: "Hardware-Algorithm Co-Optimization of Early-Exit Neural Networks for Multi-Core Edge Accelerators"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2512.04705"
published: "2026-04-01"
fetched: "2026-04-02T07:12:20.731408"
---

Computer Science > Computational Complexity
[Submitted on 4 Dec 2025 (v1), last revised 31 Mar 2026 (this version, v2)]
Title:Hardware-Algorithm Co-Optimization of Early-Exit Neural Networks for Multi-Core Edge Accelerators
View PDF HTML (experimental)Abstract:Deployment of dynamic neural networks on edge accelerators requires careful consideration of hardware constraints beyond conventional complexity metrics such as Multiply-Accumulate operations. In Early-Exiting Neural Networks (EENN), exit placement, quantization level, and hardware workload mapping interact in non-trivial ways, influencing memory traffic, accelerator utilization, and ultimately energy-latency trade-offs. These interactions remain insufficiently understood in existing Neural Architecture Search (NAS) approaches, which typically rely on proxy metrics or hardware-in-the-loop evaluation. This work presents a hardware-algorithm co-design framework for EENN that explicitly models the interplay between quantization, exit configuration, and multi-core accelerator mapping. Using analytical design space exploration, we characterize how small architectural variations can induce disproportionate changes in hardware efficiency due to tensor dimension alignment and dataflow effects. Building on this analysis, we formulate EENN deployment as a constrained multi-objective optimization problem balancing accuracy, energy-latency product, exit overhead, and dynamic inference behavior. Experimental results on CIFAR-10 demonstrate that the proposed framework identifies architectures achieving over 50\% reduction in energy-latency product compared to static baselines under 8-bit quantization. The results highlight the importance of deployment-aware co-design for dynamic inference on heterogeneous edge platforms.
Submission history
From: Alaa Zniber [view email][v1] Thu, 4 Dec 2025 11:54:09 UTC (459 KB)
[v2] Tue, 31 Mar 2026 12:32:50 UTC (481 KB)
Current browse context:
cs.CC
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
