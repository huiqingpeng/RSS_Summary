---
title: "IBEX: Internal Bandwidth-Efficient Compression Architecture for Scalable CXL Memory Expansion"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.26131"
published: "2026-03-30"
fetched: "2026-03-31T07:16:23.276153"
---

Computer Science > Hardware Architecture
[Submitted on 27 Mar 2026]
Title:IBEX: Internal Bandwidth-Efficient Compression Architecture for Scalable CXL Memory Expansion
View PDF HTML (experimental)Abstract:As the memory channel count is confined by physical dimensions, memory expanders appear to be a promising approach to extending memory capacity and channels by augmenting the existing I/O interface (e.g., PCIe) with memory-semantic protocols like CXL. Unfortunately, the physical constraints of a computing system restrict scalable capacity expansion with memory expanders. In this work, we propose a block-level compression scheme for modern memory expanders, IBEX, to achieve larger effective memory capacity. Given the performance overhead associated with block-level compression algorithms (e.g., LZ77), IBEX employs a promotion-based approach: only cold data is compressed, whereas hot data remains uncompressed. Our key innovation is internal bandwidth-efficient block management that precisely identifies cold pages with minimal metadata access overhead. Still, the promotion-based approach poses several performance-related challenges at the design level. Therefore, we also propose a shadowed promotion scheme that temporarily postpones the deallocation of promoted data, thereby mitigating the performance penalty incurred by demotion (i.e., recompression). Furthermore, we optimize our compression scheme by compacting metadata and co-locating multiple target blocks for efficient bandwidth utilization. Consequently, IBEX achieves an average of 1.28x-1.40x speedups compared to the state-of-the-art promotion-based block-level approaches. We open-source IBEX at this https URL.
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
