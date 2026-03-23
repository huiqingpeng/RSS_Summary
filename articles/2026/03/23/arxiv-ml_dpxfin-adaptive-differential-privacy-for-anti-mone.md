---
title: "DPxFin: Adaptive Differential Privacy for Anti-Money Laundering Detection via Reputation-Weighted Federated Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19314"
published: "2026-03-23"
fetched: "2026-03-24T07:16:42.226345"
---

Computer Science > Machine Learning
[Submitted on 14 Mar 2026]
Title:DPxFin: Adaptive Differential Privacy for Anti-Money Laundering Detection via Reputation-Weighted Federated Learning
View PDF HTML (experimental)Abstract:In the modern financial system, combating money laundering is a critical challenge complicated by data privacy concerns and increasingly complex fraud transaction patterns. Although federated learning (FL) is a promising problem-solving approach as it allows institutions to train their models without sharing their data, it has the drawback of being prone to privacy leakage, specifically in tabular data forms like financial data. To address this, we propose DPxFin, a novel federated framework that integrates reputation-guided adaptive differential privacy. Our approach computes client reputation by evaluating the alignment between locally trained models and the global model. Based on this reputation, we dynamically assign differential privacy noise to client updates, enhancing privacy while maintaining overall model utility. Clients with higher reputations receive lower noise to amplify their trustworthy contributions, while low-reputation clients are allocated stronger noise to mitigate risk. We validate DPxFin on the Anti-Money Laundering (AML) dataset under both IID and non-IID settings using Multi Layer Perceptron (MLP). Experimental analysis established that our approach has a more desirable trade-off between accuracy and privacy than those of traditional FL and fixed-noise Differential Privacy (DP) baselines, where performance improvements were consistent, even though on a modest scale. Moreover, DPxFin does withstand tabular data leakage attacks, proving its effectiveness under real-world financial conditions.
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
