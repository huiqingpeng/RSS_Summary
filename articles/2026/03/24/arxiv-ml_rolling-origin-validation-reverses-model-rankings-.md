---
title: "Rolling-Origin Validation Reverses Model Rankings in Multi-Step PM10 Forecasting: XGBoost, SARIMA, and Persistence"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20315"
published: "2026-03-24"
fetched: "2026-03-25T07:07:24.876667"
---

Computer Science > Machine Learning
[Submitted on 19 Mar 2026]
Title:Rolling-Origin Validation Reverses Model Rankings in Multi-Step PM10 Forecasting: XGBoost, SARIMA, and Persistence
View PDF HTML (experimental)Abstract:(a) Many air quality forecasting studies report gains from machine learning, but evaluations often use static chronological splits and omit persistence baselines, so the operational added value under routine updating is unclear.
(b) Using 2,350 daily PM10 observations from 2017 to 2024 at an urban background monitoring station in southern Europe, we compare XGBoost and SARIMA against persistence under a static split and a rolling-origin protocol with monthly updates. We report horizon-specific skill and the predictability horizon, defined as the maximum horizon with positive persistence-relative skill. Static evaluation suggests XGBoost performs well from one to seven days ahead, but rolling-origin evaluation reverses rankings: XGBoost is not consistently better than persistence at short and intermediate horizons, whereas SARIMA remains positively skilled across the full range.
(c) For researchers, static splits can overstate operational usefulness and change rankings. For practitioners, rolling-origin, persistence-referenced skill profiles show which methods stay reliable at each lead time.
Submission history
From: Francisco Federico Garcia Crespi FGCrespi [view email][v1] Thu, 19 Mar 2026 19:08:38 UTC (1,067 KB)
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
