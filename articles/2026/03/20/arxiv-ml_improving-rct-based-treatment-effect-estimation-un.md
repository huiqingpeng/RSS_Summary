---
title: "Improving RCT-Based Treatment Effect Estimation Under Covariate Mismatch via Calibrated Alignment"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19186"
published: "2026-03-20"
fetched: "2026-03-20T13:06:36.256608"
---

Computer Science > Machine Learning
[Submitted on 19 Mar 2026]
Title:Improving RCT-Based Treatment Effect Estimation Under Covariate Mismatch via Calibrated Alignment
View PDF HTML (experimental)Abstract:Randomized controlled trials (RCTs) are the gold standard for estimating heterogeneous treatment effects, yet they are often underpowered for detecting effect heterogeneity. Large observational studies (OS) can supplement RCTs for conditional average treatment effect (CATE) estimation, but a key barrier is covariate mismatch: the two sources measure different, only partially overlapping, covariates. We propose CALM (Calibrated ALignment under covariate Mismatch), which bypasses imputation by learning embeddings that map each source's features into a common representation space. OS outcome models are transferred to the RCT embedding space and calibrated using trial data, preserving causal identification from randomization. Finite-sample risk bounds decompose into alignment error, outcome-model complexity, and calibration complexity terms, identifying when embedding alignment outperforms imputation. Under the calibration-based linear variant, the framework provides protection against negative transfer; the neural variant can be vulnerable under severe distributional shift. Under sparse linear models, the embedding approach strictly generalizes imputation. Simulations across 51 settings confirm that (i) calibration-based methods are equivalent for linear CATEs, and (ii) the neural embedding variant wins all 22 nonlinear-regime settings with large margins.
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
