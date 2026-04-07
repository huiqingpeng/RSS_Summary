---
title: "ViBA: Implicit Bundle Adjustment with Geometric and Temporal Consistency for Robust Visual Matching"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2604.03377"
published: "2026-04-07"
fetched: "2026-04-08T07:02:54.284857"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 3 Apr 2026]
Title:ViBA: Implicit Bundle Adjustment with Geometric and Temporal Consistency for Robust Visual Matching
View PDF HTML (experimental)Abstract:Most existing image keypoint detection and description methods rely on datasets with accurate pose and depth annotations, limiting scalability and generalization, and often degrading navigation and localization performance. We propose ViBA, a sustainable learning framework that integrates geometric optimization with feature learning for continuous online training on unconstrained video streams. Embedded in a standard visual odometry pipeline, it consists of an implicitly differentiable geometric residual framework: (i) an initial tracking network for inter-frame correspondences, (ii) depth-based outlier filtering, and (iii) differentiable global bundle adjustment that jointly refines camera poses and feature positions by minimizing reprojection errors. By combining geometric consistency from BA with long-term temporal consistency across frames, ViBA enforces stable and accurate feature representations. We evaluate ViBA on EuRoC and UMA datasets. Compared with state-of-the-art methods such as SuperPoint+SuperGlue, ALIKED, and LightGlue, ViBA reduces mean absolute translation error (ATE) by 12-18% and absolute rotation error (ARE) by 5-10% across sequences, while maintaining real-time inference speeds (FPS 36-91). When evaluated on unseen sequences, it retains over 90% localization accuracy, demonstrating robust generalization. These results show that ViBA supports continuous online learning with geometric and temporal consistency, consistently improving navigation and localization in real-world scenarios.
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
ScienceCast (What is ScienceCast?)
Demos
Recommenders and Search Tools
Influence Flower (What are Influence Flowers?)
CORE Recommender (What is CORE?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
