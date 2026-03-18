---
title: "The Importance of Being Smoothly Calibrated"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16015"
published: "2026-03-18"
fetched: "2026-03-18T15:39:15.559788"
---

Computer Science > Machine Learning
[Submitted on 16 Mar 2026]
Title:The Importance of Being Smoothly Calibrated
View PDF HTML (experimental)Abstract:Recent work has highlighted the centrality of smooth calibration [Kakade and Foster, 2008] as a robust measure of calibration error. We generalize, unify, and extend previous results on smooth calibration, both as a robust calibration measure, and as a step towards omniprediction, which enables predictions with low regret for downstream decision makers seeking to optimize some proper loss unknown to the predictor.
We present a new omniprediction guarantee for smoothly calibrated predictors, for the class of all bounded proper losses. We smooth the predictor by adding some noise to it, and compete against smoothed versions of any benchmark predictor on the space, where we add some noise to the predictor and then post-process it arbitrarily. The omniprediction error is bounded by the smooth calibration error of the predictor and the earth mover's distance from the benchmark. We exhibit instances showing that this dependence cannot, in general, be improved. We show how this unifies and extends prior results [Foster and Vohra, 1998; Hartline, Wu, and Yang, 2025] on omniprediction from smooth calibration.
We present a crisp new characterization of smooth calibration in terms of the earth mover's distance to the closest perfectly calibrated joint distribution of predictions and labels. This also yields a simpler proof of the relation to the lower distance to calibration from [Blasiok, Gopalan, Hu, and Nakkiran, 2023].
We use this to show that the upper distance to calibration cannot be estimated within a quadratic factor with sample complexity independent of the support size of the predictions. This is in contrast to the distance to calibration, where the corresponding problem was known to be information-theoretically impossible: no finite number of samples suffice [Blasiok, Gopalan, Hu, and Nakkiran, 2023].
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
