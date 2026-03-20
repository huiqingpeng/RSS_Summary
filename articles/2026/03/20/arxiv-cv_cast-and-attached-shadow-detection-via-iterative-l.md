---
title: "Cast and Attached Shadow Detection via Iterative Light and Geometry Reasoning"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2512.06179"
published: "2026-03-20"
fetched: "2026-03-20T16:15:51.455177"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 5 Dec 2025 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:Cast and Attached Shadow Detection via Iterative Light and Geometry Reasoning
View PDF HTML (experimental)Abstract:Shadows encode rich information about scene geometry and illumination, yet existing methods either predict a unified shadow mask or overlook attached shadows entirely. We address this gap by proposing a framework for jointly detecting cast and attached shadows through explicit physical modeling of light direction and surface geometry. Our approach is grounded in a simple observation: surfaces facing away from the light source tend to fall into shadow. We exploit the reciprocal relationship between shadow formation and light estimation to construct a closed feedback loop, a dual-module architecture in which a shadow detection module and a light estimation module iteratively refine each other. At each pass, updated light estimates with surface normals produce partial attached shadow maps that guide detection, while improved shadow predictions sharpen light estimation. To support training and evaluation, we introduce a dataset of 1,458 images with manually annotated cast and attached shadow masks sourced from three existing benchmarks. Experiments demonstrate that our physically grounded, iterative formulation outperforms prior methods, with at least a 33% reduction in attached BER, while maintaining strong full and cast performance.
Submission history
From: Shilin Hu [view email][v1] Fri, 5 Dec 2025 22:01:27 UTC (8,979 KB)
[v2] Wed, 18 Mar 2026 18:06:56 UTC (20,375 KB)
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
