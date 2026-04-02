---
title: "Improving Instruction Fetch Efficiency via High-Level Program Map Traversal"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2406.06738"
published: "2026-04-02"
fetched: "2026-04-03T07:15:26.653815"
---

Computer Science > Hardware Architecture
[Submitted on 10 Jun 2024 (v1), last revised 31 Mar 2026 (this version, v2)]
Title:Improving Instruction Fetch Efficiency via High-Level Program Map Traversal
View PDF HTML (experimental)Abstract:Efficiency in instruction fetching is critical to performance, and this requires the primary structures--L1 instruction caches (L1i), branch target buffers (BTB) and instruction TLBs (iTLB)--to have the requisite information when needed. This paper proposes instruction presending, which traverses a high-level program map to identify and move instruction cache blocks, BTB entries, and iTLB entries from the secondary to the primary structures in a "just in time" fashion.
Empirical results are presented to demonstrate the efficacy of the proposed presending scheme. Presending reduces the number of cycles where the instruction fetch is waiting by an order of magnitude as compared to state-of-the-art instruction prefetching schemes while operating with small-sized primary BTBs. It is especially effective for benchmarks with a high base MPKI, where movement from secondary to primary structures is frequent. This improvement in fetch efficiency results in performance improvements in cases where this efficiency is important.
Submission history
From: Shyam Murthy [view email][v1] Mon, 10 Jun 2024 18:58:50 UTC (465 KB)
[v2] Tue, 31 Mar 2026 20:44:58 UTC (397 KB)
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
