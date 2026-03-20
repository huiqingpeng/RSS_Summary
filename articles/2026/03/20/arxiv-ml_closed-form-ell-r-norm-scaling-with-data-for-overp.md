---
title: "Closed-form $\ell_r$ norm scaling with data for overparameterized linear regression and diagonal linear networks under $\ell_p$ bias"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2509.21181"
published: "2026-03-20"
fetched: "2026-03-20T14:07:33.971829"
---

Computer Science > Machine Learning
[Submitted on 25 Sep 2025 (v1), last revised 19 Mar 2026 (this version, v4)]
Title:Closed-form $\ell_r$ norm scaling with data for overparameterized linear regression and diagonal linear networks under $\ell_p$ bias
View PDF HTML (experimental)Abstract:For overparameterized linear regression with isotropic Gaussian design and minimum-$\ell_p$ interpolator $p\in(1,2]$, we give a unified, high-probability characterization for the scaling of the family of parameter norms $ \\{ \lVert \widehat{w_p} \rVert_r \\}_{r \in [1,p]} $ with sample size. We solve this basic, but unresolved question through a simple dual-ray analysis, which reveals a competition between a signal *spike* and a *bulk* of null coordinates in $X^\top Y$, yielding closed-form predictions for (i) a data-dependent transition $n_\star$ (the "elbow"), and (ii) a universal threshold $r_\star=2(p-1)$ that separates $\lVert \widehat{w_p} \rVert_r$'s which plateau from those that continue to grow with an explicit exponent. This unified solution resolves the scaling of *all* $\ell_r$ norms within the family $r\in [1,p]$ under $\ell_p$-biased interpolation, and explains in one picture which norms saturate and which increase as $n$ grows. We then study diagonal linear networks (DLNs) trained by gradient descent. By calibrating the initialization scale $\alpha$ to an effective $p_{\mathrm{eff}}(\alpha)$ via the DLN separable potential, we show empirically that DLNs inherit the same elbow/threshold laws, providing a predictive bridge between explicit and implicit bias. Given that many generalization proxies depend on $\lVert \widehat {w_p} \rVert_r$, our results suggest that their predictive power will depend sensitively on which $l_r$ norm is used.
Submission history
From: Shuofeng Zhang [view email][v1] Thu, 25 Sep 2025 13:59:22 UTC (429 KB)
[v2] Wed, 8 Oct 2025 01:23:07 UTC (383 KB)
[v3] Mon, 8 Dec 2025 13:37:19 UTC (391 KB)
[v4] Thu, 19 Mar 2026 15:26:42 UTC (383 KB)
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
