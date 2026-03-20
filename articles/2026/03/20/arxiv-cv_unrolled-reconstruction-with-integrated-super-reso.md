---
title: "Unrolled Reconstruction with Integrated Super-Resolution for Accelerated 3D LGE MRI"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18309"
published: "2026-03-20"
fetched: "2026-03-20T15:07:17.200498"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:Unrolled Reconstruction with Integrated Super-Resolution for Accelerated 3D LGE MRI
View PDF HTML (experimental)Abstract:Accelerated 3D late gadolinium enhancement (LGE) MRI requires robust reconstruction methods to recover thin atrial structures from undersampled k-space data. While unrolled model-based networks effectively integrate physics-driven data consistency with learned priors, they operate at the acquired resolution and may fail to fully recover high-frequency detail. We propose a hybrid unrolled reconstruction framework in which an Enhanced Deep Super-Resolution (EDSR) network replaces the proximal operator within each iteration of the optimization loop, enabling joint super-resolution enhancement and data consistency enforcement. The model is trained end-to-end on retrospectively undersampled preclinical 3D LGE datasets and compared against compressed sensing, Model-Based Deep Learning (MoDL), and self-guided Deep Image Prior (DIP) baselines. Across acceleration factors, the proposed method consistently improves PSNR and SSIM over standard unrolled reconstruction and better preserves fine cardiac structures, leading to improved LA (left atrium) segmentation performance. These results demonstrate that integrating super-resolution priors directly within model-based reconstruction provides measurable gains in accelerated 3D LGE MRI.
Submission history
From: Md Hasibul Husain Hisham [view email][v1] Wed, 18 Mar 2026 21:48:48 UTC (2,511 KB)
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
