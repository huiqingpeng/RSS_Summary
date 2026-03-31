---
title: "Conformalized Signal Temporal Logic Inference under Covariate Shift"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.27062"
published: "2026-03-31"
fetched: "2026-04-01T07:21:15.409429"
---

Computer Science > Machine Learning
[Submitted on 28 Mar 2026]
Title:Conformalized Signal Temporal Logic Inference under Covariate Shift
View PDF HTML (experimental)Abstract:Signal Temporal Logic (STL) inference learns interpretable logical rules for temporal behaviors in dynamical systems. To ensure the correctness of learned STL formulas, recent approaches have incorporated conformal prediction as a statistical tool for uncertainty quantification. However, most existing methods rely on the assumption that calibration and testing data are identically distributed and exchangeable, an assumption that is frequently violated in real-world settings. This paper proposes a conformalized STL inference framework that explicitly addresses covariate shift between training and deployment trajectories dataset. From a technical standpoint, the approach first employs a template-free, differentiable STL inference method to learn an initial model, and subsequently refines it using a limited deployment side dataset to promote distribution alignment. To provide validity guarantees under distribution shift, the framework estimates the likelihood ratio between training and deployment distributions and integrates it into an STL-robustness-based weighted conformal prediction scheme. Experimental results on trajectory datasets demonstrate that the proposed framework preserves the interpretability of STL formulas while significantly improving symbolic learning reliability at deployment time.
Current browse context:
cs.LG
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
