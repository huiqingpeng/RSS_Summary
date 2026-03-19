---
title: "YOLO26: An Analysis of NMS-Free End to End Framework for Real-Time Object Detection"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2601.12882"
published: "2026-03-19"
fetched: "2026-03-19T16:30:06.615048"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 19 Jan 2026 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:YOLO26: An Analysis of NMS-Free End to End Framework for Real-Time Object Detection
View PDF HTML (experimental)Abstract:The ``You Only Look Once'' (YOLO) framework has long served as a standard for real-time object detection, though traditional iterations have utilized Non-Maximum Suppression (NMS) post-processing, which introduces specific latency and hyperparameter variables. This paper presents a comprehensive architectural analysis of YOLO26, a model that shifts toward a native end-to-end learning strategy by eliminating NMS. This study examines the core mechanisms driving this framework: the MuSGD optimizer for backbone stabilization, Small-Target-Aware Label Assignment (STAL), and ProgLoss for dynamic supervision. To contextualize its performance, this article reviews exhaustive benchmark data from the COCO \texttt{val2017} leaderboard. This evaluation provides an objective comparison of YOLO26 across various model scales (Nano to Extra-Large) against both prior CNN lineages and contemporary Transformer-based architectures (e.g., RT-DETR, DEIM, RF-DETR), detailing the observed speed-accuracy trade-offs and parameter requirements without asserting a singular optimal model. Additionally, the analysis covers the framework's unified multi-task capabilities, including the YOLOE-26 open-vocabulary module for promptable detection. Ultimately, this paper serves to document how decoupling representation learning from heuristic post-processing impacts the "Export Gap" and deterministic latency in modern edge-based computer vision deployments.
Submission history
From: Sudip Chakrabarty [view email][v1] Mon, 19 Jan 2026 09:36:08 UTC (2,704 KB)
[v2] Wed, 18 Mar 2026 14:50:45 UTC (3,638 KB)
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
