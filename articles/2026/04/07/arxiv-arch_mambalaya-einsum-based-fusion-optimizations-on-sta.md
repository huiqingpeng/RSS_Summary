---
title: "Mambalaya: Einsum-Based Fusion Optimizations on State-Space Models"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2604.03829"
published: "2026-04-07"
fetched: "2026-04-08T07:02:19.084163"
---

Computer Science > Hardware Architecture
[Submitted on 4 Apr 2026]
Title:Mambalaya: Einsum-Based Fusion Optimizations on State-Space Models
View PDF HTML (experimental)Abstract:Mamba is an emerging, complex workload with various short-range and long-range dependencies, nonlinearities, and elementwise computations that are unable to run at near-peak speeds on modern hardware. Specifically, Mamba's complex dependency graph makes fusion across its full operator cascade difficult, leaving substantial inter-operator memory traffic on the table. To address these challenges, we propose Mambalaya, a novel reconfigurable accelerator that leverages fusion to overcome the limitations of Mamba. We use the recently proposed cascade-of-Einsums abstraction to characterize Mamba's full computational structure, then apply the extended Einsum framework to systematically explore inter-Einsum fusion opportunities. This principled approach yields a series of fusion mappings that reduce off-chip inter-Einsum traffic. These mappings are supported by the underlying Mambalaya architecture. Mambalaya achieves a layer performance speedup of 4.9$\times$ for prefill and 1.9$\times$ for generation over MARCA. In prefill-dominated scenarios, it achieves up to 1.5$\times$ over a recent fine-grained, memory-aware fusion accelerator for Mamba.
Submission history
From: Toluwanimi Odemuyiwa [view email][v1] Sat, 4 Apr 2026 19:02:52 UTC (1,543 KB)
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
