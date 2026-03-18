---
title: "Fast-HaMeR: Boosting Hand Mesh Reconstruction using Knowledge Distillation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16444"
published: "2026-03-18"
fetched: "2026-03-18T18:13:22.783241"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:Fast-HaMeR: Boosting Hand Mesh Reconstruction using Knowledge Distillation
View PDF HTML (experimental)Abstract:Fast and accurate 3D hand reconstruction is essential for real-time applications in VR/AR, human-computer interaction, robotics, and healthcare. Most state-of-the-art methods rely on heavy models, limiting their use on resource-constrained devices like headsets, smartphones, and embedded systems. In this paper, we investigate how the use of lightweight neural networks, combined with Knowledge Distillation, can accelerate complex 3D hand reconstruction models by making them faster and lighter, while maintaining comparable reconstruction accuracy. While our approach is suited for various hand reconstruction frameworks, we focus primarily on boosting the HaMeR model, currently the leading method in terms of reconstruction accuracy. We replace its original ViT-H backbone with lighter alternatives, including MobileNet, MobileViT, ConvNeXt, and ResNet, and evaluate three knowledge distillation strategies: output-level, feature-level, and a hybrid of both. Our experiments show that using lightweight backbones that are only 35% the size of the original achieves 1.5x faster inference speed while preserving similar performance quality with only a minimal accuracy difference of 0.4mm. More specifically, we show how output-level distillation notably improves student performance, while feature-level distillation proves more effective for higher-capacity students. Overall, the findings pave the way for efficient real-world applications on low-power devices. The code and models are publicly available under this https URL.
Submission history
From: Ahmed Tawfik Aboukhadra [view email][v1] Tue, 17 Mar 2026 12:28:02 UTC (8,881 KB)
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
