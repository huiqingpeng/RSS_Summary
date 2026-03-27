---
title: "Not All Pretraining are Created Equal: Threshold Tuning and Class Weighting for Imbalanced Polarization Tasks in Low-Resource Settings"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23534"
published: "2026-03-27"
fetched: "2026-03-28T07:13:12.484739"
---

Computer Science > Computation and Language
[Submitted on 8 Mar 2026]
Title:Not All Pretraining are Created Equal: Threshold Tuning and Class Weighting for Imbalanced Polarization Tasks in Low-Resource Settings
View PDF HTML (experimental)Abstract:This paper describes my submission to the Polarization Shared Task at SemEval-2025, which addresses polarization detection and classification in social media text. I develop Transformer-based systems for English and Swahili across three subtasks: binary polarization detection, multi-label target type classification, and multi-label manifestation identification. The approach leverages multilingual and African language-specialized models (mDeBERTa-v3-base, SwahBERT, AfriBERTa-large), class-weighted loss functions, iterative stratified data splitting, and per-label threshold tuning to handle severe class imbalance. The best configuration, mDeBERTa-v3-base, achieves 0.8032 macro-F1 on validation for binary detection, with competitive performance on multi-label tasks (up to 0.556 macro-F1). Error analysis reveals persistent challenges with implicit polarization, code-switching, and distinguishing heated political discourse from genuine polarization.
Submission history
From: Abass Oguntade Mr [view email][v1] Sun, 8 Mar 2026 15:50:37 UTC (2,561 KB)
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
