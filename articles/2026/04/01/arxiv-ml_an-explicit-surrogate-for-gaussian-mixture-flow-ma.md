---
title: "An Explicit Surrogate for Gaussian Mixture Flow Matching with Wasserstein Gap Bounds"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.28992"
published: "2026-04-01"
fetched: "2026-04-02T07:14:13.962492"
---

Computer Science > Machine Learning
[Submitted on 30 Mar 2026]
Title:An Explicit Surrogate for Gaussian Mixture Flow Matching with Wasserstein Gap Bounds
View PDF HTML (experimental)Abstract:We study training-free flow matching between two Gaussian mixture models (GMMs) using explicit velocity fields that transport one mixture into the other over time. Our baseline approach constructs component-wise Gaussian paths with affine velocity fields satisfying the continuity equation, which yields to a closed-form surrogate for the pairwise kinetic transport cost. In contrast to the exact Gaussian Wasserstein cost, which relies on matrix square-root computations, the surrogate admits a simple analytic expression derived from the kinetic energy of the induced flow. We then analyze how closely this surrogate approximates the exact cost. We prove second-order agreement in a local commuting regime and derive an explicit cubic error bound in the local commuting regime. To handle nonlocal regimes, we introduce a path-splitting strategy that localizes the covariance evolution and enables piecewise application of the bound. We finally compare the surrogate with an exact construction based on the Gaussian Wasserstein geodesic and summarize the results in a practical regime map showing when the surrogate is accurate and the exact method is preferable.
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
