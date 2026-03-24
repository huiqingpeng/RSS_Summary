---
title: "Benchmarking Scientific Machine Learning Models for Air Quality Data"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.21039"
published: "2026-03-24"
fetched: "2026-03-25T07:18:06.606490"
---

Computer Science > Machine Learning
[Submitted on 22 Mar 2026]
Title:Benchmarking Scientific Machine Learning Models for Air Quality Data
View PDF HTML (experimental)Abstract:Accurate air quality index (AQI) forecasting is essential for the protecting public health in rapidly growing urban regions, and the practical model evaluation and selection are often challenged by the lack of rigorous, region-specific benchmarking on standardized datasets. Physics-guided machine learning and deep learning models could be a good and effective solution to resolve such issues with more accurate and efficient AQI forecasting. This research study presents an explainable and comprehensive benchmark that enables a guideline and proposed physics-guided best model by benchmarking classical time-series, machine-learning, and deep-learning approaches for multi-horizon AQI forecasting in North Texas (Dallas County). Using publicly available U.S. Environmental Protection Agency (EPA) daily observations of air quality data from 2022 to 2024, we curate city-level time series for PM2.5 and O3 by aggregating station measurements and constructing lag-wise forecasting datasets for LAG in {1,7,14,30} days. For benchmarking the best model, linear regression (LR), SARIMAX, multilayer perceptrons (MLP), and LSTM networks are evaluated with the proposed physics-guided variants (MLP+Physics and LSTM+Physics) that incorporate the EPA breakpoint-based AQI formulation as a consistency constraint through a weighted loss. Experiments using chronological train-test splits and error metrics MAE, RMSE showed that deep-learning models outperform simpler baselines, while physics guidance improves stability and yields physically consistent pollutant with AQI relationships, with the largest benefits observed for short-horizon prediction and for PM2.5 and O3. Overall, the results provide a practical reference for selecting AQI forecasting models in North Texas and clarify when lightweight physics constraints meaningfully improve predictive performance across pollutants and forecast horizons.
Submission history
From: Khawja Imran Masud [view email][v1] Sun, 22 Mar 2026 03:31:24 UTC (10,657 KB)
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
