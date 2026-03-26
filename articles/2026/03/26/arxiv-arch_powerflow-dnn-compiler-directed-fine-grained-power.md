---
title: "PowerFlow-DNN: Compiler-Directed Fine-Grained Power Orchestration for End-to-End Edge AI Inference"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.23882"
published: "2026-03-26"
fetched: "2026-03-27T07:12:44.777809"
---

Computer Science > Hardware Architecture
[Submitted on 25 Mar 2026]
Title:PowerFlow-DNN: Compiler-Directed Fine-Grained Power Orchestration for End-to-End Edge AI Inference
View PDF HTML (experimental)Abstract:Edge AI systems often operate under stringent energy and volume constraints that demand extreme efficiency under limited battery capacity, with requirements worsening as intelligent capability demands advance. Prior literature suggests that fine-grained power orchestration, including DVFS and power gating, enables significant energy efficiency benefits that cannot be left unexploited, while still exhibiting unexplored challenges. We observe that layer-level approaches incur unintended overheads due to inter-layer coupling of power control decisions, and that jointly managing these mechanisms under practical constraints such as limited voltage rails and transition overheads leads to a rapidly growing combinatorial schedule space. To address this, we propose PowerFlow-DNN, a compiler-directed framework for end-to-end power-state orchestration in ultra-low-power accelerators. By constructing a rigorous problem formulation for deadline-constrained, real-time, periodic inference as a unified inter-layer power-scheduling problem, our framework enables automated discovery of energy-minimal power-state schedules that adhere to a deadline while accounting for end-to-end, inter-layer impacts. We evaluate the framework on a DNN accelerator VLSI implementation in TSMC 40nm technology. Across representative edge networks, we show that PowerFlow-DNN discovers near-optimal solutions under the discretized formulation and achieves energy within 0.68\% of the exact ILP oracle, reducing energy by up to 37\% compared to an aggressive baseline without power orchestration, while reasoning over a combinatorial schedule space of over $10^{160}$ possible power-state assignments, yet operating on a structured layered state graph that enables efficient optimization, achieving up to 2.14$\times$ solver speedup via lightweight pruning.
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
