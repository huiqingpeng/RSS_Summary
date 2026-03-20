---
title: "MLOW: Interpretable Low-Rank Frequency Magnitude Decomposition of Multiple Effects for Time Series Forecasting"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18432"
published: "2026-03-20"
fetched: "2026-03-20T12:11:31.745476"
---

Computer Science > Machine Learning
[Submitted on 19 Mar 2026]
Title:MLOW: Interpretable Low-Rank Frequency Magnitude Decomposition of Multiple Effects for Time Series Forecasting
View PDF HTML (experimental)Abstract:Separating multiple effects in time series is fundamental yet challenging for time-series forecasting (TSF). However, existing TSF models cannot effectively learn interpretable multi-effect decomposition by their smoothing-based temporal techniques. Here, a new interpretable frequency-based decomposition pipeline MLOW captures the insight: a time series can be represented as a magnitude spectrum multiplied by the corresponding phase-aware basis functions, and the magnitude spectrum distribution of a time series always exhibits observable patterns for different effects. MLOW learns a low-rank representation of the magnitude spectrum to capture dominant trending and seasonal effects. We explore low-rank methods, including PCA, NMF, and Semi-NMF, and find that none can simultaneously achieve interpretable, efficient and generalizable decomposition. Thus, we propose hyperplane-nonnegative matrix factorization (Hyperplane-NMF). Further, to address the frequency (spectral) leakage restricting high-quality low-rank decomposition, MLOW enables a flexible selection of input horizons and frequency levels via a mathematical mechanism. Visual analysis demonstrates that MLOW enables interpretable and hierarchical multiple-effect decomposition, robust to noises. It can also enable plug-and-play in existing TSF backbones with remarkable performance improvement but minimal architectural modifications.
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
