---
title: "MedSAD-CLIP: Supervised CLIP with Token-Patch Cross-Attention for Medical Anomaly Detection and Segmentation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17325"
published: "2026-03-19"
fetched: "2026-03-19T15:08:14.289334"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:MedSAD-CLIP: Supervised CLIP with Token-Patch Cross-Attention for Medical Anomaly Detection and Segmentation
View PDF HTML (experimental)Abstract:Medical anomaly detection (MAD) and segmentation play a critical role in assisting clinical diagnosis by identifying abnormal regions in medical images and localizing pathological regions. Recent CLIP-based studies are promising for anomaly detection in zero-/few-shot settings, and typically rely on global representations and weak supervision, often producing coarse localization and limited segmentation quality. In this work, we study supervised adaptation of CLIP for MAD under a realistic clinical setting where a limited yet meaningful amount of labeled abnormal data is available. Our model MedSAD-CLIP leverages fine-grained text-visual cues via the Token-Patch Cross-Attention(TPCA) to improve lesion localization while preserving the generalization capability of CLIP representations. Lightweight image adapters and learnable prompt tokens efficiently adapt the pretrained CLIP encoder to the medical domain while preserving its rich semantic alignment. Furthermore, a Margin-based image-text Contrastive Loss is designed to enhance global feature discrimination between normal and abnormal representations. Extensive experiments on four diverse benchmarks-Brain, Retina, Lung, and Breast datasets-demonstrate the effectiveness of our approach, achieving superior performance in both pixel-level segmentation and image-level classification over state-of-the-art methods. Our results highlight the potential of supervised CLIP adaptation as a unified and scalable paradigm for medical anomaly understanding. Code will be made available at this https URL
Submission history
From: Thuy Tran Truong [view email][v1] Wed, 18 Mar 2026 03:37:44 UTC (1,551 KB)
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
