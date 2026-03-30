---
title: "Preventing Data Leakage in EEG-Based Survival Prediction: A Two-Stage Embedding and Transformer Framework"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.25923"
published: "2026-03-30"
fetched: "2026-03-31T07:19:41.701533"
---

Computer Science > Machine Learning
[Submitted on 26 Mar 2026]
Title:Preventing Data Leakage in EEG-Based Survival Prediction: A Two-Stage Embedding and Transformer Framework
View PDF HTML (experimental)Abstract:Deep learning models have shown promise in EEG-based outcome prediction for comatose patients after cardiac arrest, but their reliability is often compromised by subtle forms of data leakage. In particular, when long EEG recordings are segmented into short windows and reused across multiple training stages, models may implicitly encode and propagate label information, leading to overly optimistic validation performance and poor generalization.
In this study, we identify a previously overlooked form of data leakage in multi-stage EEG modeling pipelines. We demonstrate that violating strict patient-level separation can significantly inflate validation metrics while causing substantial degradation on independent test data.
To address this issue, we propose a leakage-aware two-stage framework. In the first stage, short EEG segments are transformed into embedding representations using a convolutional neural network with an ArcFace objective. In the second stage, a Transformer-based model aggregates these embeddings to produce patient-level predictions, with strict isolation between training cohorts to eliminate leakage pathways.
Experiments on a large-scale EEG dataset of post-cardiac-arrest patients show that the proposed framework achieves stable and generalizable performance under clinically relevant constraints, particularly in maintaining high sensitivity at stringent specificity thresholds. These results highlight the importance of rigorous data partitioning and provide a practical solution for reliable EEG-based outcome prediction.
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
