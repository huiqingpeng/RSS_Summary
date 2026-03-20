---
title: "Object-Centric Representation Learning for Enhanced 3D Semantic Scene Graph Prediction"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2510.04714"
published: "2026-03-20"
fetched: "2026-03-20T16:14:13.549312"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 6 Oct 2025 (v1), last revised 19 Mar 2026 (this version, v5)]
Title:Object-Centric Representation Learning for Enhanced 3D Semantic Scene Graph Prediction
View PDF HTML (experimental)Abstract:3D Semantic Scene Graph Prediction aims to detect objects and their semantic relationships in 3D scenes, and has emerged as a crucial technology for robotics and AR/VR applications. While previous research has addressed dataset limitations and explored various approaches including Open-Vocabulary settings, they frequently fail to optimize the representational capacity of object and relationship features, showing excessive reliance on Graph Neural Networks despite insufficient discriminative capability. In this work, we demonstrate through extensive analysis that the quality of object features plays a critical role in determining overall scene graph accuracy. To address this challenge, we design a highly discriminative object feature encoder and employ a contrastive pretraining strategy that decouples object representation learning from the scene graph prediction. This design not only enhances object classification accuracy but also yields direct improvements in relationship prediction. Notably, when plugging in our pretrained encoder into existing frameworks, we observe substantial performance improvements across all evaluation metrics. Additionally, whereas existing approaches have not fully exploited the integration of relationship information, we effectively combine both geometric and semantic features to achieve superior relationship prediction. Comprehensive experiments on the 3DSSG dataset demonstrate that our approach significantly outperforms previous state-of-the-art methods. Our code is publicly available at this https URL.
Submission history
From: KunHo Heo [view email][v1] Mon, 6 Oct 2025 11:33:09 UTC (4,020 KB)
[v2] Mon, 29 Dec 2025 07:15:13 UTC (3,186 KB)
[v3] Mon, 2 Feb 2026 08:57:36 UTC (3,157 KB)
[v4] Thu, 26 Feb 2026 16:03:04 UTC (3,157 KB)
[v5] Thu, 19 Mar 2026 03:23:28 UTC (3,236 KB)
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
