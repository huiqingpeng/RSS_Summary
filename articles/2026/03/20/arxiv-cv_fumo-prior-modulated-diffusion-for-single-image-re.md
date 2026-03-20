---
title: "FUMO: Prior-Modulated Diffusion for Single Image Reflection Removal"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.19036"
published: "2026-03-20"
fetched: "2026-03-20T15:18:19.668819"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 19 Mar 2026]
Title:FUMO: Prior-Modulated Diffusion for Single Image Reflection Removal
View PDF HTML (experimental)Abstract:Single image reflection removal (SIRR) is challenging in real scenes, where reflection strength varies spatially and reflection patterns are tightly entangled with transmission structures. This paper presents a diffusion model with prior modulation framework (FUMO) that introduces explicit guidance signals to improve spatial controllability and structural faithfulness. Two priors are extracted directly from the mixed image, an intensity prior that estimates spatial reflection severity and a high-frequency prior that captures detail-sensitive responses via multi-scale residual aggregation. We propose a coarse-to-fine training paradigm. In the first stage, these cues are combined to gate the conditional residual injections, focusing the conditioning on regions that are both reflection-dominant and structure-sensitive. In the second stage, a fine-grained refinement network corrects local misalignment and sharpens fine details in the image space. Experiments conducted on both standard benchmarks and challenging images in the wild demonstrate competitive quantitative results and consistently improved perceptual quality. The code is released at this https URL.
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
