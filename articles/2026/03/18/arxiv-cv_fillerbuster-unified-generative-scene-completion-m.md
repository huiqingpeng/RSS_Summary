---
title: "Fillerbuster: Unified Generative Scene Completion Model for Casual Captures"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2502.05175"
published: "2026-03-18"
fetched: "2026-03-18T18:25:11.150483"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 7 Feb 2025 (v1), last revised 16 Mar 2026 (this version, v2)]
Title:Fillerbuster: Unified Generative Scene Completion Model for Casual Captures
View PDFAbstract:We present Fillerbuster, a unified model that completes unknown regions of a 3D scene with a multi-view latent diffusion transformer. Casual captures are often sparse and miss surrounding content behind objects or above the scene. Existing methods are not suitable for this challenge as they focus on making known pixels look good with sparse-view priors, or on creating missing sides of objects from just one or two photos. In reality, we often have hundreds of input frames and want to complete areas that are missing and unobserved from the input frames. Our solution is to train a generative model that can consume a large context of input frames while generating unknown target views and recovering image poses when camera parameters are unknown. We show results where we complete partial captures on two existing datasets. We also present an uncalibrated scene completion task where our unified model predicts both poses and creates new content. We open-source our framework for integration into popular reconstruction platforms like Nerfstudio or Gsplat. We present a flexible, unified inpainting framework to predict many images and poses together, where all inputs are jointly inpainted, and it could be extended to predict more modalities such as depth.
Submission history
From: Ethan Weber [view email][v1] Fri, 7 Feb 2025 18:59:51 UTC (33,681 KB)
[v2] Mon, 16 Mar 2026 22:10:13 UTC (16,639 KB)
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
