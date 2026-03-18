---
title: "Topology-Preserving Data Augmentation for Ring-Type Polygon Annotations"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.14764"
published: "2026-03-18"
fetched: "2026-03-18T17:16:48.732609"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 16 Mar 2026 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:Topology-Preserving Data Augmentation for Ring-Type Polygon Annotations
View PDF HTML (experimental)Abstract:Geometric data augmentation is widely used in segmentation pipelines and typically assumes that polygon annotations represent simply connected regions. However, in structured domains such as architectural floorplan analysis, ring-type regions are often encoded as a single cyclic polygon chain connecting outer and inner boundaries. During augmentation, clipping operations may remove intermediate vertices and disrupt this cyclic connectivity, breaking the structural relationship between the boundaries. In this work, we introduce an order-preserving polygon augmentation strategy that performs transformations in mask space and then projects surviving vertices back into index-space to restore adjacency relations. This repair maintains the original traversal order of the polygon and preserves topological consistency with minimal computational overhead. Experiments demonstrate that the approach reliably restores connectivity, achieving near-perfect Cyclic Adjacency Preservation (CAP) across both single and compound augmentations.
Submission history
From: Sudip Laudari [view email][v1] Mon, 16 Mar 2026 02:53:37 UTC (6,313 KB)
[v2] Tue, 17 Mar 2026 04:01:44 UTC (6,314 KB)
Current browse context:
cs.CV
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
