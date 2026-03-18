---
title: "DiG: Differential Grounding for Enhancing Fine-Grained Perception in Multimodal Large Language Model"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2512.12633"
published: "2026-03-18"
fetched: "2026-03-18T18:31:32.442796"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 14 Dec 2025 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:DiG: Differential Grounding for Enhancing Fine-Grained Perception in Multimodal Large Language Model
View PDF HTML (experimental)Abstract:Multimodal Large Language Models have achieved impressive performance on a variety of vision-language tasks, yet their fine-grained visual perception and precise spatial reasoning remain limited. In this work, we introduce DiG (Differential Grounding), a novel proxy task framework where MLLMs learn fine-grained perception by identifying and localizing all differences between similar image pairs without prior knowledge of their number. To support scalable training, we develop an automated 3D rendering-based data generation pipeline that produces high-quality paired images with fully controllable discrepancies. To address the sparsity of difference signals, we further employ curriculum learning that progressively increases complexity from single to multiple differences, enabling stable optimization. Extensive experiments demonstrate that DiG significantly improves model performance across a variety of visual perception benchmarks and that the learned fine-grained perception skills transfer effectively to standard downstream tasks, including RefCOCO, RefCOCO+, RefCOCOg, and general multimodal perception benchmarks. Our results highlight differential grounding as a scalable and robust approach for advancing fine-grained visual reasoning in MLLMs.
Submission history
From: Zhou Tao [view email][v1] Sun, 14 Dec 2025 10:40:27 UTC (1,602 KB)
[v2] Tue, 17 Mar 2026 14:37:05 UTC (2,171 KB)
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
