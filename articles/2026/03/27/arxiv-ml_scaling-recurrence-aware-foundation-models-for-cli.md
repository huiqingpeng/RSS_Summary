---
title: "Scaling Recurrence-aware Foundation Models for Clinical Records via Next-Visit Prediction"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24562"
published: "2026-03-27"
fetched: "2026-03-28T07:11:43.834201"
---

Computer Science > Machine Learning
[Submitted on 25 Mar 2026]
Title:Scaling Recurrence-aware Foundation Models for Clinical Records via Next-Visit Prediction
View PDF HTML (experimental)Abstract:While large-scale pretraining has revolutionized language modeling, its potential remains underexplored in healthcare with structured electronic health records (EHRs). We present RAVEN, a novel generative pretraining strategy for sequential EHR data based on Recurrence-Aware next-Visit EveNt prediction. Leveraging a dataset of over one million unique individuals, our model learns to autoregressively generate tokenized clinical events for the next visit conditioned on patient history. We introduce regularization on predicting repeated events and highlight a key pitfall in EHR-based foundation model evaluations: repeated event tokens can inflate performance metrics when new onsets are not distinguished from subsequent occurrences. Furthermore, we empirically investigate the scaling behaviors in a data-constrained, compute-saturated regime, showing that simply increasing model size is suboptimal without commensurate increases in data volume. We evaluate our model via zero-shot prediction for forecasting the incidence of a diverse set of diseases, where it rivals fully fine-tuned representation-based Transformer models and outperforms widely used simulation-based next-token approaches. Finally, without additional parameter updates, we show that RAVEN can generalize to an external patient cohort under lossy clinical code mappings and feature coverage gaps.
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
