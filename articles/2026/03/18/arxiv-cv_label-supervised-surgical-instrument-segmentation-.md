---
title: "Label-supervised surgical instrument segmentation using temporal equivariance and semantic continuity"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2403.09551"
published: "2026-03-18"
fetched: "2026-03-18T18:24:22.814334"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 14 Mar 2024 (v1), last revised 17 Mar 2026 (this version, v3)]
Title:Label-supervised surgical instrument segmentation using temporal equivariance and semantic continuity
View PDF HTML (experimental)Abstract:For robotic surgical videos, instrument presence annotations are typically recorded with video streams, which offering the potential to reduce the manually annotated costs for segmentation. However, weakly supervised surgical instrument segmentation with only instrument presence labels has been rarely explored in surgical domain due to the highly under-constrained challenges. Temporal properties can enhance representation learning by capturing sequential dependencies and patterns over time even in incomplete supervision situations. From this, we take the inherent temporal attributes of surgical video into account and extend a two-stage weakly supervised segmentation paradigm from different perspectives. Firstly, we make temporal equivariance constraint to enhance pixel-wise temporal consistency between adjacent features. Secondly, we constrain class-aware semantic continuity between global and local regions across temporal dimension. Finally, we generate temporal-enhanced pseudo masks from consecutive frames to suppress irrelevant regions. Extensive experiments are validated on two surgical video datasets, including one cholecystectomy surgery benchmark and one real robotic left lateral segment liver surgery dataset. We annotate instance-wise instrument labels with fixed time-steps which are double checked by a clinician with 3-years experience to evaluate segmentation results. Experimental results demonstrate the promising performances of our method, which consistently achieves comparable or favorable results with previous state-of-the-art approaches.
Submission history
From: Qiyuan Wang [view email][v1] Thu, 14 Mar 2024 16:39:11 UTC (9,656 KB)
[v2] Mon, 30 Sep 2024 07:46:29 UTC (4,850 KB)
[v3] Tue, 17 Mar 2026 02:48:21 UTC (3,211 KB)
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
