---
title: "When Validation Fails: Cross-Institutional Blood Pressure Prediction and the Limits of Electronic Health Record-Based Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2507.19530"
published: "2026-03-20"
fetched: "2026-03-20T14:06:41.480498"
---

Computer Science > Machine Learning
[Submitted on 21 Jul 2025 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:When Validation Fails: Cross-Institutional Blood Pressure Prediction and the Limits of Electronic Health Record-Based Models
View PDF HTML (experimental)Abstract:External validation remains rare in healthcare machine learning despite being critical for establishing real-world feasibility. We developed an ensemble framework to predict blood pressure from electronic health records, incorporating rigorous data leakage prevention. Internal validation on the MIMIC-III dataset yielded moderate performance for systolic (R^2 = 0.248, RMSE = 14.84 mmHg) and diastolic (R^2 = 0.297, RMSE = 8.27 mmHg) blood pressure. However, external validation on the eICU dataset revealed substantial generalization challenges. Baseline systolic performance dropped significantly from R^2 = 0.248 to -0.024, with RMSE increasing from 14.84 to 18.69 mmHg. To address potential confounding from feature imputation, we conducted an intersection-only experiment using 16 universally available features; this yielded worse external performance (R^2 = -0.115, RMSE = 17.32 mmHg), proving imputation artifacts were not the primary cause. Attempts at post-hoc correction, including linear and isotonic recalibration (R^2 ranging from -0.170 to 0.024) and domain adaptation via covariate shift reweighting (R^2 = -0.141), showed limited gains. This highlights fundamental cross-institutional barriers. Our root-cause analysis identified three primary obstacles to generalizability: (1) site-specific feature distributions, even among standard physiological variables; (2) underlying patient population differences with unique pathophysiologies; and (3) institutional variations in measurement protocols creating non-transferable learned patterns. These findings demonstrate that strong internal performance cannot guarantee cross-institutional deployment success. Transparent reporting of validation failures is essential for setting realistic expectations for predictive models. Code is available at this https URL.
Submission history
From: Md Basit Azam [view email][v1] Mon, 21 Jul 2025 11:15:33 UTC (2,863 KB)
[v2] Wed, 18 Mar 2026 16:11:21 UTC (762 KB)
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
