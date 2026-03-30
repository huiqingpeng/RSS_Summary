---
title: "Interpretable long-term traffic modelling on national road networks using theory-informed deep learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26440"
published: "2026-03-30"
fetched: "2026-03-31T07:24:01.650469"
---

Computer Science > Machine Learning
[Submitted on 27 Mar 2026]
Title:Interpretable long-term traffic modelling on national road networks using theory-informed deep learning
View PDF HTML (experimental)Abstract:Long-term traffic modelling is fundamental to transport planning, but existing approaches often trade off interpretability, transferability, and predictive accuracy. Classical travel demand models provide behavioural structure but rely on strong assumptions and extensive calibration, whereas generic deep learning models capture complex patterns but often lack theoretical grounding and spatial transferability, limiting their usefulness for long-term planning applications. We propose DeepDemand, a theory-informed deep learning framework that embeds key components of travel demand theory to predict long-term highway traffic volumes using external socioeconomic features and road-network structure. The framework integrates a competitive two-source Dijkstra procedure for local origin-destination (OD) region extraction and OD pair screening with a differentiable architecture modelling OD interactions and travel-time deterrence. The model is evaluated using eight years (2017-2024) of observations on the UK strategic road network, covering 5088 highway segments. Under random cross-validation, DeepDemand achieves an R2 of 0.718 and an MAE of 7406 vehicles, outperforming linear, ridge, random forest, and gravity-style baselines. Performance remains strong under spatial cross-validation (R2 = 0.665), indicating good geographic transferability. Interpretability analysis reveals a stable nonlinear travel-time deterrence pattern, key socioeconomic drivers of demand, and polycentric OD interaction structures aligned with major employment centres and transport hubs. These results highlight the value of integrating transport theory with deep learning for interpretable highway traffic modelling and practical planning applications.
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
