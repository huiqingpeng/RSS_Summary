---
title: "Diversity-Aware Reverse Kullback-Leibler Divergence for Large Language Model Distillation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00223"
published: "2026-04-02"
fetched: "2026-04-03T07:18:46.105985"
---

Computer Science > Machine Learning
[Submitted on 31 Mar 2026]
Title:Diversity-Aware Reverse Kullback-Leibler Divergence for Large Language Model Distillation
View PDF HTML (experimental)Abstract:Reverse Kullback-Leibler (RKL) divergence has recently emerged as the preferred objective for large language model (LLM) distillation, consistently outperforming forward KL (FKL), particularly in regimes with large vocabularies and significant teacher-student capacity mismatch, where RKL focuses learning on dominant modes rather than enforcing dense alignment. However, RKL introduces a structural limitation that drives the student toward overconfident predictions. We first provide an analysis of RKL by decomposing its gradients into target and non-target components, and show that non-target gradients consistently push the target logit upward even when the student already matches the teacher, thereby reducing output diversity. In addition, RKL provides weak supervision over non-target classes, leading to poor tail alignment. To address these issues, we propose Diversity-aware RKL (DRKL), which removes this gradient effect and strengthens non-target supervision while preserving the optimization benefits of RKL. Extensive experiments across datasets and model families demonstrate that DRKL consistently outperforms FKL, RKL, and other state-of-the-art distillation objectives, achieving better performance and a superior fidelity-diversity trade-off.
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
