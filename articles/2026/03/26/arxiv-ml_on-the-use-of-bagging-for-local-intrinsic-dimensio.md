---
title: "On the Use of Bagging for Local Intrinsic Dimensionality Estimation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24384"
published: "2026-03-26"
fetched: "2026-03-27T07:23:13.755949"
---

Computer Science > Machine Learning
[Submitted on 25 Mar 2026]
Title:On the Use of Bagging for Local Intrinsic Dimensionality Estimation
View PDF HTML (experimental)Abstract:The theory of Local Intrinsic Dimensionality (LID) has become a valuable tool for characterizing local complexity within and across data manifolds, supporting a range of data mining and machine learning tasks. Accurate LID estimation requires samples drawn from small neighborhoods around each query to avoid biases from nonlocal effects and potential manifold mixing, yet limited data within such neighborhoods tends to cause high estimation variance. As a variance reduction strategy, we propose an ensemble approach that uses subbagging to preserve the local distribution of nearest neighbor (NN) distances. The main challenge is that the uniform reduction in total sample size within each subsample increases the proximity threshold for finding a fixed number k of NNs around the query. As a result, in the specific context of LID estimation, the sampling rate has an additional, complex interplay with the neighborhood size, where both combined determine the sample size as well as the locality and resolution considered for estimation. We analyze both theoretically and experimentally how the choice of the sampling rate and the k-NN size used for LID estimation, alongside the ensemble size, affects performance, enabling informed prior selection of these hyper-parameters depending on application-based preferences. Our results indicate that within broad and well-characterized regions of the hyper-parameters space, using a bagged estimator will most often significantly reduce variance as well as the mean squared error when compared to the corresponding non-bagged baseline, with controllable impact on bias. We additionally propose and evaluate different ways of combining bagging with neighborhood smoothing for substantial further improvements on LID estimation performance.
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
