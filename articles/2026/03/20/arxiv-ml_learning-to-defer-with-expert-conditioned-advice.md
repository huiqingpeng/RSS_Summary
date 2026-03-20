---
title: "Learning-to-Defer with Expert-Conditioned Advice"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.14324"
published: "2026-03-20"
fetched: "2026-03-20T15:04:54.516948"
---

Statistics > Machine Learning
[Submitted on 15 Mar 2026 (v1), last revised 19 Mar 2026 (this version, v2)]
Title:Learning-to-Defer with Expert-Conditioned Advice
View PDF HTML (experimental)Abstract:Learning-to-Defer routes each input to the expert that minimizes expected cost, but it assumes that the information available to every expert is fixed at decision time. Many modern systems violate this assumption: after selecting an expert, one may also choose what additional information that expert should receive, such as retrieved documents, tool outputs, or escalation context. We study this problem and call it Learning-to-Defer with advice. We show that a broad family of natural separated surrogates, which learn routing and advice with distinct heads, is inconsistent even in the smallest non-trivial setting. We then introduce an augmented surrogate that operates on the composite expert--advice action space and prove an $\mathcal{H}$-consistency guarantee together with an excess-risk transfer bound, yielding recovery of the Bayes-optimal policy in the limit. Experiments on tabular, language, and multi-modal tasks show that the resulting method improves over standard Learning-to-Defer while adapting its advice-acquisition behavior to the cost regime; a synthetic benchmark confirms the failure mode predicted for separated surrogates.
Submission history
From: Yannis Montreuil [view email][v1] Sun, 15 Mar 2026 10:52:58 UTC (217 KB)
[v2] Thu, 19 Mar 2026 04:19:16 UTC (218 KB)
Current browse context:
stat.ML
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
