---
title: "Variational Kernel Design for Internal Noise: Gaussian Chaos Noise, Representation Compatibility, and Reliable Deep Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17365"
published: "2026-03-19"
fetched: "2026-03-19T12:10:22.898253"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:Variational Kernel Design for Internal Noise: Gaussian Chaos Noise, Representation Compatibility, and Reliable Deep Learning
View PDF HTML (experimental)Abstract:Internal noise in deep networks is usually inherited from heuristics such as dropout, hard masking, or additive perturbation. We ask two questions: what correlation geometry should internal noise have, and is the implemented perturbation compatible with the representations it acts on? We answer these questions through Variational Kernel Design (VKD), a framework in which a noise mechanism is specified by a law family, a correlation kernel, and an injection operator, and is derived from learning desiderata. In a solved spatial subfamily, a quadratic maximum-entropy principle over latent log-fields yields a Gaussian optimizer with precision given by the Dirichlet Laplacian, so the induced geometry is the Dirichlet Green kernel. Wick normalization then gives a canonical positive mean-one gate, Gaussian Chaos Noise (GCh). For the sample-wise gate used in practice, we prove exact Gaussian control of pairwise log-ratio deformation, margin-sensitive ranking stability, and an exact expected intrinsic roughness budget; hard binary masks instead induce singular or coherence-amplified distortions on positive coherent representations. On ImageNet and ImageNet-C, GCh consistently improves calibration and under shift also improves NLL at competitive accuracy.
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
