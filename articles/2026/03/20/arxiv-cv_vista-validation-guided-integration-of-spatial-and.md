---
title: "VISTA: Validation-Guided Integration of Spatial and Temporal Foundation Models with Anatomical Decoding for Rare-Pathology VCE Event Detection"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18343"
published: "2026-03-20"
fetched: "2026-03-20T15:07:27.505624"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:VISTA: Validation-Guided Integration of Spatial and Temporal Foundation Models with Anatomical Decoding for Rare-Pathology VCE Event Detection
View PDF HTML (experimental)Abstract:Capsule endoscopy event detection is challenging because diagnostically relevant findings are sparse, visually heterogeneous, and embedded in long, noisy video streams, while evaluation is performed at the event level rather than by frame accuracy alone. We therefore formulate the RARE-VISION task as a metric-aligned event detection problem instead of a purely frame-wise classification task. Our framework combines two complementary backbones, EndoFM-LV for local temporal context and DINOv3 ViT-L/16 for strong frame-level visual semantics, followed by a Diverse Head Ensemble, Validation-Guided Hierarchical Fusion, and Anatomy-Aware Temporal Event Decoding. The fusion stage uses validation-derived class-wise model weighting, backbone weighting, and probability calibration, while the decoding stage applies temporal smoothing, anatomical constraints, threshold refinement, and per-label event generation to produce stable event predictions. Validation ablations indicate that complementary backbones, validation-guided fusion, and anatomy-aware temporal decoding all contribute to event-level performance. On the official hidden test set, the proposed method achieved an overall temporal mAP@0.5 of 0.3530 and temporal mAP@0.95 of 0.3235.
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
