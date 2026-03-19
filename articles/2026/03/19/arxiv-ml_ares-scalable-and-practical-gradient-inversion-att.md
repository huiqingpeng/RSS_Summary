---
title: "ARES: Scalable and Practical Gradient Inversion Attack in Federated Learning through Activation Recovery"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17623"
published: "2026-03-19"
fetched: "2026-03-19T12:14:49.891840"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:ARES: Scalable and Practical Gradient Inversion Attack in Federated Learning through Activation Recovery
View PDF HTML (experimental)Abstract:Federated Learning (FL) enables collaborative model training by sharing model updates instead of raw data, aiming to protect user privacy. However, recent studies reveal that these shared updates can inadvertently leak sensitive training data through gradient inversion attacks (GIAs). Among them, active GIAs are particularly powerful, enabling high-fidelity reconstruction of individual samples even under large batch sizes. Nevertheless, existing approaches often require architectural modifications, which limit their practical applicability. In this work, we bridge this gap by introducing the Activation REcovery via Sparse inversion (ARES) attack, an active GIA designed to reconstruct training samples from large training batches without requiring architectural modifications. Specifically, we formulate the recovery problem as a noisy sparse recovery task and solve it using the generalized Least Absolute Shrinkage and Selection Operator (Lasso). To extend the attack to multi-sample recovery, ARES incorporates the imprint method to disentangle activations, enabling scalable per-sample reconstruction. We further establish the expected recovery rate and derive an upper bound on the reconstruction error, providing theoretical guarantees for the ARES attack. Extensive experiments on CNNs and MLPs demonstrate that ARES achieves high-fidelity reconstruction across diverse datasets, significantly outperforming prior GIAs under large batch sizes and realistic FL settings. Our results highlight that intermediate activations pose a serious and underestimated privacy risk in FL, underscoring the urgent need for stronger defenses.
Submission history
From: Leo Yu Zhang Dr. [view email][v1] Wed, 18 Mar 2026 11:40:44 UTC (10,190 KB)
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
