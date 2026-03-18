---
title: "Long-Horizon Traffic Forecasting via Incident-Aware Conformal Spatio-Temporal Transformers"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16857"
published: "2026-03-18"
fetched: "2026-03-18T16:04:21.128047"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:Long-Horizon Traffic Forecasting via Incident-Aware Conformal Spatio-Temporal Transformers
View PDF HTML (experimental)Abstract:Reliable multi-horizon traffic forecasting is challenging because network conditions are stochastic, incident disruptions are intermittent, and effective spatial dependencies vary across time-of-day patterns. This study is conducted on the Ohio Department of Transportation (ODOT) traffic count data and corresponding ODOT crash records. This work utilizes a Spatio-Temporal Transformer (STT) model with Adaptive Conformal Prediction (ACP) to produce multi-horizon forecasts with calibrated uncertainty. We propose a piecewise Coefficient of Variation (CV) strategy that models hour-to-hour traveltime variability using a log-normal distribution, enabling the construction of a per-hour dynamic adjacency matrix. We further perturb edge weights using incident-related severity signals derived from the ODOT crash dataset that comprises incident clearance time, weather conditions, speed violations, work zones, and roadway functional class, to capture localized disruptions and peak/off-peak transitions. This dynamic graph construction replaces a fixed-CV assumption and better represents changing traffic conditions within the forecast window. For validation, we generate extended trips via multi-hour loop runs on the Columbus, Ohio, network in SUMO simulations and apply a Monte Carlo simulation to obtain travel-time distributions for a Vehicle Under Test (VUT). Experiments demonstrate improved long-horizon accuracy and well-calibrated prediction intervals compared to other baseline methods.
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
