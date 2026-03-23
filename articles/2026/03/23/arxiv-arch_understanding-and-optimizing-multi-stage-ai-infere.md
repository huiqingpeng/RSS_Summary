---
title: "Understanding and Optimizing Multi-Stage AI Inference Pipelines"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2504.09775"
published: "2026-03-23"
fetched: "2026-03-24T07:14:36.271756"
---

Computer Science > Hardware Architecture
[Submitted on 14 Apr 2025 (v1), last revised 20 Mar 2026 (this version, v5)]
Title:Understanding and Optimizing Multi-Stage AI Inference Pipelines
View PDFAbstract:The rapid evolution of Large Language Models (LLMs) has driven the need for increasingly sophisticated inference pipelines and hardware platforms. Modern LLM serving extends beyond traditional prefill-decode workflows, incorporating multi-stage processes such as Retrieval Augmented Generation (RAG), key-value (KV) cache retrieval, dynamic model routing, and multi step reasoning. These stages exhibit diverse computational demands, requiring distributed systems that integrate GPUs, ASICs, CPUs, and memory-centric architectures. However, existing simulators lack the fidelity to model these heterogeneous, multi-engine workflows, limiting their ability to inform architectural decisions.
To address this gap, we introduce MIST, a Heterogeneous Multi-stage LLM inference Execution Simulator. MIST models diverse request stages; including RAG, KV retrieval, reasoning, prefill, and decode across complex hardware hierarchies. MIST supports heterogeneous clients executing multiple models concurrently unlike prior frameworks while incorporating advanced batching strategies and multi-level memory hierarchies. By integrating real hardware traces with analytical modeling, MIST captures critical trade-offs such as memory bandwidth contention, inter-cluster communication latency, and batching efficiency in hybrid CPU-accelerator deployments. Through case studies, we explore the impact of reasoning stages on end-to-end latency, optimal batching strategies for hybrid pipelines, and the architectural implications of remote KV cache retrieval. MIST empowers system designers to navigate the evolving landscape of LLM inference, providing actionable insights into optimizing hardware-software co-design for next-generation AI workloads.
Submission history
From: Abhimanyu Rajeshkumar Bambhaniya [view email][v1] Mon, 14 Apr 2025 00:29:49 UTC (2,750 KB)
[v2] Wed, 16 Apr 2025 17:34:04 UTC (2,750 KB)
[v3] Sun, 20 Apr 2025 19:57:16 UTC (2,750 KB)
[v4] Tue, 25 Nov 2025 04:36:10 UTC (3,041 KB)
[v5] Fri, 20 Mar 2026 16:55:01 UTC (3,041 KB)
Current browse context:
cs.AR
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
