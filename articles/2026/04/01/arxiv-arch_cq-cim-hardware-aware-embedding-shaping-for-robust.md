---
title: "CQ-CiM: Hardware-Aware Embedding Shaping for Robust CiM-Based Retrieval"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2602.20083"
published: "2026-04-01"
fetched: "2026-04-02T07:12:34.401806"
---

Computer Science > Emerging Technologies
[Submitted on 23 Feb 2026 (v1), last revised 31 Mar 2026 (this version, v3)]
Title:CQ-CiM: Hardware-Aware Embedding Shaping for Robust CiM-Based Retrieval
View PDF HTML (experimental)Abstract:Deploying Retrieval-Augmented Generation (RAG) on edge devices is in high demand, but is hindered by the latency of massive data movement and computation on traditional architectures. Compute-in-Memory (CiM) architectures address this bottleneck by performing vector search directly within their crossbar structure. However, CiM's adoption for RAG is limited by a fundamental ``representation gap,'' as high-precision, high-dimension embeddings are incompatible with CiM's low-precision, low-dimension array constraints. This gap is compounded by the diversity of CiM implementations (e.g., SRAM, ReRAM, FeFET), each with unique designs (e.g., 2-bit cells, 512x512 arrays). Consequently, RAG data must be naively reshaped to fit each target implementation. Current data shaping methods handle dimension and precision disjointly, which degrades data fidelity. This not only negates the advantages of CiM for RAG but also confuses hardware designers, making it unclear if a failure is due to the circuit design or the degraded input data. As a result, CiM adoption remains limited. In this paper, we introduce CQ-CiM, a unified, hardware-aware data shaping framework that jointly learns Compression and Quantization to produce CiM-compatible low-bit embeddings for diverse CiM designs. To the best of our knowledge, this is the first work to shape data for comprehensive CiM usage on RAG.
Submission history
From: Ruiyang Qin [view email][v1] Mon, 23 Feb 2026 17:49:10 UTC (1,432 KB)
[v2] Wed, 25 Feb 2026 00:49:38 UTC (1,432 KB)
[v3] Tue, 31 Mar 2026 01:01:54 UTC (1,432 KB)
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
