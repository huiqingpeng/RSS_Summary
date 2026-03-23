---
title: "Speculating Experts Accelerates Inference for Mixture-of-Experts"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19289"
published: "2026-03-23"
fetched: "2026-03-24T07:15:02.170675"
---

Computer Science > Machine Learning
[Submitted on 9 Mar 2026]
Title:Speculating Experts Accelerates Inference for Mixture-of-Experts
View PDF HTML (experimental)Abstract:Mixture-of-Experts (MoE) models have gained popularity as a means of scaling the capacity of large language models (LLMs) while maintaining sparse activations and reduced per-token compute. However, in memory-constrained inference settings, expert weights must be offloaded to CPU, creating a performance bottleneck from CPU-GPU transfers during decoding. We propose an expert prefetching scheme that leverages currently computed internal model representations to speculate future experts, enabling memory transfers to overlap with computation. Across multiple MoE architectures, we demonstrate that future experts can be reliably predicted by these internal representations. We also demonstrate that executing speculated experts generally maintains downstream task accuracy, thus preserving more effective compute-memory overlap by eliminating the need to re-fetch true router-selected experts. Integrated into an optimized inference engine, our approach achieves up to 14\% reduction in time per output token (TPOT) over on-demand loading of experts from CPU memory. For MoEs where speculative execution alone yields suboptimal accuracy, we further examine lightweight estimators that improve expert prediction hit rates, thereby reducing performance degradation. Our code is released in open-source at this https URL.
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
IArxiv Recommender
(What is IArxiv?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
