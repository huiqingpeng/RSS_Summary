---
title: "Advancing Visual Reliability: Color-Accurate Underwater Image Enhancement for Real-Time Underwater Missions"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16363"
published: "2026-03-18"
fetched: "2026-03-18T18:11:40.837635"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:Advancing Visual Reliability: Color-Accurate Underwater Image Enhancement for Real-Time Underwater Missions
View PDF HTML (experimental)Abstract:Underwater image enhancement plays a crucial role in providing reliable visual information for underwater platforms, since strong absorption and scattering in water-related environments generally lead to image quality degradation. Existing high-performance methods often rely on complex architectures, which hinder deployment on underwater devices. Lightweight methods often sacrifice quality for speed and struggle to handle severely degraded underwater images. To address this limitation, we present a real-time underwater image enhancement framework with accurate color restoration. First, an Adaptive Weighted Channel Compensation module is introduced to achieve dynamic color recovery of the red and blue channels using the green channel as a reference anchor. Second, we design a Multi-branch Re-parameterized Dilated Convolution that employs multi-branch fusion during training and structural re-parameterization during inference, enabling large receptive field representation with low computational overhead. Finally, a Statistical Global Color Adjustment module is employed to optimize overall color performance based on statistical priors. Extensive experiments on eight datasets demonstrate that the proposed method achieves state-of-the-art performance across seven evaluation metrics. The model contains only 3,880 inference parameters and achieves an inference speed of 409 FPS. Our method improves the UCIQE score by 29.7% under diverse environmental conditions, and the deployment on ROV platforms and performance gains in downstream tasks further validate its superiority for real-time underwater missions.
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
