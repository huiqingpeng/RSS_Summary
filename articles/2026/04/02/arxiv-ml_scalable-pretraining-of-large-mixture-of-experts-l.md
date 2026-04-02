---
title: "Scalable Pretraining of Large Mixture of Experts Language Models on Aurora Super Computer"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00785"
published: "2026-04-02"
fetched: "2026-04-03T07:24:47.369735"
---

Computer Science > Machine Learning
[Submitted on 1 Apr 2026]
Title:Scalable Pretraining of Large Mixture of Experts Language Models on Aurora Super Computer
View PDF HTML (experimental)Abstract:Pretraining Large Language Models (LLMs) from scratch requires massive amount of compute. Aurora super computer is an ExaScale machine with 127,488 Intel PVC (Ponte Vechio) GPU tiles. In this work, we showcase LLM pretraining on Aurora at the scale of 1000s of GPU tiles. Towards this effort, we developed Optimus, an inhouse training library with support for standard large model training techniques. Using Optimus, we first pretrained Mula-1B, a 1 Billion dense model and Mula-7B-A1B, a 7 Billion Mixture of Experts (MoE) model from scratch on 3072 GPU tiles for the full 4 trillion tokens of the OLMoE-mix-0924 dataset. We then demonstrated model scaling by pretraining three large MoE models Mula-20B-A2B, Mula-100B-A7B, and Mula-220B-A10B till 100 Billion tokens on the same dataset. On our largest model Mula-220B-A10B, we pushed the compute scaling from 384 to 12288 GPU tiles and observed scaling efficiency of around 90% at 12288 GPU tiles. We significantly improved the runtime performance of MoE models using custom GPU kernels for expert computation, and a novel EP-Aware sharded optimizer resulting in training speedups up to 1.71x. As part of the Optimus library, we also developed a robust set of reliability and fault tolerant features to improve training stability and continuity at scale.
Submission history
From: Dharma Teja Vooturi [view email][v1] Wed, 1 Apr 2026 11:46:17 UTC (794 KB)
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
