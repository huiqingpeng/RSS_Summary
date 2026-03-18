---
title: "Few-Shot Video Object Segmentation in X-Ray Angiography Using Local Matching and Spatio-Temporal Consistency Loss"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2601.00988"
published: "2026-03-18"
fetched: "2026-03-18T18:31:38.212328"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 2 Jan 2026 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:Few-Shot Video Object Segmentation in X-Ray Angiography Using Local Matching and Spatio-Temporal Consistency Loss
View PDF HTML (experimental)Abstract:We introduce a novel FSVOS model that employs a local matching strategy to restrict the search space to the most relevant neighboring pixels. Rather than relying on inefficient standard im2col-like implementations (e.g., spatial convolutions, depthwise convolutions and feature-shifting mechanisms) or hardware-specific CUDA kernels (e.g., deformable and neighborhood attention), which often suffer from limited portability across non-CUDA devices, we reorganize the local sampling process through a direction-based sampling perspective. Specifically, we implement a non-parametric sampling mechanism that enables dynamically varying sampling regions. This approach provides the flexibility to adapt to diverse spatial structures without the computational costs of parametric layers and the need for model retraining. To further enhance feature coherence across frames, we design a supervised spatio-temporal contrastive learning scheme that enforces consistency in feature representations. In addition, we introduce a publicly available benchmark dataset for multi-object segmentation in X-ray angiography videos (MOSXAV), featuring detailed, manually labeled segmentation ground truth. Extensive experiments on the CADICA, XACV, and MOSXAV datasets show that our proposed FSVOS method outperforms current state-of-the-art video segmentation methods in terms of segmentation accuracy and generalization capability (i.e., seen and unseen categories). This work offers enhanced flexibility and potential for a wide range of clinical applications. Code is available at this https URL
Submission history
From: Lin Xi [view email][v1] Fri, 2 Jan 2026 21:26:28 UTC (17,842 KB)
[v2] Tue, 17 Mar 2026 11:31:45 UTC (17,843 KB)
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
