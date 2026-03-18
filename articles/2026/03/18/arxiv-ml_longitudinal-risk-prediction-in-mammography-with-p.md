---
title: "Longitudinal Risk Prediction in Mammography with Privileged History Distillation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15814"
published: "2026-03-18"
fetched: "2026-03-18T15:35:24.571967"
---

Computer Science > Machine Learning
[Submitted on 16 Mar 2026]
Title:Longitudinal Risk Prediction in Mammography with Privileged History Distillation
View PDF HTML (experimental)Abstract:Breast cancer remains a leading cause of cancer-related mortality worldwide. Longitudinal mammography risk prediction models improve multi-year breast cancer risk prediction based on prior screening exams. However, in real-world clinical practice, longitudinal histories are often incomplete, irregular, or unavailable due to missed screenings, first-time examinations, heterogeneous acquisition schedules, or archival constraints. The absence of prior exams degrades the performance of longitudinal risk models and limits their practical applicability. While substantial longitudinal history is available during training, prior exams are commonly absent at test time. In this paper, we address missing history at inference time and propose a longitudinal risk prediction method that uses mammography history as privileged information during training and distills its prognostic value into a student model that only requires the current exam at inference time. The key idea is a privileged multi-teacher distillation scheme with horizon-specific teachers: each teacher is trained on the full longitudinal history to specialize in one prediction horizon, while the student receives only a reconstructed history derived from the current exam. This allows the student to inherit horizon-dependent longitudinal risk cues without requiring prior screening exams at deployment. Our new Privileged History Distillation (PHD) method is validated on a large longitudinal mammography dataset with multi-year cancer outcomes, CSAW-CC, comparing full-history and no-history baselines to their distilled counterparts. Using time-dependent AUC across horizons, our privileged history distillation method markedly improves the performance of long-horizon prediction over no-history models and is comparable to that of full-history models, while using only the current exam at inference time.
Submission history
From: Banafsheh Karimian [view email][v1] Mon, 16 Mar 2026 18:45:19 UTC (6,727 KB)
Current browse context:
cs.LG
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
IArxiv Recommender
(What is IArxiv?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
