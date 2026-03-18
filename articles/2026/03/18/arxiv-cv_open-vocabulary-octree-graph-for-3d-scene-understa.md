---
title: "Open-Vocabulary Octree-Graph for 3D Scene Understanding"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2411.16253"
published: "2026-03-18"
fetched: "2026-03-18T18:24:53.546170"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 25 Nov 2024 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:Open-Vocabulary Octree-Graph for 3D Scene Understanding
View PDF HTML (experimental)Abstract:Open-vocabulary 3D scene understanding is indispensable for embodied agents. Recent works leverage pretrained vision-language models (VLMs) for object segmentation and project them to point clouds to build 3D maps. Despite progress, a point cloud is a set of unordered coordinates that requires substantial storage space and does not directly convey occupancy information or spatial relation, making existing methods inefficient for downstream tasks, e.g., path planning and text-based object retrieval. To address these issues, we propose \textbf{Octree-Graph}, a novel scene representation for open-vocabulary 3D scene understanding. Specifically, a Chronological Group-wise Segment Merging (CGSM) strategy and an Instance Feature Aggregation (IFA) algorithm are first designed to get 3D instances and corresponding semantic features. Subsequently, an adaptive-octree structure is developed that stores semantics and depicts the occupancy of an object adjustably according to its shape. Finally, the Octree-Graph is constructed where each adaptive-octree acts as a graph node, and edges describe the spatial relations among nodes. Extensive experiments on various tasks are conducted on several widely-used datasets, demonstrating the versatility and effectiveness of our method. Code is available \href{this https URL}{here}.
Submission history
From: Yifei Su [view email][v1] Mon, 25 Nov 2024 10:14:10 UTC (23,742 KB)
[v2] Tue, 17 Mar 2026 07:34:49 UTC (8,869 KB)
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
