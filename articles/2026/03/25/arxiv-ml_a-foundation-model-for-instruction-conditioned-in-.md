---
title: "A Foundation Model for Instruction-Conditioned In-Context Time Series Tasks"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22586"
published: "2026-03-25"
fetched: "2026-03-26T07:15:28.955639"
---

Computer Science > Machine Learning
[Submitted on 23 Mar 2026]
Title:A Foundation Model for Instruction-Conditioned In-Context Time Series Tasks
View PDF HTML (experimental)Abstract:In-context learning (ICL) allows a model to adapt at inference time by conditioning on examples rather than updating parameters. Existing time-series foundation models use implicit positional context, retrieval, or task-specific objectives, but rarely explicit instruction-conditioned demonstrations. We present a foundation model for instruction-conditioned in-context time-series tasks based on a quantile-regression T5 encoder-decoder. Historical examples and queries are encoded with a structured tokenization scheme that marks target series, covariates, context, and task-specific future information. A hierarchical Transformer with per-example encoding, example-level fusion, and cross-example attention conditions decoding on demonstration pairs, enabling forecasting and related tasks without task-specific fine-tuning. We train on large-scale real and synthetic time series using supervised forecasting plus self-supervised tasks, including imputation, reconstruction, classification, anomaly detection, and source demixing. This multi-task training learns a distribution over task mappings and improves adaptation to local structure at inference time. Across diverse datasets, frequencies, and horizons, our method outperforms strong foundation baselines on point and probabilistic forecasting benchmarks, including fev-bench and GIFT-Eval, while remaining competitive on classification and anomaly detection.
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
