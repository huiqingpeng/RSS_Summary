---
title: "DA-Mamba: Learning Domain-Aware State Space Model for Global-Local Alignment in Domain Adaptive Object Detection"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18757"
published: "2026-03-20"
fetched: "2026-03-20T15:15:42.585036"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 19 Mar 2026]
Title:DA-Mamba: Learning Domain-Aware State Space Model for Global-Local Alignment in Domain Adaptive Object Detection
View PDF HTML (experimental)Abstract:Domain Adaptive Object Detection (DAOD) aims to transfer detectors from a labeled source domain to an unlabeled target domain. Existing DAOD methods employ multi-granularity feature alignment to learn domain-invariant representations. However, the local connectivity of their CNN-based backbone and detection head restricts alignment to local regions, failing to extract global domain-invariant features. Although transformer-based DAOD methods capture global dependencies via attention mechanisms, their quadratic computational cost hinders practical deployment. To solve this, we propose DA-Mamba, a hybrid CNN-State Space Models (SSMs) architecture that combines the efficiency of CNNs with the linear-time long-range modeling capability of State Space Models (SSMs) to capture both global and local domain-invariant features. Specifically, we introduce two novel modules: Image-Aware SSM (IA-SSM) and Object-Aware SSM (OA-SSM). IA-SSM is integrated into the backbone to enhance global domain awareness, enabling image-level global and local alignment. OA-SSM is inserted into the detection head to model spatial and semantic dependencies among objects, enhancing instance-level alignment. Comprehensive experiments demonstrate that the proposed method can efficiently improve the cross-domain performance of the object detector.
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
