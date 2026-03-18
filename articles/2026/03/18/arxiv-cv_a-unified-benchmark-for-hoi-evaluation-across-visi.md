---
title: "A Unified Benchmark for HOI Evaluation across Vision-Language Models and HOI-Specific Methods"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2508.18753"
published: "2026-03-18"
fetched: "2026-03-18T18:26:57.293483"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 26 Aug 2025 (v1), last revised 17 Mar 2026 (this version, v3)]
Title:A Unified Benchmark for HOI Evaluation across Vision-Language Models and HOI-Specific Methods
View PDF HTML (experimental)Abstract:HOI detection has long been dominated by task-specific models, sometimes with early vision-language backbones such as CLIP. With the rise of large generative VLMs, a key question is whether standalone VLMs can perform HOI detection competitively against specialized HOI methods. Existing benchmarks such as HICO-DET require exact label matching under incomplete annotations, so any unmatched prediction is marked wrong. This unfairly penalizes valid outputs, especially from less constrained VLMs, and makes cross-paradigm comparison unreliable. To address this limitation, we introduce CrossHOI-Bench, a multiple-choice HOI benchmark with explicit positives and curated negatives, enabling unified and reliable evaluation of both VLMs and HOI-specific models. We further focus on challenging scenarios, such as multi-person scenes and fine-grained interaction distinctions, which are crucial for revealing real differences between the two paradigms. Experiments show that large VLMs achieve competitive, sometimes superior, zero-shot performance, yet they struggle with multiple concurrent actions and with correctly assigning interactions to the target person. Conversely, HOI-specific methods remain weaker in general HOI reasoning but demonstrate stronger multi-action recognition and more reliable identification of which person performs which action. These findings expose complementary strengths and weaknesses of VLMs and HOI-specific methods, which existing benchmarks fail to reveal due to incorrect penalization.
Submission history
From: Qinqian Lei [view email][v1] Tue, 26 Aug 2025 07:30:53 UTC (498 KB)
[v2] Mon, 29 Sep 2025 05:32:20 UTC (2,735 KB)
[v3] Tue, 17 Mar 2026 12:07:24 UTC (6,211 KB)
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
