---
title: "TimeAPN: Adaptive Amplitude-Phase Non-Stationarity Normalization for Time Series Forecasting"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17436"
published: "2026-03-19"
fetched: "2026-03-19T12:11:51.048323"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:TimeAPN: Adaptive Amplitude-Phase Non-Stationarity Normalization for Time Series Forecasting
View PDF HTML (experimental)Abstract:Non-stationarity is a fundamental challenge in multivariate long-term time series forecasting, often manifested as rapid changes in amplitude and phase. These variations lead to severe distribution shifts and consequently degrade predictive performance. Existing normalization-based methods primarily rely on first- and second-order statistics, implicitly assuming that distributions evolve smoothly and overlooking fine-grained temporal dynamics. To address these limitations, we propose TimeAPN, an Adaptive Amplitude-Phase Non-Stationarity Normalization framework that explicitly models and predicts non-stationary factors from both the time and frequency domains. Specifically, TimeAPN first models the mean sequence jointly in the time and frequency domains, and then forecasts its evolution over future horizons. Meanwhile, phase information is extracted in the frequency domain, and the phase discrepancy between the predicted and ground-truth future sequences is explicitly modeled to capture temporal misalignment. Furthermore, TimeAPN incorporates amplitude information into an adaptive normalization mechanism, enabling the model to effectively account for abrupt fluctuations in signal energy. The predicted non-stationary factors are subsequently integrated with the backbone forecasting outputs through a collaborative de-normalization process to reconstruct the final non-stationary time series. The proposed framework is model-agnostic and can be seamlessly integrated with various forecasting backbones. Extensive experiments on seven real-world multivariate datasets demonstrate that TimeAPN consistently improves long-term forecasting accuracy across multiple prediction horizons and outperforms state-of-the-art reversible normalization methods.
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
