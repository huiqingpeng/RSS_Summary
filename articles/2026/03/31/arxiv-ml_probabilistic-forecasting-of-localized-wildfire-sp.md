---
title: "Probabilistic Forecasting of Localized Wildfire Spread Based on Conditional Flow Matching"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26975"
published: "2026-03-31"
fetched: "2026-04-01T07:20:47.201202"
---

Computer Science > Machine Learning
[Submitted on 27 Mar 2026]
Title:Probabilistic Forecasting of Localized Wildfire Spread Based on Conditional Flow Matching
View PDF HTML (experimental)Abstract:This study presents a probabilistic surrogate model for localized wildfire spread based on a conditional flow matching algorithm. The approach models fire progression as a stochastic process by learning the conditional distribution of fire arrival times given the current fire state along with environmental and atmospheric inputs. Model inputs include current burned area, near-surface wind components, temperature, relative humidity, terrain height, and fuel category information, all defined on a high-resolution spatial grid. The outputs are samples of arrival time within a three-hour time window, conditioned on the input variables. Training data are generated from coupled atmosphere-wildfire spread simulations using WRF-SFIRE, paired with weather fields from the North American Mesoscale model. The proposed framework enables efficient generation of ensembles of arrival times and explicitly represents uncertainty arising from incomplete knowledge of the fire-atmosphere system and unresolved variables. The model supports localized prediction over subdomains, reducing computational cost relative to physics-based simulators while retaining sensitivity to key drivers of fire spread. Model performance is evaluated against WRF-SFIRE simulations for both single-step (3-hour) and recursive multi-step (24-hour) forecasts. Results demonstrate that the method captures variability in fire evolution and produces accurate ensemble predictions. The framework provides a scalable approach for probabilistic wildfire forecasting and offers a pathway for integrating machine learning models with operational fire prediction systems and data assimilation.
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
