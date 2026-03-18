---
title: "MorphSeek: Fine-grained Latent Representation-Level Policy Optimization for Deformable Image Registration"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2511.17392"
published: "2026-03-18"
fetched: "2026-03-18T18:29:01.249643"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 21 Nov 2025 (v1), last revised 16 Mar 2026 (this version, v2)]
Title:MorphSeek: Fine-grained Latent Representation-Level Policy Optimization for Deformable Image Registration
View PDF HTML (experimental)Abstract:Deformable image registration (DIR) remains a fundamental yet challenging problem in medical image analysis, largely due to the prohibitively high-dimensional deformation space of dense displacement fields and the scarcity of voxel-level supervision. Existing reinforcement learning frameworks often project this space into coarse, low-dimensional representations, limiting their ability to capture spatially variant deformations. We propose MorphSeek, a fine-grained representation-level policy optimization paradigm that reformulates DIR as a spatially continuous optimization process in the latent feature space. MorphSeek introduces a stochastic Gaussian policy head atop the encoder to model a distribution over latent features, facilitating efficient exploration and coarse-to-fine refinement. The framework integrates unsupervised warm-up with weakly supervised fine-tuning through Group Relative Policy Optimization, where multi-trajectory sampling stabilizes training and improves label efficiency. Across three 3D registration benchmarks (OASIS brain MRI, LiTS liver CT, and Abdomen MR-CT), MorphSeek achieves consistent Dice improvements over competitive baselines while maintaining high label efficiency with minimal parameter cost and low step-level latency overhead. Beyond optimizer specifics, MorphSeek advances a representation-level policy learning paradigm that achieves spatially coherent and data-efficient deformation optimization, offering a principled, backbone-agnostic, and optimizer-agnostic solution for scalable visual alignment in high-dimensional settings.
Submission history
From: Runxun Zhang [view email][v1] Fri, 21 Nov 2025 16:52:20 UTC (2,964 KB)
[v2] Mon, 16 Mar 2026 19:59:55 UTC (8,085 KB)
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
