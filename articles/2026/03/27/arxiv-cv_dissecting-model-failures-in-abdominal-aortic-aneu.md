---
title: "Dissecting Model Failures in Abdominal Aortic Aneurysm Segmentation through Explainability-Driven Analysis"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.24801"
published: "2026-03-27"
fetched: "2026-03-28T07:16:52.249006"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 25 Mar 2026]
Title:Dissecting Model Failures in Abdominal Aortic Aneurysm Segmentation through Explainability-Driven Analysis
View PDF HTML (experimental)Abstract:Computed tomography image segmentation of complex abdominal aortic aneurysms (AAA) often fails because the models assign internal focus to irrelevant structures or do not focus on thin, low-contrast targets. Where the model looks is the primary training signal, and thus we propose an Explainable AI (XAI) guided encoder shaping framework. Our method computes a dense, attribution-based encoder focus map ("XAI field") from the final encoder block and uses it in two complementary ways: (i) we align the predicted probability mass to the XAI field to promote agreement between focus and output; and (ii) we route the field into a lightweight refinement pathway and a confidence prior that modulates logits at inference, suppressing distractors while preserving subtle structures. The objective terms serve only as control signals; the contribution is the integration of attribution guidance into representation and decoding. We evaluate clinically validated challenging cases curated for failure-prone scenarios. Compared to a base SAM setup, our implementation yields substantial improvements. The observed gains suggest that explicitly optimizing encoder focus via XAI guidance is a practical and effective principle for reliable segmentation in complex scenarios.
Submission history
From: Abu Noman Md Sakib [view email][v1] Wed, 25 Mar 2026 20:30:03 UTC (39,324 KB)
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
