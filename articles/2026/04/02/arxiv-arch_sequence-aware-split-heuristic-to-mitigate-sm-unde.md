---
title: "Sequence-Aware Split Heuristic to Mitigate SM Underutilization in FlashAttention-3 Low-Head-Count Decoding"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2604.00028"
published: "2026-04-02"
fetched: "2026-04-03T07:14:37.389898"
---

Computer Science > Hardware Architecture
[Submitted on 19 Mar 2026]
Title:Sequence-Aware Split Heuristic to Mitigate SM Underutilization in FlashAttention-3 Low-Head-Count Decoding
View PDF HTML (experimental)Abstract:The standard FlashAttention-3 heuristic exhibits a GPU occupancy bottleneck in low-head-count decoding configurations because it disables sequence splitting based on sequence length alone, underutilizing the Streaming Multiprocessors of Hopper GPUs. Our proposed sequence-aware split policy mitigates this by allowing sequence-level parallelism in low-head-count regimes, improving hardware utilization to deliver roughly a 21 to 24% improvement in decoder kernel efficiency on metadata-enabled inference paths, with no observed regressions.
Submission history
From: Martí Llopart Font [view email][v1] Thu, 19 Mar 2026 11:44:20 UTC (106 KB)
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
