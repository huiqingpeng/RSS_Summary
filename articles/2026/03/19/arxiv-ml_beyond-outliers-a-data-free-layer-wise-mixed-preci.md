---
title: "Beyond Outliers: A Data-Free Layer-wise Mixed-Precision Quantization Approach Driven by Numerical and Structural Dual-Sensitivity"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17354"
published: "2026-03-19"
fetched: "2026-03-19T12:10:10.871937"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:Beyond Outliers: A Data-Free Layer-wise Mixed-Precision Quantization Approach Driven by Numerical and Structural Dual-Sensitivity
View PDF HTML (experimental)Abstract:Layer-wise mixed-precision quantization (LMPQ) enables effective compression under extreme low-bit settings by allocating higher precision to sensitive layers. However, existing methods typically treat all intra-layer weight modules uniformly and rely on a single numerical property when estimating sensitivity, overlooking their distinct operational roles and structural characteristics. To address this, we propose NSDS, a novel calibration-free LMPQ framework driven by Numerical and Structural Dual-Sensitivity. Specifically, it first mechanistically decomposes each layer into distinct operational roles and quantifies their sensitivity from both numerical and structural perspectives. These dual-aspect scores are then aggregated into a unified layer-wise metric through a robust aggregation scheme based on MAD-Sigmoid and Soft-OR to guide bit allocation. Extensive experiments demonstrate that NSDS consistently achieves superior performance compared to various baselines across diverse models and downstream tasks, without relying on any calibration data.
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
