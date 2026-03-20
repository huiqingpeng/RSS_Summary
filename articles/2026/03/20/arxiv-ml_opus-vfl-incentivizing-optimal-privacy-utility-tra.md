---
title: "OPUS-VFL: Incentivizing Optimal Privacy-Utility Tradeoffs in Vertical Federated Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2504.15995"
published: "2026-03-20"
fetched: "2026-03-20T14:05:47.776358"
---

Computer Science > Machine Learning
[Submitted on 22 Apr 2025 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:OPUS-VFL: Incentivizing Optimal Privacy-Utility Tradeoffs in Vertical Federated Learning
View PDF HTML (experimental)Abstract:Vertical Federated Learning (VFL) enables organizations with disjoint feature spaces but shared user bases to collaboratively train models without sharing raw data. However, existing VFL systems face critical limitations: they often lack effective incentive mechanisms, struggle to balance privacy-utility tradeoffs, and fail to accommodate clients with heterogeneous resource capabilities. These challenges hinder meaningful participation, degrade model performance, and limit practical deployment. To address these issues, we propose OPUS-VFL, an Optimal Privacy-Utility tradeoff Strategy for VFL. OPUS-VFL introduces a novel, privacy-aware incentive mechanism that rewards clients based on a principled combination of model contribution, privacy preservation, and resource investment. It employs a lightweight leave-one-out (LOO) strategy to quantify feature importance per client, and integrates an adaptive differential privacy mechanism that enables clients to dynamically calibrate noise levels to optimize their individual utility. Our framework is designed to be scalable, budget-balanced, and robust to inference and poisoning attacks. Extensive experiments on benchmark datasets (MNIST, CIFAR-10, and CIFAR-100) demonstrate that OPUS-VFL significantly outperforms state-of-the-art VFL baselines in both efficiency and robustness. It reduces label inference attack success rates by up to 20%, increases feature inference reconstruction error (MSE) by over 30%, and achieves up to 25% higher incentives for clients that contribute meaningfully while respecting privacy and cost constraints. These results highlight the practicality and innovation of OPUS-VFL as a secure, fair, and performance-driven solution for real-world VFL.
Submission history
From: Sindhuja Madabushi [view email][v1] Tue, 22 Apr 2025 16:00:11 UTC (3,081 KB)
[v2] Wed, 18 Mar 2026 20:16:11 UTC (3,077 KB)
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
