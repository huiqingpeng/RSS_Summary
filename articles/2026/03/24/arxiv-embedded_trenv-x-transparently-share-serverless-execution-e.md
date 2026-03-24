---
title: "TrEnv-X: Transparently Share Serverless Execution Environments Across Different Functions and Nodes"
source: "arXiv Embedded Systems"
url: "https://arxiv.org/abs/2509.09525"
published: "2026-03-24"
fetched: "2026-03-25T07:06:17.638073"
---

Computer Science > Distributed, Parallel, and Cluster Computing
[Submitted on 11 Sep 2025 (v1), last revised 21 Mar 2026 (this version, v2)]
Title:TrEnv-X: Transparently Share Serverless Execution Environments Across Different Functions and Nodes
View PDF HTML (experimental)Abstract:Serverless computing is renowned for its computation elasticity, yet its full potential is often constrained by the requirement for functions to operate within local and dedicated background environments, resulting in limited memory elasticity. To address this limitation, this paper introduces TrEnv-X, a co-designed integration of the serverless platform with the operating system and CXL/RDMA-based remote memory pools. TrEnv-X's core innovations are repurposable sandboxes, which can be shared across different functions to decrease the associated creation overhead, and OS-level memory templates, which enable rapid state restoration from CXL/RDMA-based remote memory pools. To further demonstrate TrEnv-X's versatility, we generalize its design from traditional containers for microVM-based agent workloads and introduce new optimizations, including browser sharing and a page cache bypassing mechanism. Our evaluation shows that TrEnv-X achieves up to 7x reduction in P99 latency and 48% memory savings for container-based functions. When applied to LLM agents, it reduces the P99 latency by up to 58% and memory usage by 61% compared to state-of-the-art systems like E2B.
Submission history
From: Jialiang Huang [view email][v1] Thu, 11 Sep 2025 15:06:03 UTC (1,429 KB)
[v2] Sat, 21 Mar 2026 12:02:04 UTC (1,623 KB)
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
