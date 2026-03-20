---
title: "Seeing Beyond the Image: ECG and Anatomical Knowledge-Guided Myocardial Scar Segmentation from Late Gadolinium-Enhanced Images"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2511.14702"
published: "2026-03-20"
fetched: "2026-03-20T16:15:06.049822"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Nov 2025 (v1), last revised 18 Mar 2026 (this version, v3)]
Title:Seeing Beyond the Image: ECG and Anatomical Knowledge-Guided Myocardial Scar Segmentation from Late Gadolinium-Enhanced Images
View PDF HTML (experimental)Abstract:Accurate segmentation of myocardial scar from late gadolinium enhanced (LGE) cardiac MRI is essential for evaluating tissue viability, yet remains challenging due to variable contrast and imaging artifacts. Electrocardiogram (ECG) signals provide complementary physiological information, as conduction abnormalities can help localize or suggest scarred myocardial regions. In this work, we propose a novel multimodal framework that integrates ECG-derived electrophysiological information with anatomical priors from the AHA-17 atlas for physiologically consistent LGE-based scar segmentation. As ECGs and LGE-MRIs are not acquired simultaneously, we introduce a Temporal Aware Feature Fusion (TAFF) mechanism that dynamically weights and fuses features based on their acquisition time difference. Our method was evaluated on a clinical dataset and achieved substantial gains over the state-of-the-art image-only baseline (nnU-Net), increasing the average Dice score for scars from 0.6149 to 0.8463 and achieving high performance in both precision (0.9115) and sensitivity (0.9043). These results show that integrating physiological and anatomical knowledge allows the model to "see beyond the image", setting a new direction for robust and physiologically grounded cardiac scar segmentation.
Submission history
From: Farheen Ramzan [view email][v1] Tue, 18 Nov 2025 17:42:20 UTC (1,060 KB)
[v2] Mon, 26 Jan 2026 13:39:13 UTC (960 KB)
[v3] Wed, 18 Mar 2026 15:33:36 UTC (959 KB)
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
