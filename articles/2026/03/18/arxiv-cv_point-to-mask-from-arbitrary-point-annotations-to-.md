---
title: "Point-to-Mask: From Arbitrary Point Annotations to Mask-Level Infrared Small Target Detection"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16257"
published: "2026-03-18"
fetched: "2026-03-18T18:09:43.127439"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:Point-to-Mask: From Arbitrary Point Annotations to Mask-Level Infrared Small Target Detection
View PDF HTML (experimental)Abstract:Infrared small target detection (IRSTD) methods predominantly formulate the task as pixel-level segmentation, which requires costly dense annotations and is not well suited to tiny targets with weak texture and ambiguous boundaries. To address this issue, we propose Point-to-Mask, a framework that bridges low-cost point supervision and mask-level detection through two components: a Physics-driven Adaptive Mask Generation (PAMG) module that converts point annotations into compact target masks and geometric cues, and a lightweight Radius-aware Point Regression Network (RPR-Net) that reformulates IRSTD as target center localization and effective radius regression using spatiotemporal motion cues. The two modules form a closed loop: PAMG generates pseudo masks and geometric supervision during training, while the geometric predictions of RPR-Net are fed back to PAMG for pixel-level mask recovery during inference. To facilitate systematic evaluation, we further construct SIRSTD-Pixel, a sequential dataset with refined pixel-level annotations. Experiments show that the proposed framework achieves strong pseudo-label quality, high detection accuracy, and efficient inference, approaching full-supervision performance under point-supervised settings with substantially lower annotation cost. Code and datasets will be available at: this https URL.
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
