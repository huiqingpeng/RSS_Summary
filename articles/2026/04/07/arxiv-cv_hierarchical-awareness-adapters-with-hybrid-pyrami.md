---
title: "Hierarchical Awareness Adapters with Hybrid Pyramid Feature Fusion for Dense Depth Prediction"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2604.03339"
published: "2026-04-07"
fetched: "2026-04-08T07:02:52.376779"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 3 Apr 2026]
Title:Hierarchical Awareness Adapters with Hybrid Pyramid Feature Fusion for Dense Depth Prediction
View PDF HTML (experimental)Abstract:Monocular depth estimation from a single RGB image remains a fundamental challenge in computer vision due to inherent scale ambiguity and the absence of explicit geometric cues. Existing approaches typically rely on increasingly complex network architectures to regress depth maps, which escalates training costs and computational overhead without fully exploiting inter-pixel spatial dependencies. We propose a multilevel perceptual conditional random field (CRF) model built upon the Swin Transformer backbone that addresses these limitations through three synergistic innovations: (1) an adaptive hybrid pyramid feature fusion (HPF) strategy that captures both short-range and long-range dependencies by combining multi-scale spatial pyramid pooling with biaxial feature aggregation, enabling effective integration of global and local contextual information; (2) a hierarchical awareness adapter (HA) that enriches cross-level feature interactions within the encoder through lightweight broadcast modules with learnable dimensional scaling, reducing computational complexity while enhancing representational capacity; and (3) a fully-connected CRF decoder with dynamic scaling attention that models fine-grained pixel-level spatial relationships, incorporating a bias learning unit to prevent extreme-value collapse and ensure stable training. Extensive experiments on NYU Depth v2, KITTI, and MatterPort3D datasets demonstrate that our method achieves state-of-the-art performance, reducing Abs Rel to 0.088 ($-$7.4\%) and RMSE to 0.316 ($-$5.4\%) on NYU Depth v2, while attaining near-perfect threshold accuracy ($\delta < 1.25^3 \approx 99.8\%$) on KITTI with only 194M parameters and 21ms inference time.
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
