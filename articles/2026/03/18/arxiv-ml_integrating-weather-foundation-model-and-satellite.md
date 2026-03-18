---
title: "Integrating Weather Foundation Model and Satellite to Enable Fine-Grained Solar Irradiance Forecasting"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.14845"
published: "2026-03-18"
fetched: "2026-03-18T17:07:17.506579"
---

Computer Science > Machine Learning
[Submitted on 16 Mar 2026 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:Integrating Weather Foundation Model and Satellite to Enable Fine-Grained Solar Irradiance Forecasting
View PDF HTML (experimental)Abstract:Accurate day-ahead solar irradiance forecasting is essential for integrating solar energy into the power grid. However, it remains challenging due to the pronounced diurnal cycle and inherently complex cloud dynamics. Current methods either lack fine-scale resolution (e.g., numerical weather prediction, weather foundation models) or degrade at longer lead times (e.g., satellite extrapolation). We propose Baguan-solar, a two-stage multimodal framework that fuses forecasts from Baguan, a global weather foundation model, with high-resolution geostationary satellite imagery to produce 24- hour irradiance forecasts at kilometer scale. Its decoupled two-stage design first forecasts day-night continuous intermediates (e.g., cloud cover) and then infers irradiance, while its modality fusion jointly preserves fine-scale cloud structures from satellite and large-scale constraints from Baguan forecasts. Evaluated over East Asia using CLDAS as ground truth, Baguan-solar outperforms strong baselines (including ECMWF IFS, vanilla Baguan, and SolarSeer), reducing RMSE by 16.08% and better resolving cloud-induced transients. An operational deployment of Baguan-solar has supported solar power forecasting in an eastern province in China, since July 2025. Our code is accessible at this https URL. git.
Submission history
From: Ziqing Ma [view email][v1] Mon, 16 Mar 2026 05:44:56 UTC (7,957 KB)
[v2] Tue, 17 Mar 2026 07:11:02 UTC (4,028 KB)
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
