---
title: "Problems with Chinchilla Approach 2: Systematic Biases in IsoFLOP Parabola Fits"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22339"
published: "2026-03-25"
fetched: "2026-03-26T07:12:36.439396"
---

Computer Science > Machine Learning
[Submitted on 21 Mar 2026]
Title:Problems with Chinchilla Approach 2: Systematic Biases in IsoFLOP Parabola Fits
View PDF HTML (experimental)Abstract:Chinchilla Approach 2 is among the most widely used methods for fitting neural scaling laws. Its parabolic approximation introduces systematic biases in compute-optimal allocation estimates, even on noise-free synthetic data. Applied to published Llama 3 IsoFLOP data at open frontier compute scales, these biases imply a parameter underallocation corresponding to 6.5% of the $3.8\times10^{25}$ FLOP training budget and \$1.4M (90% CI: \$412K-\$2.9M) in unnecessary compute at 50% H100 MFU. Simulated multimodal model misallocations show even greater opportunity costs due to higher loss surface asymmetry. Three sources of this error are examined: IsoFLOP sampling grid width (Taylor approximation accuracy), uncentered IsoFLOP sampling, and loss surface asymmetry ($\alpha \neq \beta$). Chinchilla Approach 3 largely eliminates these biases but is often regarded as less data-efficient, numerically unstable, prone to local minima, and harder to implement. Each concern is shown to be unfounded or addressable, especially when the partially linear structure of the objective is exploited via Variable Projection, enabling unbiased inference on all five loss surface parameters through a two-dimensional optimization that is well-conditioned, analytically differentiable, and amenable to dense, or even exhaustive, grid search. It may serve as a more convenient replacement for Approach 2 or a more scalable alternative for adaptations of Approach 3 to richer scaling law formulations.
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
