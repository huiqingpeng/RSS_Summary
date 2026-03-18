---
title: "SAC-NeRF: Adaptive Ray Sampling for Neural Radiance Fields via Soft Actor-Critic Reinforcement Learning"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.15622"
published: "2026-03-18"
fetched: "2026-03-18T17:17:35.958805"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 31 Dec 2025]
Title:SAC-NeRF: Adaptive Ray Sampling for Neural Radiance Fields via Soft Actor-Critic Reinforcement Learning
View PDFAbstract:Neural Radiance Fields (NeRF) have achieved photorealistic novel view synthesis but suffer from computational inefficiency due to dense ray sampling during volume rendering. We propose SAC-NeRF, a reinforcement learning framework that learns adaptive sampling policies using Soft Actor-Critic (SAC). Our method formulates sampling as a Markov Decision Process where an RL agent learns to allocate samples based on scene characteristics. We introduce three technical components: (1) a Gaussian mixture distribution color model providing uncertainty estimates, (2) a multi-component reward function balancing quality, efficiency, and consistency, and (3) a two-stage training strategy addressing environment non-stationarity. Experiments on Synthetic-NeRF and LLFF datasets show that SAC-NeRF reduces sampling points by 35-48\% while maintaining rendering quality within 0.3-0.8 dB PSNR of dense sampling baselines. While the learned policy is scene-specific and the RL framework adds complexity compared to simpler heuristics, our work demonstrates that data-driven sampling strategies can discover effective patterns that would be difficult to hand-design.
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
