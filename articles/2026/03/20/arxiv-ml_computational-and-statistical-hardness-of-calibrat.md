---
title: "Computational and Statistical Hardness of Calibration Distance"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18391"
published: "2026-03-20"
fetched: "2026-03-20T13:12:13.939211"
---

Computer Science > Data Structures and Algorithms
[Submitted on 19 Mar 2026]
Title:Computational and Statistical Hardness of Calibration Distance
View PDF HTML (experimental)Abstract:The distance from calibration, introduced by Błasiok, Gopalan, Hu, and Nakkiran (STOC 2023), has recently emerged as a central measure of miscalibration for probabilistic predictors. We study the fundamental problems of computing and estimating this quantity, given either an exact description of the data distribution or only sample access to it.
We give an efficient algorithm that exactly computes the calibration distance when the distribution has a uniform marginal and noiseless labels, which improves the $O(1/\sqrt{|\mathcal{X}|})$ additive approximation of Qiao and Zheng (COLT 2024) for this special case. Perhaps surprisingly, the problem becomes $\mathsf{NP}$-hard when either of the two assumptions is removed. We extend our algorithm to a polynomial-time approximation scheme for the general case.
For the estimation problem, we show that $\Theta(1/\epsilon^3)$ samples are sufficient and necessary for the empirical calibration distance to be upper bounded by the true distance plus $\epsilon$. In contrast, a polynomial dependence on the domain size -- incurred by the learning-based baseline -- is unavoidable for two-sided estimation.
Our positive results are based on simple sparsifications of both the distribution and the target predictor, which significantly reduce the search space for computation and lead to stronger concentration for the estimation problem. To prove the hardness results, we introduce new techniques for certifying lower bounds on the calibration distance -- a problem that is hard in general due to its $\textsf{co-NP}$-completeness.
Current browse context:
cs.DS
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
