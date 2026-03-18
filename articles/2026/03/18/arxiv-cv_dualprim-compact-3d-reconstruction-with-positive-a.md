---
title: "DualPrim: Compact 3D Reconstruction with Positive and Negative Primitives"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16133"
published: "2026-03-18"
fetched: "2026-03-18T18:06:20.701167"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:DualPrim: Compact 3D Reconstruction with Positive and Negative Primitives
View PDF HTML (experimental)Abstract:Neural reconstructions often trade structure for fidelity, yielding dense and unstructured meshes with irregular topology and weak part boundaries that hinder editing, animation, and downstream asset reuse. We present DualPrim, a compact and structured 3D reconstruction framework. Unlike additive-only implicit or primitive methods, DualPrim represents shapes with positive and negative superquadrics: the former builds the bases while the latter carves local volumes through a differentiable operator, enabling topology-aware modeling of holes and concavities. This additive-subtractive design increases the representational power without sacrificing compactness or differentiability. We embed DualPrim in a volumetric differentiable renderer, enabling end-to-end learning from multi-view images and seamless mesh export via closed-form boolean difference. Empirically, DualPrim delivers state-of-the-art accuracy and produces compact, structured, and interpretable outputs that better satisfy downstream needs than additive-only alternatives.
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
