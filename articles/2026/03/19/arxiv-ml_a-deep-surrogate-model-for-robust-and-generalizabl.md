---
title: "A Deep Surrogate Model for Robust and Generalizable Long-Term Blast Wave Prediction"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2602.18168"
published: "2026-03-19"
fetched: "2026-03-19T14:12:09.487158"
---

Computer Science > Machine Learning
This paper has been withdrawn by Xinhai Chen
[Submitted on 20 Feb 2026 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:A Deep Surrogate Model for Robust and Generalizable Long-Term Blast Wave Prediction
No PDF available, click to view other formatsAbstract:Accurately modeling the spatio-temporal dynamics of blast wave propagation remains a longstanding challenge due to its highly nonlinear behavior, sharp gradients, and burdensome computational cost. While machine learning-based surrogate models offer fast inference as a promising alternative, they suffer from degraded accuracy, particularly evaluated on complex urban layouts or out-of-distribution scenarios. Moreover, autoregressive prediction strategies in such models are prone to error accumulation over long forecasting horizons, limiting their robustness for extended-time simulations. To address these limitations, we propose RGD-Blast, a robust and generalizable deep surrogate model for high-fidelity, long-term blast wave forecasting. RGD-Blast incorporates a multi-scale module to capture both global flow patterns and local boundary interactions, effectively mitigating error accumulation during autoregressive prediction. We introduce a dynamic-static feature coupling mechanism that fuses time-varying pressure fields with static source and layout features, thereby enhancing out-of-distribution generalization. Experiments demonstrate that RGD-Blast achieves a two-order-of-magnitude speedup over traditional numerical methods while maintaining comparable accuracy. In generalization tests on unseen building layouts, the model achieves an average RMSE below 0.01 and an R2 exceeding 0.89 over 280 consecutive time steps. Additional evaluations under varying blast source locations and explosive charge weights further validate its generalization, substantially advancing the state of the art in long-term blast wave modeling.
Submission history
From: Xinhai Chen [view email][v1] Fri, 20 Feb 2026 12:14:28 UTC (27,684 KB)
[v2] Wed, 18 Mar 2026 01:27:13 UTC (1 KB) (withdrawn)
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
