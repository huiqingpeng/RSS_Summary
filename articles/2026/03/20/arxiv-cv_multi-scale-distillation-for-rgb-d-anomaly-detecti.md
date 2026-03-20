---
title: "Multi-Scale Distillation for RGB-D Anomaly Detection on the PD-REAL Dataset"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2311.04095"
published: "2026-03-20"
fetched: "2026-03-20T16:09:48.541790"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 7 Nov 2023 (v1), last revised 19 Mar 2026 (this version, v3)]
Title:Multi-Scale Distillation for RGB-D Anomaly Detection on the PD-REAL Dataset
View PDF HTML (experimental)Abstract:We present PD-REAL, a novel large-scale dataset for unsupervised anomaly detection (AD) in the 3D domain. It is motivated by the fact that 2D-only representations in the AD task may fail to capture the geometric structures of anomalies due to uncertainty in lighting conditions or shooting angles. PD-REAL consists entirely of Play-Doh models for 15 object categories and focuses on the analysis of potential benefits from 3D information in a controlled environment. Specifically, objects are first created with six types of anomalies, such as \textit{dent}, \textit{crack}, or \textit{perforation}, and then photographed under different lighting conditions to mimic real-world inspection scenarios. To demonstrate the usefulness of 3D information, we use a commercially available RealSense camera to capture RGB and depth images. Compared to the existing 3D dataset for AD tasks, the data acquisition of PD-REAL is significantly cheaper, easily scalable, and easier to control variables. Furthermore, we introduce a multi-scale teacher--student framework with hierarchical distillation for multimodal anomaly detection. This architecture overcomes the inherent limitation of single-scale distillation approaches, which often struggle to reconcile global context with local features. Leveraging multi-level guidance from the teacher network, the student network can effectively capture richer features for anomaly detection. Extensive evaluations with our method and state-of-the-art AD algorithms on our dataset qualitatively and quantitatively demonstrate the higher detection accuracy of our method. Our dataset can be downloaded from this https URL
Submission history
From: Chao Zhang [view email][v1] Tue, 7 Nov 2023 16:05:27 UTC (41,092 KB)
[v2] Sun, 8 Mar 2026 11:45:32 UTC (2,151 KB)
[v3] Thu, 19 Mar 2026 14:29:17 UTC (2,151 KB)
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
