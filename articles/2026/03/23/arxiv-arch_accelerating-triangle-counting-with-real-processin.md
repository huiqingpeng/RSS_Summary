---
title: "Accelerating Triangle Counting with Real Processing-in-Memory Systems"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2505.04269"
published: "2026-03-23"
fetched: "2026-03-24T07:14:45.550073"
---

Computer Science > Hardware Architecture
[Submitted on 7 May 2025 (v1), last revised 20 Mar 2026 (this version, v2)]
Title:Accelerating Triangle Counting with Real Processing-in-Memory Systems
View PDFAbstract:Triangle Counting (TC) is a procedure that involves enumerating the number of triangles within a graph. It has important applications in numerous fields, such as social or biological network analysis and network security. TC is a memory-bound workload that does not scale efficiently in conventional processor-centric systems due to several memory accesses across large memory regions and low data reuse. However, recent Processing-in-Memory (PIM) architectures present a promising solution to alleviate these bottlenecks. Our work presents the first TC algorithm that leverages the capabilities of the UPMEM system, the first commercially available PIM architecture, while at the same time addressing its limitations. We use a vertex coloring technique to avoid expensive communication between PIM cores and employ reservoir sampling to address the limited amount of memory available in the PIM cores' DRAM banks. In addition, our work makes use of the Misra-Gries summary to speed up counting triangles on graphs with high-degree nodes and uniform sampling of the graph edges for quicker approximate results. Our PIM implementation surpasses state-of-the-art CPU-based TC implementations when processing dynamic graphs in Coordinate List format, showcasing the effectiveness of the UPMEM architecture in addressing TC's memory-bound challenges.
Submission history
From: Francesco Silvestri [view email][v1] Wed, 7 May 2025 09:20:03 UTC (733 KB)
[v2] Fri, 20 Mar 2026 08:24:38 UTC (683 KB)
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
