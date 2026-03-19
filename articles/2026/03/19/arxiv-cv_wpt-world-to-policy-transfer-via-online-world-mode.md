---
title: "WPT: World-to-Policy Transfer via Online World Model Distillation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2511.20095"
published: "2026-03-19"
fetched: "2026-03-19T16:28:21.177644"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 25 Nov 2025 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:WPT: World-to-Policy Transfer via Online World Model Distillation
View PDF HTML (experimental)Abstract:Recent years have witnessed remarkable progress in world models, which primarily aim to capture the spatio-temporal correlations between an agent's actions and the evolving environment. However, existing approaches often suffer from tight runtime coupling or depend on offline reward signals, resulting in substantial inference overhead or hindering end-to-end optimization. To overcome these limitations, we introduce WPT, a World-to-Policy Transfer training paradigm that enables online distillation under the guidance of an end-to-end world model. Specifically, we develop a trainable reward model that infuses world knowledge into a teacher policy by aligning candidate trajectories with the future dynamics predicted by the world model. Subsequently, we propose policy distillation and world reward distillation to transfer the teacher's reasoning ability into a lightweight student policy, enhancing planning performance while preserving real-time deployability. Extensive experiments on both open-loop and closed-loop benchmarks show that our WPT achieves state-of-the-art performance with a simple policy architecture: it attains a 0.11 collision rate (open-loop) and achieves a 79.23 driving score (closed-loop) surpassing both world-model-based and imitation-learning methods in accuracy and safety. Moreover, the student sustains up to 4.9x faster inference, while retaining most of the gains.
Submission history
From: Guangfeng Jiang [view email][v1] Tue, 25 Nov 2025 09:12:06 UTC (982 KB)
[v2] Wed, 18 Mar 2026 02:40:09 UTC (972 KB)
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
