---
title: "ResNets of All Shapes and Sizes: Convergence of Training Dynamics in the Large-scale Limit"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18168"
published: "2026-03-20"
fetched: "2026-03-20T13:10:04.583471"
---

Statistics > Machine Learning
[Submitted on 18 Mar 2026]
Title:ResNets of All Shapes and Sizes: Convergence of Training Dynamics in the Large-scale Limit
View PDFAbstract:We establish convergence of the training dynamics of residual neural networks (ResNets) to their joint infinite depth L, hidden width M, and embedding dimension D limit. Specifically, we consider ResNets with two-layer perceptron blocks in the maximal local feature update (MLU) regime and prove that, after a bounded number of training steps, the error between the ResNet and its large-scale limit is O(1/L + sqrt(D/(L M)) + 1/sqrt(D)). This error rate is empirically tight when measured in embedding space. For a budget of P = Theta(L M D) parameters, this yields a convergence rate O(P^(-1/6)) for the scalings of (L, M, D) that minimize the bound. Our analysis exploits in an essential way the depth-two structure of residual blocks and applies formally to a broad class of state-of-the-art architectures, including Transformers with bounded key-query dimension. From a technical viewpoint, this work completes the program initiated in the companion paper [Chi25] where it is proved that for a fixed embedding dimension D, the training dynamics converges to a Mean ODE dynamics at rate O(1/L + sqrt(D)/sqrt(L M)). Here, we study the large-D limit of this Mean ODE model and establish convergence at rate O(1/sqrt(D)), yielding the above bound by a triangle inequality. To handle the rich probabilistic structure of the limit dynamics and obtain one of the first rigorous quantitative convergence for a DMFT-type limit, we combine the cavity method with propagation of chaos arguments at a functional level on so-called skeleton maps, which express the weight updates as functions of CLT-type sums from the past.
Submission history
From: Louis-Pierre Chaintron [view email][v1] Wed, 18 Mar 2026 18:07:02 UTC (228 KB)
Current browse context:
stat.ML
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
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
