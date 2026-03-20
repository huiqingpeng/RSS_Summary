---
title: "Fundamental Limits of Neural Network Sparsification: Evidence from Catastrophic Interpretability Collapse"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18056"
published: "2026-03-20"
fetched: "2026-03-20T12:06:35.949958"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:Fundamental Limits of Neural Network Sparsification: Evidence from Catastrophic Interpretability Collapse
View PDFAbstract:Extreme neural network sparsification (90% activation reduction) presents a critical challenge for mechanistic interpretability: understanding whether interpretable features survive aggressive compression. This work investigates feature survival under severe capacity constraints in hybrid Variational Autoencoder--Sparse Autoencoder (VAE-SAE) architectures. We introduce an adaptive sparsity scheduling framework that progressively reduces active neurons from 500 to 50 over 50 training epochs, and provide empirical evidence for fundamental limits of the sparsification-interpretability relationship. Testing across two benchmark datasets -- dSprites and Shapes3D -- with both Top-k and L1 sparsification methods, our key finding reveals a pervasive paradox: while global representation quality (measured by Mutual Information Gap) remains stable, local feature interpretability collapses systematically. Under Top-k sparsification, dead neuron rates reach $34.4\pm0.9\%$ on dSprites and $62.7\pm1.3\%$ on Shapes3D at k=50. L1 regularization -- a fundamentally different "soft constraint" paradigm -- produces equal or worse collapse: $41.7\pm4.4\%$ on dSprites and $90.6\pm0.5\%$ on Shapes3D. Extended training for 100 additional epochs fails to recover dead neurons, and the collapse pattern is robust across all tested threshold definitions. Critically, the collapse scales with dataset complexity: Shapes3D (RGB, 6 factors) shows $1.8\times$ more dead neurons than dSprites (grayscale, 5 factors) under Top-k and $2.2\times$ under L1. These findings establish that interpretability collapse under sparsification is intrinsic to the compression process rather than an artifact of any particular algorithm, training duration, or threshold choice.
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
