---
title: "Hi-GMAE: Hierarchical Graph Masked Autoencoders"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2405.10642"
published: "2026-03-19"
fetched: "2026-03-19T13:17:49.944067"
---

Computer Science > Machine Learning
[Submitted on 17 May 2024 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:Hi-GMAE: Hierarchical Graph Masked Autoencoders
View PDF HTML (experimental)Abstract:Graph Masked Autoencoders (GMAEs) have emerged as a notable self-supervised learning approach for graph-structured data. Existing GMAE models primarily focus on reconstructing node-level information, categorizing them as single-scale GMAEs. This methodology, while effective in certain contexts, tends to overlook the complex hierarchical structures inherent in many real-world graphs. For instance, molecular graphs exhibit a clear hierarchical organization in the form of the atoms-functional groups-molecules structure. Therefore, the inability of single-scale GMAE models to incorporate these hierarchical relationships often results in an inadequate capture of crucial high-level graph information, leading to a noticeable decline in performance. To address this limitation, we propose Hierarchical Graph Masked AutoEncoders (Hi-GMAE), a novel multi-scale GMAE framework designed to handle the hierarchical structures within graphs. First, Hi-GMAE constructs a multi-scale graph hierarchy through graph pooling, enabling the exploration of graph structures across different granularity levels. To ensure masking uniformity of subgraphs across these scales, we propose a novel coarse-to-fine strategy that initiates masking at the coarsest scale and progressively back-projects the mask to finer scales. Furthermore, we integrate a gradual recovery strategy with the masking process to mitigate the learning challenges posed by completely masked subgraphs. Our experiments on 17 graph datasets, covering two graph learning tasks, consistently demonstrate that Hi-GMAE outperforms 29 state-of-the-art self-supervised competitors in capturing comprehensive graph information.
Submission history
From: Chuang Liu [view email][v1] Fri, 17 May 2024 09:08:37 UTC (1,657 KB)
[v2] Wed, 18 Mar 2026 01:17:37 UTC (545 KB)
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
IArxiv Recommender
(What is IArxiv?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
