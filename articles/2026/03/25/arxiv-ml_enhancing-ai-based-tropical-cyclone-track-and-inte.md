---
title: "Enhancing AI-Based Tropical Cyclone Track and Intensity Forecasting via Systematic Bias Correction"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22314"
published: "2026-03-25"
fetched: "2026-03-26T07:09:51.769296"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:Enhancing AI-Based Tropical Cyclone Track and Intensity Forecasting via Systematic Bias Correction
View PDF HTML (experimental)Abstract:Tropical cyclones (TCs) pose severe threats to life, infrastructure, and economies in tropical and subtropical regions, underscoring the critical need for accurate and timely forecasts of both track and intensity. Recent advances in AI-based weather forecasting have shown promise in improving TC track forecasts. However, these systems are typically trained on coarse-resolution reanalysis data (e.g., ERA5 at 0.25 degree), which constrains predicted TC positions to a fixed grid and introduces significant discretization errors. Moreover, intensity forecasting remains limited especially for strong TCs by the smoothing effect of coarse meteorological fields and the use of regression losses that bias predictions toward conditional means. To address these limitations, we propose BaguanCyclone, a novel, unified framework that integrates two key innovations: (1) a probabilistic center refinement module that models the continuous spatial distribution of TC centers, enabling finer track precision; and (2) a region-aware intensity forecasting module that leverages high-resolution internal representations within dynamically defined sub-grid zones around the TC core to better capture localized extremes. Evaluated on the global IBTrACS dataset across six major TC basins, our system consistently outperforms both operational numerical weather prediction (NWP) models and most AI-based baselines, delivering a substantial enhancement in forecast accuracy. Remarkably, BaguanCyclone excels in navigating meteorological complexities, consistently delivering accurate forecasts for re-intensification, sweeping arcs, twin cyclones, and meandering events. Our code is available at this https URL.
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
