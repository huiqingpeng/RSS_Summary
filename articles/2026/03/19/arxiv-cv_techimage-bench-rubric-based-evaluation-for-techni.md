---
title: "TechImage-Bench: Rubric-Based Evaluation for Technical Image Generation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2512.12220"
published: "2026-03-19"
fetched: "2026-03-19T16:29:34.157888"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 13 Dec 2025 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:TechImage-Bench: Rubric-Based Evaluation for Technical Image Generation
View PDF HTML (experimental)Abstract:We study technical image generation, where a model must synthesize information-dense, scientifically precise illustrations from detailed descriptions rather than merely produce visually plausible pictures. To quantify the progress, we introduce TechImage-Bench, a rubric-based benchmark that targets biology schematics, engineering/patent drawings, and general technical illustrations. For 654 figures collected from real textbooks and technical reports, we construct detailed image instructions and a hierarchy of rubrics that decompose correctness into 6,076 criteria and 44,131 binary checks. Rubrics are derived from surrounding text and reference figures using large multimodal models, and are evaluated by an automated LMM-based judge with a principled penalty scheme that aggregates sub-question outcomes into interpretable criterion scores. We benchmark several representative text-to-image models on TechImage-Bench and find that, despite strong open-domain performance, the best base model reaches only 0.801 rubric accuracy and 0.576 criterion score overall, revealing substantial gaps in fine-grained scientific fidelity. Finally, we show that the same rubrics provide actionable supervision: feeding failed checks back into an editing model for iterative refinement boosts a strong generator from 0.660 to 0.865 in rubric accuracy and from 0.382 to 0.697 in criterion score. TechImage-Bench thus offers both a rigorous diagnostic for technical image generation and a scalable signal for improving specification-faithful scientific illustrations.
Submission history
From: Minheng Ni [view email][v1] Sat, 13 Dec 2025 07:13:43 UTC (26,507 KB)
[v2] Wed, 18 Mar 2026 13:36:02 UTC (36,681 KB)
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
