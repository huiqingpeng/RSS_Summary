---
title: "MIPHEI-ViT: Multiplex Immunofluorescence Prediction from H&E Images using ViT Foundation Models"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2505.10294"
published: "2026-03-20"
fetched: "2026-03-20T16:11:24.939923"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 15 May 2025 (v1), last revised 19 Mar 2026 (this version, v2)]
Title:MIPHEI-ViT: Multiplex Immunofluorescence Prediction from H&E Images using ViT Foundation Models
View PDF HTML (experimental)Abstract:Histopathological analysis is a cornerstone of cancer diagnosis, with Hematoxylin and Eosin (H&E) staining routinely acquired for every patient to visualize cell morphology and tissue architecture. On the other hand, multiplex immunofluorescence (mIF) enables more precise cell type identification via proteomic markers, but has yet to achieve widespread clinical adoption due to cost and logistical constraints. To bridge this gap, we introduce MIPHEI (Multiplex Immunofluorescence Prediction from H&E Images), a U-Net-inspired architecture that leverages a ViT pathology foundation model as encoder to predict mIF signals from H&E images using rich pretrained representations. MIPHEI targets a comprehensive panel of markers spanning nuclear content, immune lineages (T cells, B cells, myeloid), epithelium, stroma, vasculature, and proliferation. We train our model using the publicly available OrionCRC dataset of restained H&E and mIF images from colorectal cancer tissue, and validate it on five independent datasets: HEMIT, PathoCell, IMMUcan, Lizard and PanNuke. On OrionCRC test set, MIPHEI achieves accurate cell-type classification from H&E alone, with F1 scores of 0.93 for Pan-CK, 0.83 for alpha-SMA, 0.68 for CD3e, 0.36 for CD20, and 0.28 for CD68, substantially outperforming both a state-of-the-art baseline and a random classifier for most markers. Our results indicate that, for some molecular markers, our model captures the complex relationships between nuclear morphologies in their tissue context, as visible in H&E images and molecular markers defining specific cell types. MIPHEI offers a promising step toward enabling cell-type-aware analysis of large-scale H&E datasets, in view of uncovering relationships between spatial cellular organization and patient outcomes.
Submission history
From: Guillaume Balezo [view email][v1] Thu, 15 May 2025 13:42:48 UTC (31,708 KB)
[v2] Thu, 19 Mar 2026 14:24:18 UTC (17,779 KB)
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
