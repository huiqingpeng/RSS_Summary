---
title: "Benchmarking State Space Models, Transformers, and Recurrent Networks for US Grid Forecasting"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2602.21415"
published: "2026-03-20"
fetched: "2026-03-20T14:11:15.410711"
---

Computer Science > Machine Learning
[Submitted on 24 Feb 2026 (v1), last revised 19 Mar 2026 (this version, v2)]
Title:Benchmarking State Space Models, Transformers, and Recurrent Networks for US Grid Forecasting
View PDF HTML (experimental)Abstract:Selecting the right deep learning model for power grid forecasting is challenging, as performance heavily depends on the data available to the operator. This paper presents a comprehensive benchmark of five modern neural architectures: two state space models (PowerMamba, S-Mamba), two Transformers (iTransformer, PatchTST), and a traditional LSTM. We evaluate these models on hourly electricity demand across six diverse US power grids for forecast windows between 24 and 168 hours. To ensure a fair comparison, we adapt each model with specialized temporal processing and a modular layer that cleanly integrates weather covariates. Our results reveal that there is no single best model for all situations. When forecasting using only historical load, PatchTST and the state space models provide the highest accuracy. However, when explicit weather data is added to the inputs, the rankings reverse: iTransformer improves its accuracy three times more efficiently than PatchTST. By controlling for model size, we confirm that this advantage stems from the architecture's inherent ability to mix information across different variables. Extending our evaluation to solar generation, wind power, and wholesale prices further demonstrates that model rankings depend on the forecast task: PatchTST excels on highly rhythmic signals like solar, while state space models are better suited for the chaotic fluctuations of wind and price. Ultimately, this benchmark provides grid operators with actionable guidelines for selecting the optimal forecasting architecture based on their specific data environments.
Submission history
From: Jisoo Lee [view email][v1] Tue, 24 Feb 2026 22:42:39 UTC (2,320 KB)
[v2] Thu, 19 Mar 2026 02:29:57 UTC (2,055 KB)
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
