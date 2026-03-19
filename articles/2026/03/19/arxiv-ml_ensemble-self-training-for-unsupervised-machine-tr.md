---
title: "Ensemble Self-Training for Unsupervised Machine Translation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17087"
published: "2026-03-19"
fetched: "2026-03-19T13:08:39.493509"
---

Computer Science > Computation and Language
[Submitted on 17 Mar 2026]
Title:Ensemble Self-Training for Unsupervised Machine Translation
View PDF HTML (experimental)Abstract:We present an ensemble-driven self-training framework for unsupervised neural machine translation (UNMT). Starting from a primary language pair, we train multiple UNMT models that share the same translation task but differ in an auxiliary language, inducing structured diversity across models. We then generate pseudo-translations for the primary pair using token-level ensemble decoding, averaging model predictions in both directions. These ensemble outputs are used as synthetic parallel data to further train each model, allowing the models to improve via shared supervision. At deployment time, we select a single model by validation performance, preserving single-model inference cost. Experiments show statistically significant improvements over single-model UNMT baselines, with mean gains of 1.7 chrF when translating from English and 0.67 chrF when translating into English.
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
