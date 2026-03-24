---
title: "Exponential Family Discriminant Analysis: Generalizing LDA-Style Generative Classification to Non-Gaussian Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20655"
published: "2026-03-24"
fetched: "2026-03-25T07:12:54.496419"
---

Computer Science > Machine Learning
[Submitted on 21 Mar 2026]
Title:Exponential Family Discriminant Analysis: Generalizing LDA-Style Generative Classification to Non-Gaussian Models
View PDF HTML (experimental)Abstract:We introduce Exponential Family Discriminant Analysis (EFDA), a unified generative framework that extends classical Linear Discriminant Analysis (LDA) beyond the Gaussian setting to any member of the exponential family. Under the assumption that each class-conditional density belongs to a common exponential family, EFDA derives closed-form maximum-likelihood estimators for all natural parameters and yields a decision rule that is linear in the sufficient statistic, recovering LDA as a special case and capturing nonlinear decision boundaries in the original feature space. We prove that EFDA is asymptotically calibrated and statistically efficient under correct specification, and we generalise it to $K \geq 2$ classes and multivariate data. Through extensive simulation across five exponential-family distributions (Weibull, Gamma, Exponential, Poisson, Negative Binomial), EFDA matches the classification accuracy of LDA, QDA, and logistic regression while reducing Expected Calibration Error (ECE) by $2$--$6\times$, a gap that is \emph{structural}: it persists for all $n$ and across all class-imbalance levels, because misspecified models remain asymptotically miscalibrated. We further prove and empirically confirm that EFDA's log-odds estimator approaches the Cramér-Rao bound under correct specification, and is the only estimator in our comparison whose mean squared error converges to zero. Complete derivations are provided for nine distributions. Finally, we formally verify all four theoretical propositions in Lean 4, using Aristotle (Harmonic) and OpenGauss (Math, Inc.) as proof generators, with all outputs independently machine-checked by AXLE (Axiom).
Submission history
From: Anish Lakkapragada [view email][v1] Sat, 21 Mar 2026 05:24:56 UTC (366 KB)
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
