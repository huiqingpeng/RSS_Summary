---
title: "Halfway to 3D: Ensembling 2.5D and 3D Models for Robust COVID-19 CT Diagnosis"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.14832"
published: "2026-03-19"
fetched: "2026-03-19T14:20:12.395977"
---

Electrical Engineering and Systems Science > Image and Video Processing
[Submitted on 16 Mar 2026 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:Halfway to 3D: Ensembling 2.5D and 3D Models for Robust COVID-19 CT Diagnosis
View PDF HTML (experimental)Abstract:We propose a deep learning framework for COVID-19 detection and disease classification from chest CT scans that integrates both 2.5D and 3D representations to capture complementary slice-level and volumetric information. The 2.5D branch processes multi-view CT slices (axial, coronal, sagittal) using a DINOv3 vision transformer to extract robust visual features, while the 3D branch employs a ResNet-18 architecture to model volumetric context and is pretrained with Variance Risk Extrapolation (VREx) followed by supervised contrastive learning to improve cross-source robustness. Predictions from both branches are combined through logit-level ensemble inference. Experiments on the PHAROS-AIF-MIH benchmark demonstrate the effectiveness of the proposed approach: for binary COVID-19 detection, the ensemble achieves 94.48% accuracy and a 0.9426 Macro F1-score, outperforming both individual models, while for multi-class disease classification the 2.5D DINOv3 model achieves the best performance with 79.35% accuracy and a 0.7497 Macro F1-score. These results highlight the benefit of combining pretrained slice-based representations with volumetric modeling for robust multi-source medical imaging analysis. Code is available at this https URL
Submission history
From: Truong-Son Hy [view email][v1] Mon, 16 Mar 2026 05:24:10 UTC (470 KB)
[v2] Wed, 18 Mar 2026 04:16:07 UTC (470 KB)
Current browse context:
eess.IV
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
