---
title: "VLM-AutoDrive: Post-Training Vision-Language Models for Safety-Critical Autonomous Driving Events"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18178"
published: "2026-03-20"
fetched: "2026-03-20T15:06:24.474960"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:VLM-AutoDrive: Post-Training Vision-Language Models for Safety-Critical Autonomous Driving Events
View PDF HTML (experimental)Abstract:The rapid growth of ego-centric dashcam footage presents a major challenge for detecting safety-critical events such as collisions and near-collisions, scenarios that are brief, rare, and difficult for generic vision models to capture. While multimodal large language models (MLLMs) demonstrate strong general reasoning ability, they underperform in driving contexts due to domain and temporal misalignment.
We introduce VLM-AutoDrive, a modular post-training framework for adapting pretrained Vision-Language Models (VLMs) to high-fidelity anomaly detection. The framework integrates metadata-derived captions, LLM-generated descriptions, visual question answering (VQA) pairs, and chain-of-thought (CoT) reasoning supervision to enable domain-aligned and interpretable learning. Off-the-shelf VLMs such as NVIDIA's Cosmos-Reason1 7B (CR1) exhibit near-zero Collision recall in zero-shot settings; fine-tuning with VLM-AutoDrive improves Collision F1 from 0.00 to 0.69 and overall accuracy from 35.35% to 77.27%.
VLM-AutoDrive offers a scalable recipe for adapting general-purpose VLMs to safety-critical, temporally localized perception tasks. Evaluated on real-world Nexar dashcam videos, it achieves substantial gains in Collision and Near-Collision detection while producing interpretable reasoning traces, bridging the gap between perception, causality, and decision reasoning in autonomous driving.
Submission history
From: Mohammad Qazim Bhat [view email][v1] Wed, 18 Mar 2026 18:23:34 UTC (771 KB)
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
