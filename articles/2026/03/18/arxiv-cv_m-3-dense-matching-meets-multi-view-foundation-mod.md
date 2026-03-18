---
title: "M^3: Dense Matching Meets Multi-View Foundation Models for Monocular Gaussian Splatting SLAM"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16844"
published: "2026-03-18"
fetched: "2026-03-18T18:21:10.627430"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:M^3: Dense Matching Meets Multi-View Foundation Models for Monocular Gaussian Splatting SLAM
View PDF HTML (experimental)Abstract:Streaming reconstruction from uncalibrated monocular video remains challenging, as it requires both high-precision pose estimation and computationally efficient online refinement in dynamic environments. While coupling 3D foundation models with SLAM frameworks is a promising paradigm, a critical bottleneck persists: most multi-view foundation models estimate poses in a feed-forward manner, yielding pixel-level correspondences that lack the requisite precision for rigorous geometric optimization. To address this, we present M^3, which augments the Multi-view foundation model with a dedicated Matching head to facilitate fine-grained dense correspondences and integrates it into a robust Monocular Gaussian Splatting SLAM. M^3 further enhances tracking stability by incorporating dynamic area suppression and cross-inference intrinsic alignment. Extensive experiments on diverse indoor and outdoor benchmarks demonstrate state-of-the-art accuracy in both pose estimation and scene reconstruction. Notably, M^3 reduces ATE RMSE by 64.3% compared to VGGT-SLAM 2.0 and outperforms ARTDECO by 2.11 dB in PSNR on the ScanNet++ dataset.
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
