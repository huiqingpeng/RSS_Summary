---
title: "ELiC: Efficient LiDAR Geometry Compression via Cross-Bit-depth Feature Propagation and Bag-of-Encoders"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2511.14070"
published: "2026-03-20"
fetched: "2026-03-20T17:04:17.681104"
---

Electrical Engineering and Systems Science > Image and Video Processing
[Submitted on 18 Nov 2025 (v1), last revised 19 Mar 2026 (this version, v2)]
Title:ELiC: Efficient LiDAR Geometry Compression via Cross-Bit-depth Feature Propagation and Bag-of-Encoders
View PDF HTML (experimental)Abstract:Hierarchical LiDAR geometry compression encodes voxel occupancies from low to high bit-depths, yet prior methods treat each depth independently and re-estimate local context from coordinates at every level, limiting compression efficiency. We present ELiC, a real-time framework that combines cross-bit-depth feature propagation, a Bag-of-Encoders (BoE) selection scheme, and a Morton-order-preserving hierarchy. Cross-bit-depth propagation reuses features extracted at denser, lower depths to support prediction at sparser, higher depths. BoE selects, per depth, the most suitable coding network from a small pool, adapting capacity to observed occupancy statistics without training a separate model for each level. The Morton hierarchy maintains global Z-order across depth transitions, eliminating per-level sorting and reducing latency. Together these components improve entropy modeling and computation efficiency, yielding state-of-the-art compression at real-time throughput on Ford and SemanticKITTI. Code and pretrained models are available at this https URL.
Submission history
From: Soowoong Kim [view email][v1] Tue, 18 Nov 2025 02:58:16 UTC (42,108 KB)
[v2] Thu, 19 Mar 2026 03:59:33 UTC (42,080 KB)
Current browse context:
eess.IV
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
