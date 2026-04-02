---
title: "G-Drift MIA: Membership Inference via Gradient-Induced Feature Drift in LLMs"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00419"
published: "2026-04-02"
fetched: "2026-04-03T07:21:19.428909"
---

Computer Science > Machine Learning
[Submitted on 1 Apr 2026]
Title:G-Drift MIA: Membership Inference via Gradient-Induced Feature Drift in LLMs
View PDF HTML (experimental)Abstract:Large language models (LLMs) are trained on massive web-scale corpora, raising growing concerns about privacy and copyright. Membership inference attacks (MIAs) aim to determine whether a given example was used during training. Existing LLM MIAs largely rely on output probabilities or loss values and often perform only marginally better than random guessing when members and non-members are drawn from the same distribution. We introduce G-Drift MIA, a white-box membership inference method based on gradient-induced feature drift. Given a candidate (x,y), we apply a single targeted gradient-ascent step that increases its loss and measure the resulting changes in internal representations, including logits, hidden-layer activations, and projections onto fixed feature directions, before and after the update. These drift signals are used to train a lightweight logistic classifier that effectively separates members from non-members. Across multiple transformer-based LLMs and datasets derived from realistic MIA benchmarks, G-Drift substantially outperforms confidence-based, perplexity-based, and reference-based attacks. We further show that memorized training samples systematically exhibit smaller and more structured feature drift than non-members, providing a mechanistic link between gradient geometry, representation stability, and memorization. In general, our results demonstrate that small, controlled gradient interventions offer a practical tool for auditing the membership of training-data and assessing privacy risks in LLMs.
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
