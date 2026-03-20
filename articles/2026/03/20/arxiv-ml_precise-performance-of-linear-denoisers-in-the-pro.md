---
title: "Precise Performance of Linear Denoisers in the Proportional Regime"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18483"
published: "2026-03-20"
fetched: "2026-03-20T13:13:31.546515"
---

Statistics > Machine Learning
[Submitted on 19 Mar 2026]
Title:Precise Performance of Linear Denoisers in the Proportional Regime
View PDFAbstract:In the present paper we study the performance of linear denoisers for noisy data of the form $\mathbf{x} + \mathbf{z}$, where $\mathbf{x} \in \mathbb{R}^d$ is the desired data with zero mean and unknown covariance $\mathbf{\Sigma}$, and $\mathbf{z} \sim \mathcal{N}(0, \mathbf{\Sigma}_{\mathbf{z}})$ is additive noise. Since the covariance $\mathbf{\Sigma}$ is not known, the standard Wiener filter cannot be employed for denoising. Instead we assume we are given samples $\mathbf{x}_1,\dots,\mathbf{x}_n \in \mathbb{R}^d$ from the true distribution. A standard approach would then be to estimate $\mathbf{\Sigma}$ from the samples and use it to construct an ``empirical" Wiener filter. However, in this paper, motivated by the denoising step in diffusion models, we take a different approach whereby we train a linear denoiser $\mathbf{W}$ from the data itself. In particular, we synthetically construct noisy samples $\hat{\mathbf{x}}_i$ of the data by injecting the samples with Gaussian noise with covariance $\mathbf{\Sigma}_1 \neq \mathbf{\Sigma}_{\mathbf{z}}$ and find the best $\mathbf{W}$ that approximates $\mathbf{W}\hat{\mathbf{x}}_i \approx \mathbf{x}_i$ in a least-squares sense. In the proportional regime $\frac{n}{d} \rightarrow \kappa > 1$ we use the {\it Convex Gaussian Min-Max Theorem (CGMT)} to analytically find the closed form expression for the generalization error of the denoiser obtained from this process. Using this expression one can optimize over $\mathbf{\Sigma}_1$ to find the best possible denoiser. Our numerical simulations show that our denoiser outperforms the ``empirical" Wiener filter in many scenarios and approaches the optimal Wiener filter as $\kappa\rightarrow\infty$.
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
