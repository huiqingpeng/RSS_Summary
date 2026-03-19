---
title: "Auto-Unrolled Proximal Gradient Descent: An AutoML Approach to Interpretable Waveform Optimization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17478"
published: "2026-03-19"
fetched: "2026-03-19T12:12:20.804496"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:Auto-Unrolled Proximal Gradient Descent: An AutoML Approach to Interpretable Waveform Optimization
View PDF HTML (experimental)Abstract:This study explores the combination of automated machine learning (AutoML) with model-based deep unfolding (DU) for optimizing wireless beamforming and waveforms. We convert the iterative proximal gradient descent (PGD) algorithm into a deep neural network, wherein the parameters of each layer are learned instead of being predetermined. Additionally, we enhance the architecture by incorporating a hybrid layer that performs a learnable linear gradient transformation prior to the proximal projection. By utilizing AutoGluon with a tree-structured parzen estimator (TPE) for hyperparameter optimization (HPO) across an expanded search space, which includes network depth, step-size initialization, optimizer, learning rate scheduler, layer type, and post-gradient activation, the proposed auto-unrolled PGD (Auto-PGD) achieves 98.8% of the spectral efficiency of a traditional 200-iteration PGD solver using only five unrolled layers, while requiring only 100 training samples. We also address a gradient normalization issue to ensure consistent performance during training and evaluation, and we illustrate per-layer sum-rate logging as a tool for transparency. These contributions highlight a notable reduction in the amount of training data and inference cost required, while maintaining high interpretability compared to conventional black-box architectures.
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
