---
title: "GateANN: I/O-Efficient Filtered Vector Search on SSDs"
source: "arXiv Embedded Systems"
url: "https://arxiv.org/abs/2603.21466"
published: "2026-03-24"
fetched: "2026-03-25T07:06:12.549379"
---

Computer Science > Operating Systems
[Submitted on 23 Mar 2026]
Title:GateANN: I/O-Efficient Filtered Vector Search on SSDs
View PDF HTML (experimental)Abstract:We present GateANN, an I/O-efficient SSD-based graph ANNS system that supports filtered vector search on an unmodified graph index. Existing SSD-based systems either waste I/O by post-filtering, or require expensive filter-aware index rebuilds. GateANN avoids both by decoupling graph traversal from vector retrieval. Our key insight is that traversing a node requires only its neighbor list and an approximate distance, neither of which needs the full-precision vector on SSD. Based on this, GateANN introduces graph tunneling. It checks each node's filter predicate in memory before issuing I/O and routes through non-matching nodes entirely in memory, preserving graph connectivity without any SSD read for non-matching nodes. Our experimental results show that it reduces SSD reads by up to 10x and improves throughput by up to 7.6x.
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
