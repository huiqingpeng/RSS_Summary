---
title: "Embedding Physical Reasoning into Diffusion-Based Shadow Generation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2512.06174"
published: "2026-03-20"
fetched: "2026-03-20T16:15:45.452967"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 5 Dec 2025 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:Embedding Physical Reasoning into Diffusion-Based Shadow Generation
View PDF HTML (experimental)Abstract:Generating realistic shadows for inserted objects requires reasoning about scene geometry and illumination. However, most existing methods operate purely in image space, leaving the physical relationship between objects, lighting, and shadows to be learned implicitly, often resulting in misaligned or implausible shadows. We instead ground shadow generation in the physics of shadow formation. Given a composite image and an object mask, we recover approximate scene geometry and estimate a dominant light direction to derive a physics-grounded shadow estimate via geometric reasoning. While coarse, this estimate provides a spatial anchor for shadow placement. Because illumination cannot always be uniquely inferred from a single image, we predict confidence scores for both lighting and shadow cues and use them to regulate their influence during generation. These cues, shadow mask, light direction, and their confidences, condition a diffusion-based generator that refines the estimate into a realistic shadow. Experiments on DESOBAV2 show that our method improves both shadow realism and localization, achieving 23% lower shadow-region RMSE and 30% lower shadow-region BER over prior state-of-the-art.
Submission history
From: Shilin Hu [view email][v1] Fri, 5 Dec 2025 21:52:23 UTC (9,389 KB)
[v2] Wed, 18 Mar 2026 18:12:43 UTC (6,802 KB)
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
