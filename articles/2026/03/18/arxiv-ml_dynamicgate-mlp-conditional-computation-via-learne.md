---
title: "DynamicGate MLP Conditional Computation via Learned Structural Dropout and Input Dependent Gating for Functional Plasticity"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16367"
published: "2026-03-18"
fetched: "2026-03-18T15:42:59.304210"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:DynamicGate MLP Conditional Computation via Learned Structural Dropout and Input Dependent Gating for Functional Plasticity
View PDF HTML (experimental)Abstract:Dropout is a representative regularization technique that stochastically deactivates hidden units during training to mitigate overfitting. In contrast, standard inference executes the full network with dense computation, so its goal and mechanism differ from conditional computation, where the executed operations depend on the input. This paper organizes DynamicGate-MLP into a single framework that simultaneously satisfies both the regularization view and the conditional-computation view. Instead of a random mask, the proposed model learns gates that decide whether to use each unit (or block), suppressing unnecessary computation while implementing sample-dependent execution that concentrates computation on the parts needed for each input. To this end, we define continuous gate probabilities and, at inference time, generate a discrete execution mask from them to select an execution path. Training controls the compute budget via a penalty on expected gate usage and uses a Straight-Through Estimator (STE) to optimize the discrete mask. We evaluate DynamicGate-MLP on MNIST, CIFAR-10, Tiny-ImageNet, Speech Commands, and PBMC3k, and compare it with various MLP baselines and MoE-style variants. Compute efficiency is compared under a consistent criterion using gate activation ratios and a layerweighted relative MAC metric, rather than wall-clock latency that depends on hardware and backend kernels.
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
