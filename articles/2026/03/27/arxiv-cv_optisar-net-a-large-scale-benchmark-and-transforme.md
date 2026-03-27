---
title: "OptiSAR-Net++: A Large-Scale Benchmark and Transformer-Free Framework for Cross-Domain Remote Sensing Visual Grounding"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.24876"
published: "2026-03-27"
fetched: "2026-03-28T07:18:01.007715"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 25 Mar 2026]
Title:OptiSAR-Net++: A Large-Scale Benchmark and Transformer-Free Framework for Cross-Domain Remote Sensing Visual Grounding
View PDF HTML (experimental)Abstract:Remote sensing visual grounding (RSVG) aims to localize specific targets in remote sensing images using natural language expressions. However, existing methods are restricted to single-sensor domains, i.e., either optical or synthetic aperture radar (SAR), limiting their real-world applicability. In this paper, we introduce the Cross-Domain RSVG (CD-RSVG) task and construct OptSAR-RSVG, the first large-scale benchmark dataset for this setting. To tackle the challenges of cross-domain feature modeling, computational inefficiency, and fine-grained semantic discrimination, we propose OptiSAR-Net++. Our framework features a patch-level Low-Rank Adaptation Mixture of Experts (PL-MoE) for efficient cross-domain feature decoupling. To mitigate the substantial computational overhead of Transformer decoding frameworks, we adopt a CLIP-based contrastive paradigm and further incorporate dynamic adversarial negative sampling, thereby transforming generative regression into an efficient cross-modal matching process. Additionally, a text-guided dual-gate fusion module (TGDF-SSA) and a region-aware auxiliary head are introduced to enhance semantic-visual alignment and spatial modeling. Extensive experiments demonstrate that OptiSAR-Net++ achieves SOTA performance on both OptSAR-RSVG and DIOR-RSVG benchmarks, offering significant advantages in localization accuracy and efficiency. Our code and dataset will be made publicly available.
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
