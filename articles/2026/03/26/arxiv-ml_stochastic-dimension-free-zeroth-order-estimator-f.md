---
title: "Stochastic Dimension-Free Zeroth-Order Estimator for High-Dimensional and High-Order PINNs"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24002"
published: "2026-03-26"
fetched: "2026-03-27T07:19:37.341984"
---

Computer Science > Machine Learning
[Submitted on 25 Mar 2026]
Title:Stochastic Dimension-Free Zeroth-Order Estimator for High-Dimensional and High-Order PINNs
View PDF HTML (experimental)Abstract:Physics-Informed Neural Networks (PINNs) for high-dimensional and high-order partial differential equations (PDEs) are primarily constrained by the $\mathcal{O}(d^k)$ spatial derivative complexity and the $\mathcal{O}(P)$ memory overhead of backpropagation (BP). While randomized spatial estimators successfully reduce the spatial complexity to $\mathcal{O}(1)$, their reliance on first-order optimization still leads to prohibitive memory consumption at scale. Zeroth-order (ZO) optimization offers a BP-free alternative; however, naively combining randomized spatial operators with ZO perturbations triggers a variance explosion of $\mathcal{O}(1/\varepsilon^2)$, leading to numerical divergence. To address these challenges, we propose the \textbf{S}tochastic \textbf{D}imension-free \textbf{Z}eroth-order \textbf{E}stimator (\textbf{SDZE}), a unified framework that achieves dimension-independent complexity in both space and memory. Specifically, SDZE leverages \emph{Common Random Numbers Synchronization (CRNS)} to algebraically cancel the $\mathcal{O}(1/\varepsilon^2)$ variance by locking spatial random seeds across perturbations. Furthermore, an \emph{implicit matrix-free subspace projection} is introduced to reduce parameter exploration variance from $\mathcal{O}(P)$ to $\mathcal{O}(r)$ while maintaining an $\mathcal{O}(1)$ optimizer memory footprint. Empirical results demonstrate that SDZE enables the training of 10-million-dimensional PINNs on a single NVIDIA A100 GPU, delivering significant improvements in speed and memory efficiency over state-of-the-art baselines.
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
