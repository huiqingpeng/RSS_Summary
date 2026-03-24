---
title: "RMNP: Row-Momentum Normalized Preconditioning for Scalable Matrix-Based Optimization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20527"
published: "2026-03-24"
fetched: "2026-03-25T07:11:10.542785"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:RMNP: Row-Momentum Normalized Preconditioning for Scalable Matrix-Based Optimization
View PDF HTML (experimental)Abstract:Preconditioned adaptive methods have gained significant attention for training deep neural networks, as they capture rich curvature information of the loss landscape . The central challenge in this field lies in balancing preconditioning effectiveness with computational efficiency of implementing the preconditioner. Among recent advances, \textsc{Muon} stands out by using Newton-Schulz iteration to obtain preconditioned updates without explicitly constructing the preconditioning matrix. Despite its advantages, the efficiency of \textsc{Muon} still leaves room for further improvement. In this paper, we introduce \textsc{RMNP} (Row Momentum Normalized Preconditioning), an optimizer that replaces Newton-Schulz iteration with a simple row-wise $\ell_2$ normalization operation, motivated by the empirically observed diagonal block structure of the Transformer layerwise Hessian. This substitution reduces the per-iteration computational complexity from $\mathcal{O}(mn\cdot\min(m,n))$ to $\mathcal{O}(mn)$ for an $m\times n$ weight matrix while maintaining comparable optimization performance. Theoretically, we establish convergence guarantees for \textsc{RMNP} in the non-convex setting that match recent results for \textsc{Muon} optimizers, achieving the information-theoretic minimax optimal complexity. Extensive experiments on large language model pretraining show that \textsc{RMNP} delivers competitive optimization performance compared with \textsc{Muon} while substantially reducing preconditioning wall-clock time. Our code is available at \href{this https URL}{this link}.
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
