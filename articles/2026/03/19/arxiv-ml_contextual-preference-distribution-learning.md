---
title: "Contextual Preference Distribution Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17139"
published: "2026-03-19"
fetched: "2026-03-19T12:07:47.616427"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:Contextual Preference Distribution Learning
View PDF HTML (experimental)Abstract:Decision-making problems often feature uncertainty stemming from heterogeneous and context-dependent human preferences. To address this, we propose a sequential learning-and-optimization pipeline to learn preference distributions and leverage them to solve downstream problems, for example risk-averse formulations. We focus on human choice settings that can be formulated as (integer) linear programs. In such settings, existing inverse optimization and choice modelling methods infer preferences from observed choices but typically produce point estimates or fail to capture contextual shifts, making them unsuitable for risk-averse decision-making. Using a bounded-variance score function gradient estimator, we train a predictive model mapping contextual features to a rich class of parameterizable distributions. This approach yields a maximum likelihood estimate. The model generates scenarios for unseen contexts in the subsequent optimization phase. In a synthetic ridesharing environment, our approach reduces average post-decision surprise by up to 114$\times$ compared to a risk-neutral approach with perfect predictions and up to 25$\times$ compared to leading risk-averse baselines.
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
