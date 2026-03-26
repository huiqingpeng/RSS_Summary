---
title: "Manifold Generalization Provably Proceeds Memorization in Diffusion Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23792"
published: "2026-03-26"
fetched: "2026-03-27T07:17:08.524841"
---

Computer Science > Machine Learning
[Submitted on 24 Mar 2026]
Title:Manifold Generalization Provably Proceeds Memorization in Diffusion Models
View PDF HTML (experimental)Abstract:Diffusion models often generate novel samples even when the learned score is only \emph{coarse} -- a phenomenon not accounted for by the standard view of diffusion training as density estimation. In this paper, we show that, under the \emph{manifold hypothesis}, this behavior can instead be explained by coarse scores capturing the \emph{geometry} of the data while discarding the fine-scale distributional structure of the population measure~$\mu_{\scriptscriptstyle\mathrm{data}}$. Concretely, whereas estimating the full data distribution $\mu_{\scriptscriptstyle\mathrm{data}}$ supported on a $k$-dimensional manifold is known to require the classical minimax rate $\tilde{\mathcal{O}}(N^{-1/k})$, we prove that diffusion models trained with coarse scores can exploit the \emph{regularity of the manifold support} and attain a near-parametric rate toward a \emph{different} target distribution. This target distribution has density uniformly comparable to that of~$\mu_{\scriptscriptstyle\mathrm{data}}$ throughout any $\tilde{\mathcal{O}}\bigl(N^{-\beta/(4k)}\bigr)$-neighborhood of the manifold, where $\beta$ denotes the manifold regularity. Our guarantees therefore depend only on the smoothness of the underlying support, and are especially favorable when the data density itself is irregular, for instance non-differentiable. In particular, when the manifold is sufficiently smooth, we obtain that \emph{generalization} -- formalized as the ability to generate novel, high-fidelity samples -- occurs at a statistical rate strictly faster than that required to estimate the full population distribution~$\mu_{\scriptscriptstyle\mathrm{data}}$.
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
