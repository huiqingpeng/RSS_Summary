---
title: "Cloud-Edge Collaborative Large Models for Robust Photovoltaic Power Forecasting"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22343"
published: "2026-03-25"
fetched: "2026-03-26T07:12:46.921742"
---

Computer Science > Machine Learning
[Submitted on 21 Mar 2026]
Title:Cloud-Edge Collaborative Large Models for Robust Photovoltaic Power Forecasting
View PDF HTML (experimental)Abstract:Photovoltaic (PV) power forecasting in edge-enabled grids requires balancing forecasting accuracy, robustness under weather-driven distribution shifts, and strict latency constraints. Local specialized models are efficient for routine conditions but often degrade under rare ramp events and unseen weather patterns, whereas always relying on cloud-side large models incurs substantial communication delay and cloud overhead. To address this challenge, we propose a risk-aware cloud-edge collaborative framework for latency-sensitive PV forecasting. The framework integrates a site-specific expert predictor for routine cases, a lightweight edge-side model for enhanced local inference, and a cloud-side large retrieval model that provides matched historical context when needed through a retrieval-prediction pipeline. A lightweight screening module estimates predictive uncertainty, out-of-distribution risk, weather mutation intensity, and model disagreement, while a Lyapunov-guided router selectively escalates inference to the edge-small or cloud-assisted branches under long-term latency, communication, and cloud-usage constraints. The outputs of the activated branches are combined through adaptive fusion. Experiments on two real-world PV datasets demonstrate a favorable overall trade-off among forecasting accuracy, routing quality, robustness, and system efficiency.
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
