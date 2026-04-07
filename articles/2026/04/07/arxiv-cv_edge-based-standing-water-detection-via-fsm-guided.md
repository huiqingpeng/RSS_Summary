---
title: "Edge-Based Standing-Water Detection via FSM-Guided Tiering and Multi-Model Consensus"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2604.03308"
published: "2026-04-07"
fetched: "2026-04-08T07:02:44.469209"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 31 Mar 2026]
Title:Edge-Based Standing-Water Detection via FSM-Guided Tiering and Multi-Model Consensus
View PDF HTML (experimental)Abstract:Standing water in agricultural fields threatens vehicle mobility and crop health. This paper presents a deployed edge architecture for standing-water detection using Raspberry-Pi-class devices with optional Jetson acceleration. Camera input and environmental sensors (humidity, pressure, temperature) are combined in a finite-state machine (FSM) that acts as the architectural decision engine. The FSM-guided control plane selects between local and offloaded inference tiers, trading accuracy, latency, and energy under intermittent connectivity and motion-dependent compute budgets. A multi-model YOLO ensemble provides image scores, while diurnal-baseline sensor fusion adjusts caution using environmental anomalies. All decisions are logged per frame, enabling bit-identical hardware-in-the-loop replays. Across ten configurations and sensor variants on identical field sequences with frame-level ground truth, we show that the combination of adaptive tiering, multi-model consensus, and diurnal sensor fusion improves flood-detection performance over static local baselines, uses less energy than a naive always-heavy offload policy, and maintains bounded tail latency in a real agricultural setting.
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
