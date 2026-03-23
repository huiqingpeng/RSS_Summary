---
title: "Beyond Weighted Summation: Learnable Nonlinear Aggregation Functions for Robust Artificial Neurons"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19344"
published: "2026-03-23"
fetched: "2026-03-24T07:17:38.198047"
---

Computer Science > Machine Learning
[Submitted on 19 Mar 2026]
Title:Beyond Weighted Summation: Learnable Nonlinear Aggregation Functions for Robust Artificial Neurons
View PDF HTML (experimental)Abstract:Weighted summation has remained the default input aggregation mechanism in artificial neurons since the earliest neural network models. While computationally efficient, this design implicitly behaves like a mean-based estimator and is therefore sensitive to noisy or extreme inputs. This paper investigates whether replacing fixed linear aggregation with learnable nonlinear alternatives can improve neural network robustness without sacrificing trainability. Two differentiable aggregation mechanisms are introduced: an F-Mean neuron based on a learnable power-weighted aggregation rule, and a Gaussian Support neuron based on distance-aware affinity weighting. To preserve the optimisation stability of standard neurons, hybrid neurons are proposed that interpolate between linear and nonlinear aggregation through a learnable blending parameter. Evaluated in multilayer perceptrons and convolutional neural networks on CIFAR-10 and a noisy CIFAR-10 variant with additive Gaussian corruption, hybrid neurons consistently improve robustness under noise while F-Mean hybrids also yield modest gains on clean data. The three-way hybrid achieves robustness scores of up to 0.991 compared to 0.890 for the standard baseline, and learned parameters converge consistently to sub-linear aggregation (p $\approx$ 0.43--0.50) and high novelty utilisation ($\alpha$ $\approx$ 0.69--0.79). These findings suggest that neuron-level aggregation is a meaningful and underexplored design dimension for building more noise-tolerant neural networks.
Submission history
From: Berke Deniz Bozyigit [view email][v1] Thu, 19 Mar 2026 15:32:12 UTC (13 KB)
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
