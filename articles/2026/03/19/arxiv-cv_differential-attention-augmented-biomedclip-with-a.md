---
title: "Differential Attention-Augmented BiomedCLIP with Asymmetric Focal Optimization for Imbalanced Multi-Label Video Capsule Endoscopy Classification"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17879"
published: "2026-03-19"
fetched: "2026-03-19T16:17:48.574264"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:Differential Attention-Augmented BiomedCLIP with Asymmetric Focal Optimization for Imbalanced Multi-Label Video Capsule Endoscopy Classification
View PDF HTML (experimental)Abstract:This work presents a multi-label classification framework for video capsule endoscopy (VCE) that addresses the extreme class imbalance inherent in the Galar dataset through a combination of architectural and optimization-level strategies. Our approach modifies BiomedCLIP, a biomedical vision-language foundation model, by replacing its standard multi-head self-attention with a differential attention mechanism that computes the difference between two softmax attention maps to suppress attention noise. To counteract the skewed label distribution, where pathological findings constitute less than 0.1% of all annotated frames, a sqrt-frequency weighted sampler, asymmetric focal loss, mixup regularization, and per-class threshold optimization are employed. Temporal coherence is enforced through median-filter smoothing and gap merging prior to event-level JSON generation. On the held-out RARE-VISION test set comprising three NaviCam examinations (161,025 frames), the pipeline achieves an overall temporal mAP@0.5 of 0.2456 and mAP@0.95 of 0.2353, with total inference completed in approximately 8.6 minutes on a single GPU.
Submission history
From: Podakanti Satyajith Chary [view email][v1] Wed, 18 Mar 2026 16:04:50 UTC (126 KB)
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
