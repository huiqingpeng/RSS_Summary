---
title: "Mutually Causal Semantic Distillation Network for Zero-Shot Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17412"
published: "2026-03-19"
fetched: "2026-03-19T13:11:59.230772"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:Mutually Causal Semantic Distillation Network for Zero-Shot Learning
View PDF HTML (experimental)Abstract:Zero-shot learning (ZSL) aims to recognize the unseen classes in the open-world guided by the side-information (e.g., attributes). Its key task is how to infer the latent semantic knowledge between visual and attribute features on seen classes, and thus conducting a desirable semantic knowledge transfer from seen classes to unseen ones. Prior works simply utilize unidirectional attention within a weakly-supervised manner to learn the spurious and limited latent semantic representations, which fail to effectively discover the intrinsic semantic knowledge (e.g., attribute semantic) between visual and attribute features. To solve the above challenges, we propose a mutually causal semantic distillation network (termed MSDN++) to distill the intrinsic and sufficient semantic representations for ZSL. MSDN++ consists of an attribute$\rightarrow$visual causal attention sub-net that learns attribute-based visual features, and a visual$\rightarrow$attribute causal attention sub-net that learns visual-based attribute features. The causal attentions encourages the two sub-nets to learn causal vision-attribute associations for representing reliable features with causal visual/attribute learning. With the guidance of semantic distillation loss, the two mutual attention sub-nets learn collaboratively and teach each other throughout the training process. Extensive experiments on three widely-used benchmark datasets (e.g., CUB, SUN, AWA2, and FLO) show that our MSDN++ yields significant improvements over the strong baselines, leading to new state-of-the-art performances.
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
