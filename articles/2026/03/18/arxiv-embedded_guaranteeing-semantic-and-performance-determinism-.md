---
title: "Guaranteeing Semantic and Performance Determinism in Flexible GPU Sharing"
source: "arXiv Embedded Systems"
url: "https://arxiv.org/abs/2603.15042"
published: "2026-03-18"
fetched: "2026-03-18T14:52:04.049558"
---

Computer Science > Distributed, Parallel, and Cluster Computing
[Submitted on 16 Mar 2026 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:Guaranteeing Semantic and Performance Determinism in Flexible GPU Sharing
View PDF HTML (experimental)Abstract:GPU sharing is critical for maximizing hardware utilization in modern data centers. However, existing approaches present a stark trade-off: coarse-grained temporal multiplexing incurs severe tail-latency spikes for interactive services, while fine-grained spatial partitioning often necessitates invasive kernel modifications that compromise behavioral equivalence.
We present DetShare, a novel GPU sharing system that prioritizes determinism and transparency. DetShare ensures semantic determinism (unmodified kernels yield identical results) and performance determinism (predictable tail latency), all while maintaining complete transparency (zero code modification). DetShare introduces GPU coroutines, a new abstraction that decouples logical execution contexts from physical GPU resources. This decoupling enables flexible, fine-grained resource allocation via lightweight context migration.
Our evaluation demonstrates that DetShare improves training throughput by up to 79.2% compared to temporal sharing. In co-location scenarios, it outperforms state-of-the-art baselines, reducing P99 tail latency by 15.1% without compromising throughput. Furthermore, through workload-aware placement and our TPOT-First scheduling policy, DetShare decreases average inference latency by 69.1% and reduces Time-Per-Output-Token (TPOT) SLO violations by 21.2% relative to default policies.
Submission history
From: Zhenyuan Yang [view email][v1] Mon, 16 Mar 2026 09:48:34 UTC (3,121 KB)
[v2] Tue, 17 Mar 2026 08:51:40 UTC (3,121 KB)
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
