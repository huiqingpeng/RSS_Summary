---
title: "TR2M: Transferring Monocular Relative Depth to Metric Depth with Language Descriptions and Dual-Level Scale-Oriented Contrast"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2506.13387"
published: "2026-03-20"
fetched: "2026-03-20T16:12:04.561374"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 16 Jun 2025 (v1), last revised 19 Mar 2026 (this version, v2)]
Title:TR2M: Transferring Monocular Relative Depth to Metric Depth with Language Descriptions and Dual-Level Scale-Oriented Contrast
View PDF HTML (experimental)Abstract:This work presents a generalizable framework to transfer relative depth to metric depth. Current monocular depth estimation methods are mainly divided into metric depth estimation (MMDE) and relative depth estimation (MRDE). MMDEs estimate depth in metric scale but are often limited to a specific domain. MRDEs generalize well across different domains, but with uncertain scales which hinders downstream applications. To this end, we aim to build up a framework to solve scale uncertainty and transfer relative depth to metric depth. Previous methods used language as input and estimated two factors for conducting rescaling. Our approach, TR2M, utilizes both text description and image as inputs and estimates two rescale maps to transfer relative depth to metric depth at pixel level. Features from two modalities are fused with a cross-modality attention module to better capture scale information. A strategy is designed to construct and filter confident pseudo metric depth for more comprehensive supervision. We also develop scale-oriented contrastive learning to utilize depth distribution as guidance to enforce the model learning about intrinsic knowledge aligning with the scale distribution. TR2M only exploits a small number of trainable parameters to train on datasets in various domains and experiments not only demonstrate TR2M's great performance in seen datasets but also reveal superior zero-shot capabilities on five unseen datasets. We show the huge potential in pixel-wise transferring relative depth to metric depth with language assistance. (Code is available at: this https URL)
Submission history
From: Beilei Cui [view email][v1] Mon, 16 Jun 2025 11:50:00 UTC (4,843 KB)
[v2] Thu, 19 Mar 2026 06:53:17 UTC (604 KB)
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
