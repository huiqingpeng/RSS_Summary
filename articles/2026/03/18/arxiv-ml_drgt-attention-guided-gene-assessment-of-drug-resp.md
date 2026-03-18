---
title: "drGT: Attention-Guided Gene Assessment of Drug Response Utilizing a Drug-Cell-Gene Heterogeneous Network"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2405.08979"
published: "2026-03-18"
fetched: "2026-03-18T16:15:59.638731"
---

Computer Science > Machine Learning
[Submitted on 14 May 2024 (v1), last revised 17 Mar 2026 (this version, v4)]
Title:drGT: Attention-Guided Gene Assessment of Drug Response Utilizing a Drug-Cell-Gene Heterogeneous Network
View PDFAbstract:For translational impact, both accurate drug response prediction and biological plausibility of predictive features are needed. We present drGT, a heterogeneous graph deep learning model over drugs, genes, and cell lines that couples prediction with mechanism-oriented interpretability via attention coefficients (ACs).
We assess both predictive generalization (random, unseen-drug, unseen-cell, and zero-shot splits) and biological plausibility (use of text-mined PubMed gene-drug co-mentions and comparison to a structure-based DTI predictor) on GDSC, NCI60, and CTRP datasets. Across benchmarks, drGT consistently delivers top regression performance while maintaining competitive classification accuracy for drug sensitivity. Under random 5-fold cross-validation, drGT attains an AUROC of up to 0.945 (3rd overall) and an $R^2$ up to 0.690, outperforming all baselines on regression. In leave-one-out tests for unseen cell lines and drugs, drGT achieves AUROCs of 0.706 and 0.844, and $R^2$ values of 0.692 and 0.022, the only model yielding positive $R^2$ for unseen drugs. In zero-shot prediction, drGT achieves an AUROC of 0.786 and a regression $R^2$ of 0.334, both representing the highest scores among all models. For interpretability, AC-derived drug-gene links recover known biology: among 976 drugs with known DTIs, 36.9% of predicted links match established DTIs, and 63.7% are supported by either PubMed abstracts or a structure-based predictive model. Enrichment analyses of AC-prioritized genes reveal drug-perturbed biological processes, providing pathway-level explanations.
drGT advances predictive generalization and mechanism-centered interpretability, offering state-of-the-art regression accuracy and literature-supported biological hypotheses that demonstrate the use of graph learning from heterogeneous input data for biological discovery. Code: this https URL
Submission history
From: Augustin Luna [view email][v1] Tue, 14 May 2024 22:16:52 UTC (5,054 KB)
[v2] Wed, 27 Aug 2025 20:36:18 UTC (1,766 KB)
[v3] Wed, 11 Mar 2026 18:14:08 UTC (2,184 KB)
[v4] Tue, 17 Mar 2026 16:07:37 UTC (2,184 KB)
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
