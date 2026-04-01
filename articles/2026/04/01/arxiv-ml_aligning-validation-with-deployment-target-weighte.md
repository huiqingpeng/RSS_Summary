---
title: "Aligning Validation with Deployment: Target-Weighted Cross-Validation for Spatial Prediction"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.29981"
published: "2026-04-01"
fetched: "2026-04-02T07:21:38.512532"
---

Computer Science > Machine Learning
[Submitted on 31 Mar 2026]
Title:Aligning Validation with Deployment: Target-Weighted Cross-Validation for Spatial Prediction
View PDF HTML (experimental)Abstract:Cross-validation (CV) is commonly used to estimate predictive risk when independent test data are unavailable. Its validity depends on the assumption that validation tasks are sampled from the same distribution as prediction tasks encountered during deployment. In spatial prediction and other settings with structured data, this assumption is frequently violated, leading to biased estimates of deployment risk. We propose Target-Weighted CV (TWCV), an estimator of deployment risk that accounts for discrepancies between validation and deployment task distributions, thus accounting for (1) covariate shift and (2) task-difficulty shift. We characterize prediction tasks by descriptors such as covariates and spatial configuration. TWCV assigns weights to validation losses such that the weighted empirical distribution of validation tasks matches the corresponding distribution over a target domain. The weights are obtained via calibration weighting, yielding an importance-weighted estimator that targets deployment risk. Since TWCV requires adequate coverage of the deployment distribution's support, we combine it with spatially buffered resampling that diversifies the task difficulty distribution. In a simulation study, conventional as well as spatial estimators exhibit substantial bias depending on sampling, whereas buffered TWCV remains approximately unbiased across scenarios. A case study in environmental pollution mapping further confirms that discrepancies between validation and deployment task distributions can affect performance assessment, and that buffered TWCV better reflects the prediction task over the target domain. These results establish task distribution mismatch as a primary source of CV bias in spatial prediction and show that calibration weighting combined with a suitable validation task generator provides a viable approach to estimating predictive risk under dataset shift.
Submission history
From: Alexander Brenning [view email][v1] Tue, 31 Mar 2026 16:44:07 UTC (4,590 KB)
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
