---
title: "Stress Estimation in Elderly Oncology Patients Using Visual Wearable Representations and Multi-Instance Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.06990"
published: "2026-04-09"
fetched: "2026-04-10T07:05:10.512553"
---

Computer Science > Machine Learning
[Submitted on 8 Apr 2026]
Title:Stress Estimation in Elderly Oncology Patients Using Visual Wearable Representations and Multi-Instance Learning
View PDF HTML (experimental)Abstract:Psychological stress is clinically relevant in cardio-oncology, yet it is typically assessed only through patient-reported outcome measures (PROMs) and is rarely integrated into continuous cardiotoxicity surveillance. We estimate perceived stress in an elderly, multicenter breast cancer cohort (CARDIOCARE) using multimodal wearable data from a smartwatch (physical activity and sleep) and a chest-worn ECG sensor. Wearable streams are transformed into heterogeneous visual representations, yielding a weakly supervised setting in which a single Perceived Stress Scale (PSS) score corresponds to many unlabeled windows. A lightweight pretrained mixture-of-experts backbone (Tiny-BioMoE) embeds each representation into 192-dimensional vectors, which are aggregated via attention-based multiple instance learning (MIL) to predict PSS at month 3 (M3) and month 6 (M6). Under leave-one-subject-out (LOSO) evaluation, predictions showed moderate agreement with questionnaire scores (M3: R^2=0.24, Pearson r=0.42, Spearman rho=0.48; M6: R^2=0.28, Pearson r=0.49, Spearman rho=0.52), with global RMSE/MAE of 6.62/6.07 at M3 and 6.13/5.54 at M6.
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
