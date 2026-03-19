---
title: "LoGSAM: Parameter-Efficient Cross-Modal Grounding for MRI Segmentation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17576"
published: "2026-03-19"
fetched: "2026-03-19T15:14:15.085545"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:LoGSAM: Parameter-Efficient Cross-Modal Grounding for MRI Segmentation
View PDF HTML (experimental)Abstract:Precise localization and delineation of brain tumors using Magnetic Resonance Imaging (MRI) are essential for planning therapy and guiding surgical decisions. However, most existing approaches rely on task-specific supervised models and are constrained by the limited availability of annotated data. To address this, we propose LoGSAM, a parameter-efficient, detection-driven framework that transforms radiologist dictation into text prompts for foundation-model-based localization and segmentation. Radiologist speech is first transcribed and translated using a pretrained Whisper ASR model, followed by negation-aware clinical NLP to extract tumor-specific textual prompts. These prompts guide text-conditioned tumor localization via a LoRA-adapted vision-language detection model, Grounding DINO (GDINO). The LoRA adaptation updates using 5% of the model parameters, thereby enabling computationally efficient domain adaptation while preserving pretrained cross-modal knowledge. The predicted bounding boxes are used as prompts for MedSAM to generate pixel-level tumor masks without any additional fine-tuning. Conditioning the frozen MedSAM on LoGSAM-derived priors yields a state-of-the-art dice score of 80.32% on BRISC 2025. In addition, we evaluate the full pipeline using German dictations from a board-certified radiologist on 12 unseen MRI scans, achieving 91.7% case-level accuracy. These results highlight the feasibility of constructing a modular, speech-to-segmentation pipeline by intelligently leveraging pretrained foundation models with minimal parameter updates.
Submission history
From: Mohammad Robaitul Islam Bhuiyan [view email][v1] Wed, 18 Mar 2026 10:33:32 UTC (1,026 KB)
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
