---
title: "AdapTS: Lightweight Teacher-Student Approach for Multi-Class and Continual Visual Anomaly Detection"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17530"
published: "2026-03-19"
fetched: "2026-03-19T15:12:47.905542"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:AdapTS: Lightweight Teacher-Student Approach for Multi-Class and Continual Visual Anomaly Detection
View PDF HTML (experimental)Abstract:Visual Anomaly Detection (VAD) is crucial for industrial inspection, yet most existing methods are limited to single-category scenarios, failing to address the multi-class and continual learning demands of real-world environments. While Teacher-Student (TS) architectures are efficient, they remain unexplored for the Continual Setting. To bridge this gap, we propose AdapTS, a unified TS framework designed for multi-class and continual settings, optimized for edge deployment. AdapTS eliminates the need for two different architectures by utilizing a single shared frozen backbone and injecting lightweight trainable adapters into the student pathway. Training is enhanced via a segmentation-guided objective and synthetic Perlin noise, while a prototype-based task identification mechanism dynamically selects adapters at inference with 99\% accuracy.
Experiments on MVTec AD and VisA demonstrate that AdapTS matches the performance of existing TS methods across multi-class and continual learning scenarios, while drastically reducing memory overhead. Our lightest variant, AdapTS-S, requires only 8 MB of additional memory, 13x less than STFPM (95 MB), 48x less than RD4AD (360 MB), and 149x less than DeSTSeg (1120 MB), making it a highly scalable solution for edge deployment in complex industrial environments.
Submission history
From: Davide Dalle Pezze [view email][v1] Wed, 18 Mar 2026 09:39:03 UTC (950 KB)
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
