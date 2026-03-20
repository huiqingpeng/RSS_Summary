---
title: "Towards Efficient and Stable Ocean State Forecasting: A Continuous-Time Koopman Approach"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.05560"
published: "2026-03-20"
fetched: "2026-03-20T14:11:58.851605"
---

Computer Science > Machine Learning
[Submitted on 5 Mar 2026 (v1), last revised 19 Mar 2026 (this version, v2)]
Title:Towards Efficient and Stable Ocean State Forecasting: A Continuous-Time Koopman Approach
View PDF HTML (experimental)Abstract:We investigate the Continuous-Time Koopman Autoencoder (CT-KAE) as a lightweight surrogate model for long-horizon ocean state forecasting in a two-layer quasi-geostrophic (QG) system. By projecting nonlinear dynamics into a latent space governed by a linear ordinary differential equation, the model enforces structured and interpretable temporal evolution while enabling temporally resolution-invariant forecasting via a matrix exponential formulation. Across 2083-day rollouts, CT-KAE exhibits bounded error growth and stable large-scale statistics, in contrast to autoregressive Transformer baselines which exhibit gradual error amplification and energy drift over long rollouts. While fine-scale turbulent structures are partially dissipated, bulk energy spectra, enstrophy evolution, and autocorrelation structure remain consistent over long horizons. The model achieves orders-of-magnitude faster inference compared to the numerical solver, suggesting that continuous-time Koopman surrogates offer a promising backbone for efficient and stable physical-machine learning climate models.
Submission history
From: Rares Grozavescu [view email][v1] Thu, 5 Mar 2026 09:39:44 UTC (4,615 KB)
[v2] Thu, 19 Mar 2026 10:03:30 UTC (2,054 KB)
Current browse context:
cs.LG
Change to browse by:
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
