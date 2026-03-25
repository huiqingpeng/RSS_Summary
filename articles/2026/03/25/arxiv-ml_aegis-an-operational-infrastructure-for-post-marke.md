---
title: "AEGIS: An Operational Infrastructure for Post-Market Governance of Adaptive Medical AI Under US and EU Regulations"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22322"
published: "2026-03-25"
fetched: "2026-03-26T07:11:01.139383"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:AEGIS: An Operational Infrastructure for Post-Market Governance of Adaptive Medical AI Under US and EU Regulations
View PDF HTML (experimental)Abstract:Machine learning systems deployed in medical devices require governance frameworks that ensure safety while enabling continuous improvement. Regulatory bodies including the FDA and European Union have introduced mechanisms such as the Predetermined Change Control Plan (PCCP) and Post-Market Surveillance (PMS) to manage iterative model updates without repeated submissions. This paper presents AI/ML Evaluation and Governance Infrastructure for Safety (AEGIS), a governance framework applicable to any healthcare AI system. AEGIS comprises three modules, i.e., dataset assimilation and retraining, model monitoring, and conditional decision, that operationalize FDA PCCP and EU AI Act Article 43(4) provisions. We implement a four-category deployment decision taxonomy (APPROVE, CONDITIONAL APPROVAL, CLINICAL REVIEW, REJECT) with an independent PMS ALARM signal, enabling detection of the critical state in which no deployable model exists while the released model is simultaneously at risk.
To illustrate how AEGIS can be instantiated across heterogeneous clinical contexts, we provide two examples: sepsis prediction from electronic health records and brain tumor segmentation from medical imaging. Both cases use identical governance architecture, differing only in configuration. Across 11 simulated iterations on the sepsis example, AEGIS yielded 8 APPROVE, 1 CONDITIONAL APPROVAL, 1 CLINICAL REVIEW, and 1 REJECT decision, exercising all four categories. ALARM signals were co-issued at iterations 8 and 10, including the critical state where no deployable model exists and the released model is simultaneously failing. AEGIS detected drift before observable performance degradation. These results demonstrate that AEGIS translates regulatory change-control concepts into executable governance procedures, supporting safe continuous learning for adaptive medical AI across diverse clinical applications.
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
