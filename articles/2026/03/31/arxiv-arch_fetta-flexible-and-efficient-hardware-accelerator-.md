---
title: "FETTA: Flexible and Efficient Hardware Accelerator for Tensorized Neural Network Training"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2504.06474"
published: "2026-03-31"
fetched: "2026-04-01T07:17:14.790096"
---

Computer Science > Hardware Architecture
[Submitted on 8 Apr 2025 (v1), last revised 29 Mar 2026 (this version, v2)]
Title:FETTA: Flexible and Efficient Hardware Accelerator for Tensorized Neural Network Training
View PDF HTML (experimental)Abstract:The increasing demand for on-device training of deep neural networks (DNNs) aims to leverage personal data for high-performance applications while addressing privacy concerns and reducing communication latency. However, resource-constrained platforms face significant challenges due to the intensive computational and memory demands of DNN training. Tensor decomposition emerges as a promising approach to compress model size without sacrificing accuracy. Nevertheless, training tensorized neural networks (TNNs) incurs non-trivial overhead and severe performance degradation on conventional accelerators due to complex tensor shaping requirements. To address these challenges, we propose FETTA, an algorithm and hardware co-optimization framework for efficient TNN training. On the algorithm side, we develop a contraction sequence search engine (CSSE) to identify the optimal contraction sequence with the minimal computational overhead. On the hardware side, FETTA features a flexible and efficient architecture equipped with a reconfigurable contraction engine (CE) array to support diverse dataflows. Furthermore, butterfly-based distribution and reduction networks are implemented to perform flexible tensor shaping operations during computation. Evaluation results demonstrate that FETTA achieves reductions of 20.5x/100.9x, 567.5x/45.03x, and 11609.7x/4544.8x in terms of processing latency, energy, and energy-delay product (EDP) over GPU and TPU, respectively. Moreover, working on the tensorized training, FETTA outperforms prior accelerators with a speedup of 3.87~14.63x, and an energy efficiency improvement of 1.41~2.73x on average.
Submission history
From: Jinming Lu [view email][v1] Tue, 8 Apr 2025 22:32:38 UTC (1,740 KB)
[v2] Sun, 29 Mar 2026 09:04:57 UTC (2,384 KB)
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
