---
title: "DSeq-JEPA: Discriminative Sequential Joint-Embedding Predictive Architecture"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2511.17354"
published: "2026-03-19"
fetched: "2026-03-19T16:27:46.722941"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 21 Nov 2025 (v1), last revised 17 Mar 2026 (this version, v3)]
Title:DSeq-JEPA: Discriminative Sequential Joint-Embedding Predictive Architecture
View PDF HTML (experimental)Abstract:Recent advances in self-supervised visual representation learning have demonstrated the effectiveness of predictive latent-space objectives for learning transferable features. In particular, Image-based Joint-Embedding Predictive Architecture (I-JEPA) learns representations by predicting latent embeddings of masked target regions from visible context. However, it predicts target regions in parallel and all at once, lacking ability to order predictions meaningfully. Inspired by human visual perception, which attends selectively and progressively from primary to secondary cues, we propose DSeq-JEPA, a Discriminative Sequential Joint-Embedding Predictive Architecture that bridges latent predictive and autoregressive self-supervised learning. Specifically, DSeq-JEPA integrates a discriminatively ordered sequential process with JEPA-style learning objective. This is achieved by (i) identifying primary discriminative regions using an attention-derived saliency map that serves as a proxy for visual importance, and (ii) predicting subsequent regions in discriminative order, inducing a curriculum-like semantic progression from primary to secondary cues in pre-training. Extensive experiments across tasks -- image classification (ImageNet), fine-grained visual categorization (iNaturalist21, CUB, Stanford Cars), detection/segmentation (MS-COCO, ADE20K), and low-level reasoning (CLEVR) -- show that DSeq-JEPA consistently learns more discriminative and generalizable representations compared to I-JEPA variants. Project page: this https URL.
Submission history
From: Xiangteng He [view email][v1] Fri, 21 Nov 2025 16:18:50 UTC (8,220 KB)
[v2] Thu, 12 Mar 2026 19:55:28 UTC (17,275 KB)
[v3] Tue, 17 Mar 2026 20:10:41 UTC (11,130 KB)
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
