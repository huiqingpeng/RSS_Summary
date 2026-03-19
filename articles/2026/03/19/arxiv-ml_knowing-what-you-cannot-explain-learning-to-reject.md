---
title: "Knowing What You Cannot Explain: Learning to Reject Low-Quality Explanations"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2507.12900"
published: "2026-03-19"
fetched: "2026-03-19T14:04:17.652828"
---

Computer Science > Machine Learning
[Submitted on 17 Jul 2025 (v1), last revised 17 Mar 2026 (this version, v3)]
Title:Knowing What You Cannot Explain: Learning to Reject Low-Quality Explanations
View PDF HTML (experimental)Abstract:Learning to Reject (LtR) frameworks allow ML models to abstain from uncertain predictions and promote user trust. However, since current LtR strategies focus solely on predictive performance, they completely neglect explanation quality. Low-quality explanations -- whether they inaccurately reflect the model's reasoning or fail to satisfy users -- can severely compromise trust assessments and induce over-reliance on incorrect predictions. We argue that models should abstain from making a prediction when they cannot offer a satisfactory explanation for it and introduce a framework for learning to reject low-quality explanations (LtX) in which predictors are equipped with a rejector that evaluates the explanation quality. Focusing on popular attribution techniques, we propose REX (REjector of low-quality eXplanations), which learns a rejector from explanation quality labels combining machine-side judgments with explicit human annotations to assess explanation quality. Our empirical evaluation demonstrates that \method outperforms popular LtR strategies and baselines relying on isolated explanation metrics. Finally, to support future research, we publicly release a novel, larger-scale dataset of 1050 human-annotated machine explanations.
Submission history
From: Luca Stradiotti [view email][v1] Thu, 17 Jul 2025 08:40:28 UTC (237 KB)
[v2] Fri, 18 Jul 2025 09:14:45 UTC (236 KB)
[v3] Tue, 17 Mar 2026 19:01:33 UTC (314 KB)
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
