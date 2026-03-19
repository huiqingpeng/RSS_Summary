---
title: "NutVLM: A Self-Adaptive Defense Framework against Full-Dimension Attacks for Vision Language Models in Autonomous Driving"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2602.13293"
published: "2026-03-19"
fetched: "2026-03-19T16:30:57.270059"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 9 Feb 2026 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:NutVLM: A Self-Adaptive Defense Framework against Full-Dimension Attacks for Vision Language Models in Autonomous Driving
View PDF HTML (experimental)Abstract:Vision Language Models (VLMs) have advanced perception in autonomous driving (AD), but they remain vulnerable to adversarial threats. These risks range from localized physical patches to imperceptible global perturbations. Existing defense methods for VLMs remain limited and often fail to reconcile robustness with clean-sample performance. To bridge these gaps, we propose NutVLM, a comprehensive self-adaptive defense framework designed to secure the entire perception-decision lifecycle. Specifically, we first employ NutNet++ as a sentinel, which is a unified detection-purification mechanism. It identifies benign samples, local patches, and global perturbations through three-way classification. Subsequently, localized threats are purified via efficient grayscale masking, while global perturbations trigger Expert-guided Adversarial Prompt Tuning (EAPT). Instead of the costly parameter updates of full-model fine-tuning, EAPT generates "corrective driving prompts" via gradient-based latent optimization and discrete projection. These prompts refocus the VLM's attention without requiring exhaustive full-model retraining. Evaluated on the Dolphins benchmark, our NutVLM yields a 4.89% improvement in overall metrics (e.g., Accuracy, Language Score, and GPT Score). These results validate NutVLM as a scalable security solution for intelligent transportation. Our code is available at this https URL.
Submission history
From: Xiaoxu Peng [view email][v1] Mon, 9 Feb 2026 05:42:59 UTC (30,501 KB)
[v2] Wed, 18 Mar 2026 02:30:50 UTC (27,262 KB)
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
