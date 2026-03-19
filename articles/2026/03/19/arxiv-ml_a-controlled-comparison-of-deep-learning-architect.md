---
title: "A Controlled Comparison of Deep Learning Architectures for Multi-Horizon Financial Forecasting: Evidence from 918 Experiments"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16886"
published: "2026-03-19"
fetched: "2026-03-19T13:05:34.916490"
---

Quantitative Finance > Statistical Finance
[Submitted on 27 Feb 2026]
Title:A Controlled Comparison of Deep Learning Architectures for Multi-Horizon Financial Forecasting: Evidence from 918 Experiments
View PDF HTML (experimental)Abstract:Multi-horizon price forecasting is central to portfolio allocation, risk management, and algorithmic trading, yet deep learning architectures have proliferated faster than rigorous financial benchmarks can evaluate them. This study provides a controlled comparison of nine architectures (Autoformer, DLinear, iTransformer, LSTM, ModernTCN, N-HiTS, PatchTST, TimesNet, and TimeXer) spanning Transformer, MLP, CNN, and RNN families across cryptocurrency, forex, and equity index markets at 4-hour and 24-hour horizons. A total of 918 experiments were conducted under a strict five-stage protocol including fixed-seed Bayesian hyperparameter optimization, configuration freezing per asset class, multi-seed retraining, uncertainty aggregation, and statistical validation. ModernTCN achieves the best mean rank (1.333) with a 75 percent first-place rate, followed by PatchTST (2.000). Results reveal a clear three-tier ranking structure and show that architecture explains nearly all performance variance, while seed randomness is negligible. Rankings remain stable across horizons despite 2 to 2.5 times error amplification. Directional accuracy remains near 50 percent across all configurations, indicating that MSE-trained models lack directional skill at hourly resolution. The findings highlight the importance of architectural inductive bias over raw parameter count and provide reproducible guidance for multi-step financial forecasting.
Current browse context:
q-fin.ST
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
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
