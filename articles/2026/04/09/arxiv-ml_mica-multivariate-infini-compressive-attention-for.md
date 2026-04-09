---
title: "MICA: Multivariate Infini Compressive Attention for Time Series Forecasting"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.06473"
published: "2026-04-09"
fetched: "2026-04-10T07:05:00.376239"
---

Computer Science > Machine Learning
[Submitted on 7 Apr 2026]
Title:MICA: Multivariate Infini Compressive Attention for Time Series Forecasting
View PDFAbstract:Multivariate forecasting with Transformers faces a core scalability challenge: modeling cross-channel dependencies via attention compounds attention's quadratic sequence complexity with quadratic channel scaling, making full cross-channel attention impractical for high-dimensional time series. We propose Multivariate Infini Compressive Attention (MICA), an architectural design to extend channel-independent Transformers to channel-dependent forecasting. By adapting efficient attention techniques from the sequence dimension to the channel dimension, MICA adds a cross-channel attention mechanism to channel-independent backbones that scales linearly with channel count and context length. We evaluate channel-independent Transformer architectures with and without MICA across multiple forecasting benchmarks. MICA reduces forecast error over its channel-independent counterparts by 5.4% on average and up to 25.4% on individual datasets, highlighting the importance of explicit cross-channel modeling. Moreover, models with MICA rank first among deep multivariate Transformer and MLP baselines. MICA models also scale more efficiently with respect to both channel count and context length than Transformer baselines that compute attention across both the temporal and channel dimensions, establishing compressive attention as a practical solution for scalable multivariate forecasting.
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
