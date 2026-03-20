---
title: "T-QPM: Enabling Temporal Out-Of-Distribution Detection and Domain Generalization for Vision-Language Models in Open-World"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18481"
published: "2026-03-20"
fetched: "2026-03-20T13:13:12.799095"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 19 Mar 2026]
Title:T-QPM: Enabling Temporal Out-Of-Distribution Detection and Domain Generalization for Vision-Language Models in Open-World
View PDF HTML (experimental)Abstract:Out-of-distribution (OOD) detection remains a critical challenge in open-world learning, where models must adapt to evolving data distributions. While recent vision-language models (VLMS) like CLIP enable multimodal OOD detection through Dual-Pattern Matching (DPM), existing methods typically suffer from two major shortcomings: (1) They rely on fixed fusion rules and assume static environments, failing under temporal drift; and (2) they lack robustness against covariate shifted inputs. In this paper, we propose a novel two-step framework to enhance OOD detection and covariate distribution shift robustness in dynamic settings. We extend the dual-pattern regime into Temporal Quadruple-Pattern Matching (T-QPM). First, by pairing OOD images with text descriptions, we introduce cross-modal consistency patterns between ID and OOD signals, refining the decision boundary through joint image-text reasoning. Second, we address temporal distribution shifts by learning lightweight fusion weights to optimally combine semantic matching and visual typicality. To ensure stability, we enforce explicit regularization based on Average Thresholded Confidence (ATC), preventing performance degradation as distributions evolve. Experiments on temporally partitioned benchmarks demonstrate that our approach significantly outperforms static baselines, offering a robust, temporally-consistent framework for multimodal OOD detection in non-stationary environments.
Submission history
From: Aditi Naiknaware [view email][v1] Thu, 19 Mar 2026 04:35:38 UTC (6,093 KB)
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
