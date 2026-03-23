---
title: "Agile TLB Prefetching and Prediction Replacement Policy"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2412.17203"
published: "2026-03-23"
fetched: "2026-03-24T07:14:28.183690"
---

Computer Science > Hardware Architecture
[Submitted on 23 Dec 2024 (v1), last revised 19 Mar 2026 (this version, v2)]
Title:Agile TLB Prefetching and Prediction Replacement Policy
View PDF HTML (experimental)Abstract:Virtual-to-physical address translation is a critical performance bottleneck in paging-based virtual memory systems. The Translation Lookaside Buffer (TLB) accelerates address translation by caching frequently accessed mappings, but TLB misses lead to costly page walks. Hardware and software techniques address this challenge. Hardware approaches enhance TLB reach through system-level support, while software optimizations include TLB prefetching, replacement policies, superpages, and page size adjustments. Prefetching Page Table Entries (PTEs) for future accesses reduces bottlenecks but may incur overhead from incorrect predictions. Integrating an Agile TLB Prefetcher (ATP) with SBFP optimizes performance by leveraging page table locality and dynamically identifying essential free PTEs during page walks. Predictive replacement policies further improve TLB performance. Traditional LRU replacement is limited to near-instant references, while advanced policies like SRRIP, GHRP, SHiP, SDBP, and CHiRP enhance performance by targeting specific inefficiencies. CHiRP, tailored for L2 TLBs, surpasses other policies by leveraging control flow history to detect dead blocks, utilizing L2 TLB entries for learning instead of sampling. These integrated techniques collectively address key challenges in virtual memory management.
Submission history
From: Melkamu Abay Mersha [view email][v1] Mon, 23 Dec 2024 00:46:53 UTC (413 KB)
[v2] Thu, 19 Mar 2026 22:34:04 UTC (413 KB)
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
