---
title: "Dual Space Preconditioning for Gradient Descent in the Overparameterized Regime"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.10485"
published: "2026-03-19"
fetched: "2026-03-19T14:19:05.383476"
---

Statistics > Machine Learning
[Submitted on 11 Mar 2026 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:Dual Space Preconditioning for Gradient Descent in the Overparameterized Regime
View PDF HTML (experimental)Abstract:In this work we study the convergence properties of the Dual Space Preconditioned Gradient Descent, encompassing optimizers such as Normalized Gradient Descent, Gradient Clipping and Adam. We consider preconditioners of the form $\nabla K$, where $K: \mathbb{R}^p \to \mathbb{R}$ is convex and assume that the latter is applied to train an over-parameterized linear model with loss of the form $\ell({X} {W} - {Y})$, for weights ${W} \in \mathbb{R}^{d \times k}$, labels ${Y} \in \mathbb{R}^{n \times k}$ and data ${X} \in \mathbb{R}^{n \times d}$. Under the aforementioned assumptions, we prove that the iterates of the preconditioned gradient descent always converge to a point ${W}_{\infty} \in \mathbb{R}^{d \times k}$ satisfying ${X}{W}_{\infty} = {Y}$. Our proof techniques are of independent interest as we introduce a novel version of the Bregman Divergence with accompanying identities that allow us to establish convergence. We also study the implicit bias of Dual Space Preconditioned Gradient Descent. First, we demonstrate empirically that, for general $K(\cdot)$, ${W}_\infty$ depends on the chosen learning rate, hindering a precise characterization of the implicit bias. Then, for preconditioners of the form $K({G}) = h(\|{G}\|_F)$, known as \textit{isotropic preconditioners}, we show that ${W}_\infty$ minimizes $\|{W}_\infty - {W}_0\|_F^2$ subject to ${X}{W}_\infty = {Y}$, where ${W}_0$ is the initialization. Denoting the convergence point of GD initialized at ${W}_0$ by ${W}_{\text{GD}, \infty}$, we thus note ${W}_{\infty} = {W}_{\text{GD}, \infty}$ for isotropic preconditioners. Finally, we show that a similar fact holds for general preconditioners up to a multiplicative constant, namely, $\|{W}_0 - {W}_{\infty}\|_F \le c \|{W}_0 - {W}_{\text{GD}, \infty}\|_F$ for a constant $c>0$.
Submission history
From: Reza Ghane [view email][v1] Wed, 11 Mar 2026 07:19:52 UTC (217 KB)
[v2] Tue, 17 Mar 2026 21:55:00 UTC (217 KB)
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
