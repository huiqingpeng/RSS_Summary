---
title: "COTONET: A custom cotton detection algorithm based on YOLO11 for stage of growth cotton boll detection"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.11717"
published: "2026-03-20"
fetched: "2026-03-20T16:18:37.907397"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 12 Mar 2026 (v1), last revised 19 Mar 2026 (this version, v2)]
Title:COTONET: A custom cotton detection algorithm based on YOLO11 for stage of growth cotton boll detection
View PDF HTML (experimental)Abstract:Cotton harvesting is a critical phase where cotton capsules are physically manipulated and can lead to fibre degradation. To maintain the highest quality, harvesting methods must emulate delicate manual grasping, to preserve cotton's intrinsic properties. Automating this process requires systems capable of recognising cotton capsules across various phenological stages. To address this challenge, we propose COTONET, an enhanced custom YOLO11 model tailored with attention mechanisms to improve the detection of difficult instances. The architecture incorporates gradients in non-learnable operations to enhance shape and feature extraction. Key architectural modifications include: the replacement of convolutional blocks with Squeeze-and-Exitation blocks, a redesigned backbone integrating attention mechanisms, and the substitution of standard upsampling operations for Content Aware Reassembly of Features (CARAFE). Additionally, we integrate Simple Attention Modules (SimAM) for primary feature aggregation and Parallel Hybrid Attention Mechanisms (PHAM) for channel-wise, spatial-wise and coordinate-wise attention in the downward neck path. This configuration offers increased flexibility and robustness for interpreting the complexity of cotton crop growth. COTONET aligns with small-to-medium YOLO models utilizing 7.6M parameters and 27.8 GFLOPS, making it suitable for low-resource edge computing and mobile robotics. COTONET outperforms the standard YOLO baselines, achieving a mAP50 of 81.1% and a mAP50-95 of 60.6%.
Submission history
From: Guillem González [view email][v1] Thu, 12 Mar 2026 09:22:48 UTC (23,757 KB)
[v2] Thu, 19 Mar 2026 16:01:26 UTC (26,729 KB)
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
