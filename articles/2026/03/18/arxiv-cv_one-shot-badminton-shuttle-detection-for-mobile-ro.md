---
title: "One-Shot Badminton Shuttle Detection for Mobile Robots"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.06691"
published: "2026-03-18"
fetched: "2026-03-18T19:03:12.082351"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 4 Mar 2026 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:One-Shot Badminton Shuttle Detection for Mobile Robots
View PDF HTML (experimental)Abstract:This paper presents a robust one-shot badminton shuttlecock detection framework for non-stationary robots. To address the lack of egocentric shuttlecock detection datasets, we introduce a dataset of 20,510 semi-automatically annotated frames captured across 11 distinct backgrounds in diverse indoor and outdoor environments, and categorize each frame into one of three difficulty levels. For labeling, we present a novel semi-automatic annotation pipeline, that enables efficient labeling from stationary camera footage. We propose a metric suited to our downstream use case and fine-tune a YOLOv8 network optimized for real-time shuttlecock detection, achieving an F1-score of 0.86 under our metric in test environments similar to training, and 0.70 in entirely unseen environments. Our analysis reveals that detection performance is critically dependent on shuttlecock size and background texture complexity. Qualitative experiments confirm their applicability to robots with moving cameras. Unlike prior work with stationary camera setups, our detector is specifically designed for the egocentric, dynamic viewpoints of mobile robots, providing a foundational building block for downstream tasks, including tracking, trajectory estimation, and system (re)-initialization.
Submission history
From: Florentin Dipner [view email][v1] Wed, 4 Mar 2026 11:47:50 UTC (23,284 KB)
[v2] Tue, 17 Mar 2026 13:59:25 UTC (23,284 KB)
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
