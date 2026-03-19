---
title: "Feeling the Space: Egomotion-Aware Video Representation for Efficient and Accurate 3D Scene Understanding"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17980"
published: "2026-03-19"
fetched: "2026-03-19T16:19:54.501656"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:Feeling the Space: Egomotion-Aware Video Representation for Efficient and Accurate 3D Scene Understanding
View PDF HTML (experimental)Abstract:Recent Multimodal Large Language Models (MLLMs) have shown high potential for spatial reasoning within 3D scenes. However, they typically rely on computationally expensive 3D representations like point clouds or reconstructed Bird's-Eye View (BEV) maps, or lack physical grounding to resolve ambiguities in scale and size. This paper significantly enhances MLLMs with egomotion modality data, captured by Inertial Measurement Units (IMUs) concurrently with the video. In particular, we propose a novel framework, called Motion-MLLM, introducing two key components: (1) a cascaded motion-visual keyframe filtering module that leverages both IMU data and visual features to efficiently select a sparse yet representative set of keyframes, and (2) an asymmetric cross-modal fusion module where motion tokens serve as intermediaries that channel egomotion cues and cross-frame visual context into the visual representation. By grounding visual content in physical egomotion trajectories, Motion-MLLM can reason about absolute scale and spatial relationships across the scene. Our extensive evaluation shows that Motion-MLLM makes significant improvements in various tasks related to 3D scene understanding and spatial reasoning. Compared to state-of-the-art (SOTA) methods based on video frames and explicit 3D data, Motion-MLLM exhibits similar or even higher accuracy with significantly less overhead (i.e., 1.40$\times$ and 1.63$\times$ higher cost-effectiveness, respectively).
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
