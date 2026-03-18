---
title: "A Novel Patch-Based TDA Approach for Computed Tomography Imaging"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2512.12108"
published: "2026-03-18"
fetched: "2026-03-18T17:13:04.294896"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 13 Dec 2025 (v1), last revised 17 Mar 2026 (this version, v4)]
Title:A Novel Patch-Based TDA Approach for Computed Tomography Imaging
View PDF HTML (experimental)Abstract:The development of machine learning (ML) models based on computed tomography (CT) imaging has been a major focus due to the promise that imaging holds for diagnosis, staging, and prognostication. These models often rely on the extraction of hand-crafted features, incorporating robust feature engineering improves the performance of these models. Topological data analysis (TDA), based on the mathematical field of algebraic topology, focuses on data from a topological perspective, extracting deeper insight and higher dimensional structures. Persistent homology (PH), a fundamental tool in TDA, extracts topological features such as connected components, cycles, and voids. A popular approach to construct PH from 3D CT images is to utilize the 3D cubical complex filtration, a method adapted for grid-structured data. However, this approach is subject to poor performance and high computational cost with higher resolution CT images. This study introduces a novel patch-based PH construction approach tailored for volumetric CT imaging data that improves performance and reduces computational time. This study conducts a series of systematic experiments to comprehensively analyze the performance of the proposed method with various parameters and benchmarks against the 3D cubical complex algorithm and radiomic features. Our results highlight the dominance of the patch-based TDA approach in terms of both classification performance and computational time. The proposed approach outperformed the cubical complex method and radiomic features, achieving average improvement of 7.2%, 3.6%, 2.7%, 8.0%, and 7.2% in accuracy, AUC, sensitivity, specificity, and F1 score, respectively, across all datasets. Finally, we provide a convenient python package, Patch-TDA, to facilitate the utilization of the proposed approach.
Submission history
From: Dashti Ali [view email][v1] Sat, 13 Dec 2025 00:51:03 UTC (3,702 KB)
[v2] Fri, 9 Jan 2026 15:47:58 UTC (3,703 KB)
[v3] Thu, 5 Mar 2026 20:34:26 UTC (3,702 KB)
[v4] Tue, 17 Mar 2026 15:48:45 UTC (3,701 KB)
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
