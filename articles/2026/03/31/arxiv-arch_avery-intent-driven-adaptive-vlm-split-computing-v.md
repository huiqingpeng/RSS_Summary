---
title: "AVERY: Intent-Driven Adaptive VLM Split Computing via Embodied Self-Awareness for Efficient Disaster Response Systems"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2511.18151"
published: "2026-03-31"
fetched: "2026-04-01T07:17:22.093286"
---

Computer Science > Distributed, Parallel, and Cluster Computing
[Submitted on 22 Nov 2025 (v1), last revised 28 Mar 2026 (this version, v3)]
Title:AVERY: Intent-Driven Adaptive VLM Split Computing via Embodied Self-Awareness for Efficient Disaster Response Systems
View PDF HTML (experimental)Abstract:Unmanned Aerial Vehicles (UAVs) in disaster response require complex, queryable intelligence that onboard CNNs cannot provide. While Vision-Language Models (VLMs) offer this semantic reasoning, their high resource demands make on-device deployment infeasible, and naive cloud offloading fails under the low-bandwidth, unstable networks endemic to disaster zones. We present AVERY, an intent-driven adaptive split computing framework for efficient VLM deployment on resource-constrained platforms. AVERY is motivated by the observation that operator intent must be treated as a first-class system objective, since missions such as broad situational monitoring and precise, spatially grounded investigation require different semantic products, latency targets, and resource allocations. To reflect this, AVERY advances split computing beyond traditional depth-wise partitioning through a functional, cognitive-inspired dual-stream split: a high-frequency, low-resolution Context stream for real-time awareness, and a low-frequency, high-fidelity Insight stream for deep analysis. This design enables a hierarchical split strategy: computation is first separated by function, then partitioned depth-wise across edge and cloud when the Insight stream is required. A lightweight, self-aware onboard controller monitors network conditions and operator intent to select from pre-trained compression models, navigating the accuracy-throughput trade-off at runtime. Evaluated using LISA-7B in an edge-cloud setting under fluctuating network conditions, AVERY achieves 11.2% higher accuracy than raw image compression, 93.98% lower energy consumption than full-edge execution, and average accuracy within 0.75% of the static High-Accuracy baseline during dynamic adaptation. Overall, AVERY enhances mission efficiency and enables real-time, queryable intelligence in dynamic disaster environments.
Submission history
From: Rajat Bhattacharjya [view email][v1] Sat, 22 Nov 2025 18:42:04 UTC (6,160 KB)
[v2] Mon, 2 Feb 2026 09:53:38 UTC (6,210 KB)
[v3] Sat, 28 Mar 2026 02:11:38 UTC (15,743 KB)
Current browse context:
cs.DC
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
