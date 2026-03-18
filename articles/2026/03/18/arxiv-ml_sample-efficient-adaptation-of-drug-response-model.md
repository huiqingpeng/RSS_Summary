---
title: "Sample-Efficient Adaptation of Drug-Response Models to Patient Tumors under Strong Biological Domain Shift"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16185"
published: "2026-03-18"
fetched: "2026-03-18T15:41:34.002042"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:Sample-Efficient Adaptation of Drug-Response Models to Patient Tumors under Strong Biological Domain Shift
View PDF HTML (experimental)Abstract:Predicting drug response in patients from preclinical data remains a major challenge in precision oncology due to the substantial biological gap between in vitro cell lines and patient tumors. Rather than aiming to improve absolute in vitro prediction accuracy, this work examines whether explicitly separating representation learning from task supervision enables more sample-efficient adaptation of drug-response models to patient data under strong biological domain shift. We propose a staged transfer-learning framework in which cellular and drug representations are first learned independently from large collections of unlabeled pharmacogenomic data using autoencoder-based representation learning. These representations are then aligned with drug-response labels on cell-line data and subsequently adapted to patient tumors using few-shot supervision. Through a systematic evaluation spanning in-domain, cross-dataset, and patient-level settings, we show that unsupervised pretraining provides limited benefit when source and target domains overlap substantially, but yields clear gains when adapting to patient tumors with very limited labeled data. In particular, the proposed framework achieves faster performance improvements during few-shot patient-level adaptation while maintaining comparable accuracy to single-phase baselines on standard cell-line benchmarks. Overall, these results demonstrate that learning structured and transferable representations from unlabeled molecular profiles can substantially reduce the amount of clinical supervision required for effective drug-response prediction, offering a practical pathway toward data-efficient preclinical-to-clinical translation.
Submission history
From: Philippe Lalanda [view email][v1] Tue, 17 Mar 2026 07:12:38 UTC (1,036 KB)
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
