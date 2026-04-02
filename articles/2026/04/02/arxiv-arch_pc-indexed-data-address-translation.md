---
title: "PC-Indexed Data Address Translation"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2408.15878"
published: "2026-04-02"
fetched: "2026-04-03T07:15:44.153206"
---

Computer Science > Hardware Architecture
[Submitted on 28 Aug 2024 (v1), last revised 31 Mar 2026 (this version, v2)]
Title:PC-Indexed Data Address Translation
View PDF HTML (experimental)Abstract:This paper proposes a novel way to assist conventional data address translation. The approach, PC-Indexed Data Address Translation (PCAX), uses the PC of a load instruction, and not a data virtual address, to obtain the page table entry (PTE) for the data accessed by a load instruction. PCAX is intended to be used for a small subset of the static loads in a program. We observe that: (i) a small subset of static loads is responsible for most of the misses in a data translation lookaside buffer (DTLB), and (ii) often a dynamic instance of a static load instruction accesses the same PTE as the last dynamic instance, and consider PCAX for this subset. With PCAX the effective miss rate of a conventional DTLB can be cut down by a factor of 2-3X in many cases, and even more in some cases. PCAX is also beneficial in reducing the number of secondary TLB (STLB) misses. Since the tables used for PCAX can be accessed alongside instruction fetch, they can be slow, yet frequently provide a valid PTE even before the data address calculation. This yields an average performance improvement of 1.7% while reducing data address translation energy by 7% across 84 server traces.
Submission history
From: Shyam Murthy [view email][v1] Wed, 28 Aug 2024 15:48:39 UTC (527 KB)
[v2] Tue, 31 Mar 2026 19:01:30 UTC (353 KB)
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
