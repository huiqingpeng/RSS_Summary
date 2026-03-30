---
title: "AcTTA: Rethinking Test-Time Adaptation via Dynamic Activation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26096"
published: "2026-03-30"
fetched: "2026-03-31T07:21:24.635689"
---

Computer Science > Machine Learning
[Submitted on 27 Mar 2026]
Title:AcTTA: Rethinking Test-Time Adaptation via Dynamic Activation
View PDF HTML (experimental)Abstract:Test-time adaptation (TTA) aims to mitigate performance degradation under distribution shifts by updating model parameters during inference. Existing approaches have primarily framed adaptation around affine modulation, focusing on recalibrating normalization layers. This perspective, while effective, overlooks another influential component in representation dynamics: the activation function. We revisit this overlooked space and propose AcTTA, an activation-aware framework that reinterprets conventional activation functions from a learnable perspective and updates them adaptively at test time. AcTTA reformulates conventional activation functions (e.g., ReLU, GELU) into parameterized forms that shift their response threshold and modulate gradient sensitivity, enabling the network to adjust activation behavior under domain shifts. This functional reparameterization enables continuous adjustment of activation behavior without modifying network weights or requiring source data. Despite its simplicity, AcTTA achieves robust and stable adaptation across diverse corruptions. Across CIFAR10-C, CIFAR100-C, and ImageNet-C, AcTTA consistently surpasses normalization-based TTA methods. Our findings highlight activation adaptation as a compact and effective route toward domain-shift-robust test-time learning, broadening the prevailing affine-centric view of adaptation.
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
