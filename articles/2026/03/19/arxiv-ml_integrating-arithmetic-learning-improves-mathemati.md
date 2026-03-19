---
title: "Integrating Arithmetic Learning Improves Mathematical Reasoning in Smaller Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2502.12855"
published: "2026-03-19"
fetched: "2026-03-19T14:14:41.503374"
---

Computer Science > Computation and Language
[Submitted on 18 Feb 2025 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:Integrating Arithmetic Learning Improves Mathematical Reasoning in Smaller Models
View PDFAbstract:While large models pre-trained on high-quality data exhibit excellent performance on mathematical reasoning (e.g., GSM8k, MultiArith), it remains challenging to specialize smaller models for these tasks. Common approaches to address this challenge include knowledge distillation from large teacher models and data augmentation (e.g., rephrasing questions and generating synthetic solutions). Despite these efforts, smaller models struggle with arithmetic computations, leading to errors in mathematical reasoning. In this work, we leverage a synthetic arithmetic dataset generated programmatically to enhance the reasoning capabilities of smaller models. We investigate two key approaches to incorporate this dataset: (1) intermediate fine-tuning, in which a model is fine-tuned on the arithmetic dataset before training it on a reasoning dataset, and (2) integrating the arithmetic dataset into an instruction-tuning mixture, allowing the model to learn arithmetic skills alongside general instruction-following abilities. Our experiments on multiple reasoning benchmarks demonstrate that incorporating an arithmetic dataset, whether through targeted fine-tuning or within an instruction-tuning mixture, enhances models' arithmetic capabilities, thereby improving their mathematical reasoning performance.
Submission history
From: Neeraj Gangwar [view email][v1] Tue, 18 Feb 2025 13:43:06 UTC (105 KB)
[v2] Wed, 18 Mar 2026 17:43:04 UTC (115 KB)
Current browse context:
cs.CL
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
