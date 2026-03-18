---
title: "Bridging the Simulation-to-Reality Gap in Electron Microscope Calibration via VAE-EM Estimation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16549"
published: "2026-03-18"
fetched: "2026-03-18T16:13:13.216269"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:Bridging the Simulation-to-Reality Gap in Electron Microscope Calibration via VAE-EM Estimation
View PDF HTML (experimental)Abstract:Electron microscopy has enabled many scientific breakthroughs across multiple fields. A key challenge is the tuning of microscope parameters based on images to overcome optical aberrations that deteriorate image quality. This calibration problem is challenging due to the high-dimensional and noisy nature of the diagnostic images, and the fact that optimal parameters cannot be identified from a single image. We tackle the calibration problem for Scanning Transmission Electron Microscopes (STEM) by employing variational autoencoders (VAEs), trained on simulated data, to learn low-dimensional representations of images, whereas most existing methods extract only scalar values. We then simultaneously estimate the model that maps calibration parameters to encoded representations and the optimal calibration parameters using an expectation maximization (EM) approach. This joint estimation explicitly addresses the simulation-to-reality gap inherent in data-driven methods that train on simulated data from a digital twin. We leverage the known symmetry property of the optical system to establish global identifiability of the joint estimation problem, ensuring that a unique optimum exists. We demonstrate that our approach is substantially faster and more consistent than existing methods on a real STEM, achieving a 2x reduction in estimation error while requiring fewer observations. This represents a notable advance in automated STEM calibration and demonstrates the potential of VAEs for information compression in images. Beyond microscopy, the VAE-EM framework applies to inverse problems where simulated training data introduces a reality gap and where non-injective mappings would otherwise prevent unique solutions.
Submission history
From: Jilles Van Hulst [view email][v1] Tue, 17 Mar 2026 14:15:33 UTC (4,828 KB)
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
