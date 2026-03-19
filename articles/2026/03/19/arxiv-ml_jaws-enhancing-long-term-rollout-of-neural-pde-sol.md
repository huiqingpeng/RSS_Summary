---
title: "JAWS: Enhancing Long-term Rollout of Neural PDE Solvers via Spatially-Adaptive Jacobian Regularization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.05538"
published: "2026-03-19"
fetched: "2026-03-19T14:13:07.946250"
---

Computer Science > Machine Learning
[Submitted on 4 Mar 2026 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:JAWS: Enhancing Long-term Rollout of Neural PDE Solvers via Spatially-Adaptive Jacobian Regularization
View PDF HTML (experimental)Abstract:Data-driven surrogate models can significantly accelerate the simulation of continuous dynamical systems, yet the step-wise accumulation of errors during autoregressive time-stepping often leads to spectral blow-up and unphysical divergence. Existing global regularization techniques can enforce contractive dynamics but uniformly damp high-frequency features, causing over-smoothing; meanwhile, long-horizon trajectory optimization methods are severely constrained by memory bottlenecks. This paper proposes Jacobian-Adaptive Weighting for Stability (JAWS), which reformulates operator learning as a Maximum A Posteriori (MAP) estimation problem with spatially heteroscedastic uncertainty, enabling the regularization strength to adapt automatically based on local physical complexity: enforcing contraction in smooth regions to suppress noise while relaxing constraints near singular features such as shocks to preserve gradient information. Experiments demonstrate that JAWS serves as an effective spectral pre-conditioner for trajectory optimization, allowing short-horizon, memory-efficient training to match the accuracy of long-horizon baselines. Validations on the 1D viscous Burgers' equation and 2D flow past a cylinder (Re=400 out-of-distribution generalization) confirm the method's advantages in long-term stability, preservation of physical conservation properties, and computational efficiency. This significant reduction in memory usage makes the method particularly well-suited for stable and efficient long-term simulation of large-scale flow fields in practical engineering applications. Our source code and implementation are publicly available at this https URL.
Submission history
From: Hosyo Jyo [view email][v1] Wed, 4 Mar 2026 06:15:09 UTC (337 KB)
[v2] Wed, 18 Mar 2026 16:03:44 UTC (910 KB)
Current browse context:
cs.LG
Change to browse by:
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
