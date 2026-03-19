---
title: "Interpretable AI-Assisted Early Reliability Prediction for a Two-Parameter Parallel Root-Finding Scheme"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16980"
published: "2026-03-19"
fetched: "2026-03-19T13:08:00.479292"
---

Mathematics > Numerical Analysis
[Submitted on 17 Mar 2026]
Title:Interpretable AI-Assisted Early Reliability Prediction for a Two-Parameter Parallel Root-Finding Scheme
View PDF HTML (experimental)Abstract:We propose an interpretable AI-assisted reliability diagnostic framework for parameterized root-finding schemes based on kNN-LLE proxy stability profiling and multi-horizon early prediction. The approach augments a numerical solver with a lightweight predictive layer that estimates solver reliability from short prefixes of iteration dynamics, enabling early identification of stable and unstable parameter regimes. For each configuration in the parameter space, raw and smoothed proxy profiles of a largest Lyapunov exponent (LLE) estimator are constructed, from which contractivity-based reliability scores summarizing finite-time convergence are derived. Machine learning models predict the reliability score from early segments of the proxy profile, allowing the framework to determine when solver dynamics become diagnostically informative. Experiments on a two-parameter parallel root-finding scheme show reliable prediction after only a few iterations: the best models achieve R^2=0.48 at horizon T=1, improve to R^2=0.67 by T=3, and exceed R^2=0.89 before the characteristic minimum-location scale of the stability profile. Prediction accuracy increases to R^2=0.96 at larger horizons, with mean absolute errors around 0.03, while inference costs remain negligible (microseconds per sample). The framework provides interpretable stability indicators and supports early decisions during solver execution, such as continuing, restarting, or adjusting parameters.
Current browse context:
math.NA
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
