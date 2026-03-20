---
title: "SwiftTailor: Efficient 3D Garment Generation with Geometry Image Representation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.19053"
published: "2026-03-20"
fetched: "2026-03-20T15:18:46.868055"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 19 Mar 2026]
Title:SwiftTailor: Efficient 3D Garment Generation with Geometry Image Representation
View PDFAbstract:Realistic and efficient 3D garment generation remains a longstanding challenge in computer vision and digital fashion. Existing methods typically rely on large vision- language models to produce serialized representations of 2D sewing patterns, which are then transformed into simulation-ready 3D meshes using garment modeling framework such as GarmentCode. Although these approaches yield high-quality results, they often suffer from slow inference times, ranging from 30 seconds to a minute. In this work, we introduce SwiftTailor, a novel two-stage framework that unifies sewing-pattern reasoning and geometry-based mesh synthesis through a compact geometry image representation. SwiftTailor comprises two lightweight modules: PatternMaker, an efficient vision-language model that predicts sewing patterns from diverse input modalities, and GarmentSewer, an efficient dense prediction transformer that converts these patterns into a novel Garment Geometry Image, encoding the 3D surface of all garment panels in a unified UV space. The final 3D mesh is reconstructed through an efficient inverse mapping process that incorporates remeshing and dynamic stitching algorithms to directly assemble the garment, thereby amortizing the cost of physical simulation. Extensive experiments on the Multimodal GarmentCodeData demonstrate that SwiftTailor achieves state-of-the-art accuracy and visual fidelity while significantly reducing inference time. This work offers a scalable, interpretable, and high-performance solution for next-generation 3D garment generation.
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
