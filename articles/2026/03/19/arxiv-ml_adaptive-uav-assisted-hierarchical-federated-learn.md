---
title: "Adaptive UAV-Assisted Hierarchical Federated Learning: Optimizing Energy, Latency, and Resilience for Dynamic Smart IoT"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2503.06145"
published: "2026-03-19"
fetched: "2026-03-19T13:19:02.478116"
---

Computer Science > Machine Learning
[Submitted on 8 Mar 2025 (v1), last revised 18 Mar 2026 (this version, v4)]
Title:Adaptive UAV-Assisted Hierarchical Federated Learning: Optimizing Energy, Latency, and Resilience for Dynamic Smart IoT
View PDFAbstract:Hierarchical Federated Learning (HFL) extends conventional Federated Learning (FL) by introducing intermediate aggregation layers, enabling distributed learning in geographically dispersed environments, particularly relevant for smart IoT systems, such as remote monitoring and battlefield operations, where cellular connectivity is limited. In these scenarios, UAVs serve as mobile aggregators, dynamically connecting terrestrial IoT devices. This paper investigates an HFL architecture with energy-constrained, dynamically deployed UAVs prone to communication disruptions. We propose a novel approach to minimize global training costs by formulating a joint optimization problem that integrates learning configuration, bandwidth allocation, and device-to-UAV association, ensuring timely global aggregation before UAV disconnections and redeployments. The problem accounts for dynamic IoT devices and intermittent UAV connectivity and is NP-hard. To tackle this, we decompose it into three subproblems: \textit{(i)} optimizing learning configuration and bandwidth allocation via an augmented Lagrangian to reduce training costs; \textit{(ii)} introducing a device fitness score based on data heterogeneity (via Kullback-Leibler divergence), device-to-UAV proximity, and computational resources, using a TD3-based algorithm for adaptive device-to-UAV assignment; \textit{(iii)} developing a low-complexity two-stage greedy strategy for UAV redeployment and global aggregator selection, ensuring efficient aggregation despite UAV disconnections. Experiments on diverse real-world datasets validate the approach, demonstrating cost reduction and robust performance under communication disruptions.
Submission history
From: Xiaohong Yang [view email][v1] Sat, 8 Mar 2025 10:06:29 UTC (1,703 KB)
[v2] Mon, 24 Mar 2025 13:05:25 UTC (1,740 KB)
[v3] Mon, 13 Oct 2025 02:50:18 UTC (2,108 KB)
[v4] Wed, 18 Mar 2026 08:38:03 UTC (2,205 KB)
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
