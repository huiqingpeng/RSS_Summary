---
title: "PulmoVec: A Two-Stage Stacking Meta-Learning Architecture Built on the HeAR Foundation Model for Multi-Task Classification of Pediatric Respiratory Sounds"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15688"
published: "2026-03-18"
fetched: "2026-03-18T16:06:52.619456"
---

Computer Science > Sound
[Submitted on 15 Mar 2026]
Title:PulmoVec: A Two-Stage Stacking Meta-Learning Architecture Built on the HeAR Foundation Model for Multi-Task Classification of Pediatric Respiratory Sounds
View PDF HTML (experimental)Abstract:Background: Respiratory diseases are a leading cause of childhood morbidity and mortality, yet lung auscultation remains subjective and limited by inter-listener variability, particularly in pediatric populations. Existing AI approaches are further constrained by small datasets and single-task designs. We developed PulmoVec, a multi-task framework built on the Health Acoustic Representations (HeAR) foundation model for classification of pediatric respiratory sounds. Methods: In this retrospective analysis of the SPRSound database, 24,808 event-level annotated segments from 1,652 pediatric patients were analyzed. Three task-specific classifiers were trained for screening, sound-pattern recognition, and disease-group prediction. Their out-of-fold probability outputs were combined with demographic metadata in a LightGBM stacking meta-model, and event-level predictions were aggregated to the patient level using ensemble voting. Results: At the event level, the screening model achieved an ROC-AUC of 0.96 (95% CI, 0.95-0.97), the sound-pattern recognition model a macro ROC-AUC of 0.96 (95% CI, 0.96-0.97), and the disease-group prediction model a macro ROC-AUC of 0.94 (95% CI, 0.93-0.94). At the patient level, disease-group classification yielded an accuracy of 0.74 (95% CI, 0.71-0.77), a weighted F1-score of 0.73, and a macro ROC-AUC of 0.91 (95% CI, 0.90-0.93). Stacking improved performance across all tasks compared with base models alone. Conclusions: PulmoVec links event-level acoustic phenotyping with patient-level clinical classification, supporting the potential of foundation-model-based digital auscultation in pediatric respiratory medicine. Multi-center external validation across devices and real-world conditions remains essential.
Submission history
From: Izzet Turkalp Akbasli [view email][v1] Sun, 15 Mar 2026 21:13:47 UTC (1,275 KB)
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
