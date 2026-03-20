---
title: "Improved Convex Decomposition with Ensembling and Negative Primitives"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2405.19569"
published: "2026-03-20"
fetched: "2026-03-20T16:09:58.561270"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 29 May 2024 (v1), last revised 19 Mar 2026 (this version, v4)]
Title:Improved Convex Decomposition with Ensembling and Negative Primitives
View PDF HTML (experimental)Abstract:Describing a scene in terms of primitives -- geometrically simple shapes that offer a parsimonious but accurate abstraction of structure -- is an established and difficult fitting problem. Different scenes require different numbers of primitives, and these primitives interact strongly. Existing methods are evaluated by comparing predicted depth, normals, and segmentation against ground truth. The state of the art method involves a learned regression procedure to predict a start point consisting of a fixed number of primitives, followed by a descent method to refine the geometry and remove redundant primitives. CSG (Constructive Solid Geometry) representations are significantly enhanced by a set-differencing operation. Our representation incorporates negative primitives, which are differenced from the positive primitives. These notably enrich the geometry that the model can encode, while complicating the fitting problem. This paper presents a method that can (a) incorporate these negative primitives and (b) choose the overall number of positive and negative primitives by ensembling. Extensive experiments on the standard NYUv2 dataset confirm that (a) this approach results in substantial improvements in depth representation and segmentation over SOTA and (b) negative primitives improve fitting accuracy. Our method is robustly applicable across datasets: in a first, we evaluate primitive prediction for LAION images.
Submission history
From: Vaibhav Vavilala [view email][v1] Wed, 29 May 2024 23:24:48 UTC (3,327 KB)
[v2] Sun, 9 Jun 2024 21:06:44 UTC (3,338 KB)
[v3] Tue, 17 Jun 2025 22:49:59 UTC (3,861 KB)
[v4] Thu, 19 Mar 2026 06:48:36 UTC (14,901 KB)
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
