---
title: "A Tutorial on ALOS2 SAR Utilization: Dataset Preparation, Self-Supervised Pretraining, and Semantic Segmentation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.15119"
published: "2026-03-19"
fetched: "2026-03-19T17:04:39.478772"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 16 Mar 2026 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:A Tutorial on ALOS2 SAR Utilization: Dataset Preparation, Self-Supervised Pretraining, and Semantic Segmentation
View PDF HTML (experimental)Abstract:Masked auto-encoders (MAE) and related approaches have shown promise for satellite imagery, but their application to synthetic aperture radar (SAR) remains limited due to challenges in semantic labeling and high noise levels. Building on our prior work with SAR-W-MixMAE, which adds SAR-specific intensity-weighted loss to standard MixMAE for pretraining, we also introduce SAR-W-SimMIM; a weighted variant of SimMIM applied to ALOS-2 single-channel SAR imagery. This method aims to reduce the impact of speckle and extreme intensity values during self-supervised pretraining. We evaluate its effect on semantic segmentation compared to our previous trial with SAR-W-MixMAE and random initialization, observing notable improvements. In addition, pretraining and fine-tuning models on satellite imagery pose unique challenges, particularly when developing region-specific models. Imbalanced land cover distributions such as dominant water, forest, or desert areas can introduce bias, affecting both pretraining and downstream tasks like land cover segmentation. To address this, we constructed a SAR dataset using ALOS-2 single-channel (HH polarization) imagery focused on the Japan region, marking the initial phase toward a national-scale foundation model. This dataset was used to pretrain a vision transformer-based autoencoder, with the resulting encoder fine-tuned for semantic segmentation using a task-specific decoder. Initial results demonstrate significant performance improvements compared to training from scratch with random initialization. In summary, this work provides a guide to process and prepare ALOS2 observations to create dataset so that it can be taken advantage of self-supervised pretraining of models and finetuning downstream tasks such as semantic segmentation.
Submission history
From: Nevrez Imamoglu [view email][v1] Mon, 16 Mar 2026 11:16:03 UTC (19,648 KB)
[v2] Wed, 18 Mar 2026 04:23:38 UTC (19,642 KB)
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
