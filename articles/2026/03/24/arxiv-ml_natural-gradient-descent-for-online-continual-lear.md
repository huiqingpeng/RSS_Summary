---
title: "Natural Gradient Descent for Online Continual Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20898"
published: "2026-03-24"
fetched: "2026-03-25T07:15:32.523176"
---

Computer Science > Machine Learning
[Submitted on 21 Mar 2026]
Title:Natural Gradient Descent for Online Continual Learning
View PDF HTML (experimental)Abstract:Online Continual Learning (OCL) for image classification represents a challenging subset of Continual Learning, focusing on classifying images from a stream without assuming data independence and identical distribution (i.i.d). The primary challenge in this context is to prevent catastrophic forgetting, where the model's performance on previous tasks deteriorates as it learns new ones. Although various strategies have been proposed to address this issue, achieving rapid convergence remains a significant challenge in the online setting. In this work, we introduce a novel approach to training OCL models that utilizes the Natural Gradient Descent optimizer, incorporating an approximation of the Fisher Information Matrix (FIM) through Kronecker Factored Approximate Curvature (KFAC). This method demonstrates substantial improvements in performance across all OCL methods, particularly when combined with existing OCL tricks, on datasets such as Split CIFAR-100, CORE50, and Split miniImageNet.
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
