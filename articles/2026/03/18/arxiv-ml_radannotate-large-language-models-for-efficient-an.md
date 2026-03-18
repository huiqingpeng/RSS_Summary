---
title: "RadAnnotate: Large Language Models for Efficient and Reliable Radiology Report Annotation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16002"
published: "2026-03-18"
fetched: "2026-03-18T16:09:20.318387"
---

Computer Science > Computation and Language
[Submitted on 16 Mar 2026]
Title:RadAnnotate: Large Language Models for Efficient and Reliable Radiology Report Annotation
View PDF HTML (experimental)Abstract:Radiology report annotation is essential for clinical NLP, yet manual labeling is slow and costly. We present RadAnnotate, an LLM-based framework that studies retrieval-augmented synthetic reports and confidence-based selective automation to reduce expert effort for labeling in RadGraph. We study RadGraph-style entity labeling (graph nodes) and leave relation extraction (edges) to future work. First, we train entity-specific classifiers on gold-standard reports and characterize their strengths and failure modes across anatomy and observation categories, with uncertain observations hardest to learn. Second, we generate RAG-guided synthetic reports and show that synthetic-only models remain within 1-2 F1 points of gold-trained models, and that synthetic augmentation is especially helpful for uncertain observations in a low-resource setting, improving F1 from 0.61 to 0.70. Finally, by learning entity-specific confidence thresholds, RadAnnotate can automatically annotate 55-90% of reports at 0.86-0.92 entity match score while routing low-confidence cases for expert review.
Submission history
From: Saisha Pradeep Shetty [view email][v1] Mon, 16 Mar 2026 23:23:23 UTC (347 KB)
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
