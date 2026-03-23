---
title: "Graph2TS: Structure-Controlled Time Series Generation via Quantile-Graph VAEs"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19970"
published: "2026-03-23"
fetched: "2026-03-24T07:23:31.341400"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:Graph2TS: Structure-Controlled Time Series Generation via Quantile-Graph VAEs
View PDF HTML (experimental)Abstract:Although recent generative models can produce time series with close marginal distributions, they often face a fundamental tension between preserving global temporal structure and modeling stochastic local variations, particularly for highly volatile signals with weak or irregular periodicity. Direct distribution matching in such settings can amplify noise or suppress meaningful temporal patterns. In this work, we propose a structure-residual perspective on time-series generation, viewing temporal data as the combination of a structural backbone and stochastic residual dynamics, thereby motivating the separation of global organization from sample-level variability. Based on this insight, we represent time-series structure using a quantile-based transition graph that compactly captures global distributional and temporal dependencies. Building on this representation, we propose Graph2TS, a quantile-graph conditioned variational autoencoder that performs cross-modal generation from structural graphs to time series. By conditioning generation on structure rather than labels or metadata, the model preserves global temporal organization while enabling controlled stochastic variation. Experiments on diverse datasets, including sunspot, electricity load, ECG, and EEG signals, demonstrate improved distributional fidelity, temporal alignment, and representativeness compared to diffusion- and GAN-based baselines, highlighting structure-controlled and cross-modal generation as a promising direction for time-series modeling.
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
