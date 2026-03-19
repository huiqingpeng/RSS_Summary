---
title: "Hidden Clones: Exposing and Fixing Family Bias in Vision-Language Model Ensembles"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17111"
published: "2026-03-19"
fetched: "2026-03-19T15:05:15.644165"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:Hidden Clones: Exposing and Fixing Family Bias in Vision-Language Model Ensembles
View PDF HTML (experimental)Abstract:Ensembling Vision-Language Models (VLMs) from different providers maximizes benchmark accuracy, yet models from the same architectural family share correlated errors that standard voting ignores. We study this structure across 17 VLMs from 8 families on VQAv2, TextVQA, and GQA. Family-correlated errors reduce effective ensemble dimensionality to 2.5-3.6 independent voters and create a Misleading tier (1.5-6.5% of questions) where correlated majority errors destroy accuracy to 0% despite the best model being correct.
We propose three family-aware methods. Hierarchical Family Voting (HFV) aggregates within families before voting across them, recovering +18-26 pp on the Misleading tier. QualRCCV, a training-free method weighting models by calibration, family quality, and inverse family size, is the first to beat calibrated voting on all three benchmarks (p<0.05). Learned Candidate Scoring (LCS) trains a cross-validated classifier to re-rank candidate answers using support breadth, family diversity, and model quality, achieving the largest gains: +0.68% VQAv2, +0.61% TextVQA, +2.45% GQA -- all significant -- and is the only learned method that never degrades any benchmark. On VQAv2 test-standard (EvalAI), LCS reaches 87.83% with 12 models, confirming generalization.
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
