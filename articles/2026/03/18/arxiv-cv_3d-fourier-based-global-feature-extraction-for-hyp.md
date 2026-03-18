---
title: "3D Fourier-based Global Feature Extraction for Hyperspectral Image Classification"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16426"
published: "2026-03-18"
fetched: "2026-03-18T18:12:58.711255"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:3D Fourier-based Global Feature Extraction for Hyperspectral Image Classification
View PDF HTML (experimental)Abstract:Hyperspectral image classification (HSIC) has been significantly advanced by deep learning methods that exploit rich spatial-spectral correlations. However, existing approaches still face fundamental limitations: transformer-based models suffer from poor scalability due to the quadratic complexity of self-attention, while recent Fourier transform-based methods typically rely on 2D spatial FFTs and largely ignore critical inter-band spectral dependencies inherent to hyperspectral data. To address these challenges, we propose Hybrid GFNet (HGFNet), a novel architecture that integrates localized 3D convolutional feature extraction with frequency-domain global filtering via GFNet-style blocks for efficient and robust spatial-spectral representation learning. HGFNet introduces three complementary frequency transforms tailored to hyperspectral imagery: Spectral Fourier Transform (a 1D FFT along the spectral axis), Spatial Fourier Transform (a 2D FFT over spatial dimensions), and Spatial-Spatial Fourier Transform (a 3D FFT jointly over spectral and spatial dimensions), enabling comprehensive and high-dimensional frequency modeling. The 3D convolutional layers capture fine-grained local spatial-spectral structures, while the Fourier-based global filtering modules efficiently model long-range dependencies and suppress noise. To further mitigate the severe class imbalance commonly observed in HSIC, HGFNet incorporates an Adaptive Focal Loss (AFL) that dynamically adjusts class-wise focusing and weighting, improving discrimination for underrepresented classes.
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
