---
title: "Hypothesis Class Determines Explanation: Why Accurate Models Disagree on Feature Attribution"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15821"
published: "2026-03-18"
fetched: "2026-03-18T15:35:36.346317"
---

Computer Science > Machine Learning
[Submitted on 16 Mar 2026]
Title:Hypothesis Class Determines Explanation: Why Accurate Models Disagree on Feature Attribution
View PDF HTML (experimental)Abstract:The assumption that prediction-equivalent models produce equivalent explanations underlies many practices in explainable AI, including model selection, auditing, and regulatory evaluation. In this work, we show that this assumption does not hold. Through a large-scale empirical study across 24 datasets and multiple model classes, we find that models with identical predictive behavior can produce substantially different feature attributions.
This disagreement is highly structured: models within the same hypothesis class exhibit strong agreement, while cross-class pairs (e.g., tree-based vs. linear) trained on identical data splits show substantially reduced agreement, consistently near or below the lottery threshold. We identify hypothesis class as the structural driver of this phenomenon, which we term the Explanation Lottery.
We theoretically show that the resulting Agreement Gap persists under interaction structure in the data-generating process. This structural finding motivates a post-hoc diagnostic, the Explanation Reliability Score R(x), which predicts when explanations are stable across architectures without additional training.
Our results demonstrate that model selection is not explanation-neutral: the hypothesis class chosen for deployment can determine which features are attributed responsibility for a decision.
Submission history
From: Thackshanaramana Balashanmugam [view email][v1] Mon, 16 Mar 2026 18:55:50 UTC (252 KB)
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
