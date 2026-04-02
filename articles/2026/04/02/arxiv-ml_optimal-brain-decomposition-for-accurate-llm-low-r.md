---
title: "Optimal Brain Decomposition for Accurate LLM Low-Rank Approximation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00821"
published: "2026-04-02"
fetched: "2026-04-03T07:25:18.948722"
---

Computer Science > Machine Learning
[Submitted on 1 Apr 2026]
Title:Optimal Brain Decomposition for Accurate LLM Low-Rank Approximation
View PDF HTML (experimental)Abstract:Low-rank decomposition has emerged as an important problem in Large Language Model (LLM) fine-tuning and inference. Through Singular Value Decomposition (SVD), the weight matrix can be factorized into low-rank spaces optimally. Previously, a common practice was to decompose the weight in the activation-whitened space, and then achieve satisfying results. In this work, we propose Optimal Brain Decomposition LLM (OBD-LLM), which studies the decomposition problem in the model space by utilizing second-order Hessian information. Through a rigorous Kronecker-factorization of the Hessian, we show that the decomposition needs to consider both input and output information of the layer, and achieves much better decomposition results compared to input only method. Our loss-aware decomposition method involves a bi-directional whitening on the weight matrix. As a result, OBD-LLM is a closed-form solution for the optimal decomposition of weights in the language model. Remarkably, we achieve ~20-40\% better results than previous state-of-the-art decomposition methods, the SVD-LLM.
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
