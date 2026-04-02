---
title: "Deep Networks Favor Simple Data"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00394"
published: "2026-04-02"
fetched: "2026-04-03T07:21:08.189664"
---

Computer Science > Machine Learning
[Submitted on 1 Apr 2026]
Title:Deep Networks Favor Simple Data
View PDF HTML (experimental)Abstract:Estimated density is often interpreted as indicating how typical a sample is under a model. Yet deep models trained on one dataset can assign \emph{higher} density to simpler out-of-distribution (OOD) data than to in-distribution test data. We refer to this behavior as the OOD anomaly. Prior work typically studies this phenomenon within a single architecture, detector, or benchmark, implicitly assuming certain canonical densities. We instead separate the trained network from the density estimator built from its representations or outputs. We introduce two estimators: Jacobian-based estimators and autoregressive self-estimators, making density analysis applicable to a wide range of models.
Applying this perspective to a range of models, including iGPT, PixelCNN++, Glow, score-based diffusion models, DINOv2, and I-JEPA, we find the same striking regularity that goes beyond the OOD anomaly: \textbf{lower-complexity samples receive higher estimated density, while higher-complexity samples receive lower estimated density}. This ordering appears within a test set and across OOD pairs such as CIFAR-10 and SVHN, and remains highly consistent across independently trained models. To quantify these orderings, we introduce Spearman rank correlation and find striking agreement both across models and with external complexity metrics. Even when trained only on the lowest-density (most complex) samples or \textbf{even a single such sample} the resulting models still rank simpler images as higher density.
These observations lead us beyond the original OOD anomaly to a more general conclusion: deep networks consistently favor simple data. Our goal is not to close this question, but to define and visualize it more clearly. We broaden its empirical scope and show that it appears across architectures, objectives, and density estimators.
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
