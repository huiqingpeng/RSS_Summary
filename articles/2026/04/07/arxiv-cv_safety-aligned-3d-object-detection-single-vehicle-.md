---
title: "Safety-Aligned 3D Object Detection: Single-Vehicle, Cooperative, and End-to-End Perspectives"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2604.03325"
published: "2026-04-07"
fetched: "2026-04-08T07:02:49.987047"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 2 Apr 2026]
Title:Safety-Aligned 3D Object Detection: Single-Vehicle, Cooperative, and End-to-End Perspectives
View PDF HTML (experimental)Abstract:Perception plays a central role in connected and autonomous vehicles (CAVs), underpinning not only conventional modular driving stacks, but also cooperative perception systems and recent end-to-end driving models. While deep learning has greatly improved perception performance, its statistical nature makes perfect predictions difficult to attain. Meanwhile, standard training objectives and evaluation benchmarks treat all perception errors equally, even though only a subset is safety-critical. In this paper, we investigate safety-aligned evaluation and optimization for 3D object detection that explicitly characterize high-impact errors. Building on our previously proposed safety-oriented metric, NDS-USC, and safety-aware loss function, EC-IoU, we make three contributions. First, we present an expanded study of single-vehicle 3D object detection models across diverse neural network architectures and sensing modalities, showing that gains under standard metrics such as mAP and NDS may not translate to safety-oriented criteria represented by NDS-USC. With EC-IoU, we reaffirm the benefit of safety-aware fine-tuning for improving safety-critical detection performance. Second, we conduct an ego-centric, safety-oriented evaluation of AV-infrastructure cooperative object detection models, underscoring its superiority over vehicle-only models and demonstrating a safety impact analysis that illustrates the potential contribution of cooperative models to "Vision Zero." Third, we integrate EC-IoU into SparseDrive and show that safety-aware perception hardening can reduce collision rate by nearly 30% and improve system-level safety directly in an end-to-end perception-to-planning framework. Overall, our results indicate that safety-aligned perception evaluation and optimization offer a practical path toward enhancing CAV safety across single-vehicle, cooperative, and end-to-end autonomy settings.
Submission history
From: Brian Hsuan-Cheng Liao [view email][v1] Thu, 2 Apr 2026 21:18:01 UTC (3,811 KB)
Current browse context:
cs.CV
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
ScienceCast (What is ScienceCast?)
Demos
Recommenders and Search Tools
Influence Flower (What are Influence Flowers?)
CORE Recommender (What is CORE?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
