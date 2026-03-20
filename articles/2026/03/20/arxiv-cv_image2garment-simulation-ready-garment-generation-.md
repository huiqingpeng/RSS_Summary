---
title: "Image2Garment: Simulation-ready Garment Generation from a Single Image"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2601.09658"
published: "2026-03-20"
fetched: "2026-03-20T16:17:06.288560"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 14 Jan 2026 (v1), last revised 19 Mar 2026 (this version, v4)]
Title:Image2Garment: Simulation-ready Garment Generation from a Single Image
View PDF HTML (experimental)Abstract:Estimating physically accurate, simulation-ready garments from a single image is challenging due to the absence of image-to-physics datasets and the ill-posed nature of this problem. Prior methods either require multi-view capture and expensive differentiable simulation or predict only garment geometry without the material properties required for realistic simulation. We propose a feed-forward framework that sidesteps these limitations by first fine-tuning a vision-language model to infer material composition and fabric attributes from real images, and then training a lightweight predictor that maps these attributes to the corresponding physical fabric parameters using a small dataset of material-physics measurements. Our approach introduces two new datasets (FTAG and T2P) and delivers simulation-ready garments from a single image without iterative optimization. Experiments show that our estimator achieves superior accuracy in material composition estimation and fabric attribute prediction, and by passing them through our physics parameter estimator, we further achieve higher-fidelity simulations compared to state-of-the-art image-to-garment methods.
Submission history
From: Selim Can [view email][v1] Wed, 14 Jan 2026 17:47:33 UTC (8,739 KB)
[v2] Thu, 15 Jan 2026 21:21:50 UTC (8,739 KB)
[v3] Sun, 25 Jan 2026 14:13:38 UTC (8,711 KB)
[v4] Thu, 19 Mar 2026 00:15:11 UTC (8,738 KB)
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
