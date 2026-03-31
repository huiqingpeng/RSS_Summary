---
title: "Proxima: Near-storage Acceleration for Graph-based Approximate Nearest Neighbor Search in 3D NAND"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2312.04257"
published: "2026-03-31"
fetched: "2026-04-01T07:17:08.140059"
---

Computer Science > Hardware Architecture
[Submitted on 7 Dec 2023 (v1), last revised 29 Mar 2026 (this version, v2)]
Title:Proxima: Near-storage Acceleration for Graph-based Approximate Nearest Neighbor Search in 3D NAND
View PDF HTML (experimental)Abstract:Approximate nearest neighbor search (ANNS) plays an indispensable role in a wide variety of applications, including recommendation systems, information retrieval, and semantic search. Among the cutting-edge ANNS algorithms, graph-based approaches provide superior accuracy and scalability on massive datasets. However, the best-performing graph-based ANN search solutions incur tens of hundreds of memory footprints as well as costly distance computation, thus hindering their efficient deployment at scale. The 3D NAND flash is emerging as a promising device for data-intensive applications due to its high density and nonvolatility. In this work, we present the near-storage processing (NSP)-based ANNS solution Proxima, to accelerate graph-based ANNS with algorithm-hardware co-design in 3D NAND flash. Proxima significantly reduces the complexity of graph search by leveraging the distance approximation and early termination. On top of the algorithmic enhancement, we implement Proxima search algorithm in 3D NAND flash using the heterogeneous integration technique. To maximize 3D NAND's bandwidth utilization, we present customized dataflow and optimized data allocation scheme. Our evaluation results show that: compared to graph ANNS on CPU and GPU, Proxima achieves a magnitude improvement in throughput or energy efficiency. Proxima yields 7x to 13x speedup over existing ASIC designs. Furthermore, Proxima achieves a good balance between accuracy, efficiency and storage density compared to previous NSP-based accelerators.
Submission history
From: Weihong Xu [view email][v1] Thu, 7 Dec 2023 12:32:18 UTC (2,117 KB)
[v2] Sun, 29 Mar 2026 06:34:46 UTC (418 KB)
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
