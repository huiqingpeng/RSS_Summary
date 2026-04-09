---
title: "Towards Accurate and Calibrated Classification: Regularizing Cross-Entropy From A Generative Perspective"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.06689"
published: "2026-04-09"
fetched: "2026-04-10T07:05:05.282361"
---

Computer Science > Machine Learning
[Submitted on 8 Apr 2026]
Title:Towards Accurate and Calibrated Classification: Regularizing Cross-Entropy From A Generative Perspective
View PDF HTML (experimental)Abstract:Accurate classification requires not only high predictive accuracy but also well-calibrated confidence estimates. Yet, modern deep neural networks (DNNs) are often overconfident, primarily due to overfitting on the negative log-likelihood (NLL). While focal loss variants alleviate this issue, they typically reduce accuracy, revealing a persistent trade-off between calibration and predictive performance. Motivated by the complementary strengths of generative and discriminative classifiers, we propose Generative Cross-Entropy (GCE), which maximizes $p(x|y)$ and is equivalent to cross-entropy augmented with a class-level confidence regularizer. Under mild conditions, GCE is strictly proper. Across CIFAR-10/100, Tiny-ImageNet, and a medical imaging benchmark, GCE improves both accuracy and calibration over cross-entropy, especially in the long-tailed scenario. Combined with adaptive piecewise temperature scaling (ATS), GCE attains calibration competitive with focal-loss variants without sacrificing accuracy.
Current browse context:
cs.LG
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
IArxiv Recommender
(What is IArxiv?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
