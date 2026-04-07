---
title: "MoViD: View-Invariant 3D Human Pose Estimation via Motion-View Disentanglement"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2604.03299"
published: "2026-04-07"
fetched: "2026-04-08T07:02:41.725195"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 29 Mar 2026]
Title:MoViD: View-Invariant 3D Human Pose Estimation via Motion-View Disentanglement
View PDF HTML (experimental)Abstract:3D human pose estimation is a key enabling technology for applications such as healthcare monitoring, human-robot collaboration, and immersive gaming, but real-world deployment remains challenged by viewpoint variations. Existing methods struggle to generalize to unseen camera viewpoints, require large amounts of training data, and suffer from high inference latency. We propose MoViD, a viewpoint-invariant 3D human pose estimation framework that disentangles viewpoint information from motion features. The key idea is to extract viewpoint information from intermediate pose features and leverage it to enhance both the robustness and efficiency of pose estimation. MoViD introduces a view estimator that models key joint relationships to predict viewpoint information, and an orthogonal projection module to disentangle motion and view features, further enhanced through physics-grounded contrastive alignment across views. For real-time edge deployment, MoViD employs a frame-by-frame inference pipeline with a view-aware strategy that adaptively activates flip refinement based on the estimated viewpoint. Evaluations on nine public datasets and newly collected multiview UAV and gait analysis datasets show that MoViD reduces pose estimation error by over 24.2\% compared to state-of-the-art methods, maintains robust performance under severe occlusions with 60\% less training data, and achieves real-time inference at 15 FPS on NVIDIA edge devices.
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
