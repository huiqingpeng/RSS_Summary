---
title: "Auto-Annotation with Expert-Crafted Guidelines: A Study through 3D LiDAR Detection Benchmark"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2506.02914"
published: "2026-03-20"
fetched: "2026-03-20T16:11:52.713459"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 3 Jun 2025 (v1), last revised 19 Mar 2026 (this version, v2)]
Title:Auto-Annotation with Expert-Crafted Guidelines: A Study through 3D LiDAR Detection Benchmark
View PDF HTML (experimental)Abstract:Data annotation is crucial for developing machine learning solutions. The current paradigm is to hire ordinary human annotators to annotate data instructed by expert-crafted guidelines. As this paradigm is laborious, tedious, and costly, we are motivated to explore auto-annotation with expert-crafted guidelines. To this end, we first develop a supporting benchmark AutoExpert by repurposing the established nuScenes dataset, which has been widely used in autonomous driving research and provides authentic expert-crafted guidelines. The guidelines define 18 object classes using both nuanced language descriptions and a few visual examples, and require annotating objects in LiDAR data with 3D cuboids. Notably, the guidelines do not provide LiDAR visuals to demonstrate how to annotate. Therefore, AutoExpert requires methods to learn on few-shot labeled images and texts to perform 3D detection in LiDAR data. Clearly, the challenges of AutoExpert lie in the data-modality and annotation-task discrepancies. Meanwhile, publicly-available foundation models (FMs) serve as promising tools to tackle these challenges. Hence, we address AutoExpert by leveraging appropriate FMs within a conceptually simple pipeline, which (1) utilizes FMs for 2D object detection and segmentation in RGB images, (2) lifts 2D detections into 3D using known sensor poses, and (3) generates 3D cuboids for the 2D detections. In this pipeline, we progressively refine key components and eventually boost 3D detection mAP to 25.4, significantly higher than 12.1 achieved by prior arts.
Submission history
From: Yechi Ma [view email][v1] Tue, 3 Jun 2025 14:17:37 UTC (5,477 KB)
[v2] Thu, 19 Mar 2026 08:24:17 UTC (9,117 KB)
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
