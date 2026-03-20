---
title: "ELM: A Hybrid Ensemble of Language Models for Automated Tumor Group Classification in Population-Based Cancer Registries"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2503.21800"
published: "2026-03-20"
fetched: "2026-03-20T14:15:10.750849"
---

Computer Science > Computation and Language
[Submitted on 24 Mar 2025 (v1), last revised 19 Mar 2026 (this version, v2)]
Title:ELM: A Hybrid Ensemble of Language Models for Automated Tumor Group Classification in Population-Based Cancer Registries
View PDF HTML (experimental)Abstract:Background: Population-based cancer registries (PBCRs) manually extract data from unstructured pathology reports, a labor-intensive process where assigning reports to tumor groups can consume 900 person-hours annually for approximately 100,000 reports at a medium-sized registry. Current automated rule-based systems fail to handle the linguistic complexity of this classification task.
Materials and Methods: We present ELM (Ensemble of Language Models), a novel hybrid approach combining small, encoder only language models and large language models (LLMs). ELM employs an ensemble of six fine-tuned encoder only models: three analyzing the top portion and three analyzing the bottom portion of each report to maximize text coverage given token limits. A tumor group is assigned when at least five of six models agree; otherwise, an LLM arbitrates using a carefully curated prompt constrained to likely tumor groups.
Results: On a held-out test set of 2,058 pathology reports spanning 19 tumor groups, ELM achieves weighted precision and recall of 0.94, representing a statistically significant improvement (p<0.001) over encoder-only ensembles (0.91 F1-score) and substantially outperforming rule-based approaches. ELM demonstrates particular gains for challenging categories including leukemia (F1: 0.76 to 0.88), lymphoma (0.76 to 0.89), and skin cancer (0.44 to 0.58).
Discussion: Deployed in production at British Columbia Cancer Registry, ELM has reduced manual review requirements by approximately 60-70%, saving an estimated 900 person-hours annually while maintaining data quality standards.
Conclusion: ELM represents the first successful deployment of a hybrid small, encoder only models-LLM architecture for tumor group classification in a real-world PBCR setting, demonstrating how strategic combination of language models can achieve both high accuracy and operational efficiency.
Submission history
From: Lovedeep Gondara [view email][v1] Mon, 24 Mar 2025 19:21:53 UTC (190 KB)
[v2] Thu, 19 Mar 2026 00:26:07 UTC (183 KB)
Current browse context:
cs.CL
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
