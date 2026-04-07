---
title: "Inference-Path Optimization via Circuit Duplication in Frozen Visual Transformers for Marine Species Classification"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2604.03428"
published: "2026-04-07"
fetched: "2026-04-08T07:02:56.611500"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 3 Apr 2026]
Title:Inference-Path Optimization via Circuit Duplication in Frozen Visual Transformers for Marine Species Classification
View PDF HTML (experimental)Abstract:Automated underwater species classification is constrained by annotation cost and environmental variation that limits the transferability of fully supervised models. Recent work has shown that frozen embeddings from self-supervised vision foundation models already provide a strong label-efficient baseline for marine image classification. Here we investigate whether this frozen-embedding regime can be improved at inference time, without fine-tuning or changing model weights.
We apply Circuit Duplication, an inference-time method originally proposed for Large Language Models, in which a selected range of transformer layers is traversed twice during the forward pass. We evaluate on the class-imbalanced AQUA20 benchmark using frozen DINOv3 embeddings under two settings: global circuit selection, where a single duplicated circuit is chosen for the full dataset, and class-specific circuit selection, where each species may receive a different optimal circuit. Both settings use simple semi-supervised downstream classifiers.
Circuit Duplication consistently improves over the standard frozen forward pass. At the maximum label budget, class-specific selection reaches a macro F1 of 0.875, closing the gap to the fully supervised ConvNeXt benchmark (0.889) to 1.4 points without any gradient-based training. Four species exceed their fully supervised reference, with octopus improving by +12.1 F1 points. Across all budgets, roughly 75% of classes prefer a class-specific circuit, indicating a genuinely class-dependent benefit. To our knowledge, this is the first application of Circuit Duplication to computer vision.
Current browse context:
cs.CV
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
ScienceCast (What is ScienceCast?)
Demos
Recommenders and Search Tools
Influence Flower (What are Influence Flowers?)
CORE Recommender (What is CORE?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
