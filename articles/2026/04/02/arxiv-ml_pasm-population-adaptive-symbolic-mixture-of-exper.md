---
title: "PASM: Population Adaptive Symbolic Mixture-of-Experts Model for Cross-location Hurricane Evacuation Decision Prediction"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00074"
published: "2026-04-02"
fetched: "2026-04-03T07:17:00.602967"
---

Computer Science > Machine Learning
[Submitted on 31 Mar 2026]
Title:PASM: Population Adaptive Symbolic Mixture-of-Experts Model for Cross-location Hurricane Evacuation Decision Prediction
View PDF HTML (experimental)Abstract:Accurate prediction of evacuation behavior is critical for disaster preparedness, yet models trained in one region often fail elsewhere. Using a multi-state hurricane evacuation survey, we show this failure goes beyond feature distribution shift: households with similar characteristics follow systematically different decision patterns across states. As a result, single global models overfit dominant responses, misrepresent vulnerable subpopulations, and generalize poorly across locations. We propose Population-Adaptive Symbolic Mixture-of-Experts (PASM), which pairs large language model guided symbolic regression with a mixture-of-experts architecture. PASM discovers human-readable closed-form decision rules, specializes them to data-driven subpopulations, and routes each input to the appropriate expert at inference time. On Hurricanes Harvey and Irma data, transferring from Florida and Texas to Georgia with 100 calibration samples, PASM achieves a Matthews correlation coefficient of 0.607, compared to XGBoost (0.404), TabPFN (0.333), GPT-5-mini (0.434), and meta-learning baselines MAML and Prototypical Networks (MCC $\leq$ 0.346). The routing mechanism assigns distinct formula archetypes to subpopulations, so the resulting behavioral profiles are directly interpretable. A fairness audit across four demographic axes finds no statistically significant disparities after Bonferroni correction. PASM closes more than half the cross-location generalization gap while keeping decision rules transparent enough for real-world emergency planning.
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
