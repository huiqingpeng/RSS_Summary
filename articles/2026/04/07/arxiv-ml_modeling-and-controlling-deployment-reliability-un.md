---
title: "Modeling and Controlling Deployment Reliability under Temporal Distribution Shift"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.02351"
published: "2026-04-07"
fetched: "2026-04-08T07:02:36.213149"
---

Computer Science > Machine Learning
[Submitted on 1 Mar 2026]
Title:Modeling and Controlling Deployment Reliability under Temporal Distribution Shift
View PDF HTML (experimental)Abstract:Machine learning models deployed in non-stationary environments are exposed to temporal distribution shift, which can erode predictive reliability over time. While common mitigation strategies such as periodic retraining and recalibration aim to preserve performance, they typically focus on average metrics evaluated at isolated time points and do not explicitly model how reliability evolves during deployment.
We propose a deployment-centric framework that treats reliability as a dynamic state composed of discrimination and calibration. The trajectory of this state across sequential evaluation windows induces a measurable notion of volatility, allowing deployment adaptation to be formulated as a multi-objective control problem that balances reliability stability against cumulative intervention cost.
Within this framework, we define a family of state-dependent intervention policies and empirically characterize the resulting cost-volatility Pareto frontier. Experiments on a large-scale, temporally indexed credit-risk dataset (1.35M loans, 2007-2018) show that selective, drift-triggered interventions can achieve smoother reliability trajectories than continuous rolling retraining while substantially reducing operational cost.
These findings position deployment reliability under temporal shift as a controllable multi-objective system and highlight the role of policy design in shaping stability-cost trade-offs in high-stakes tabular applications.
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
