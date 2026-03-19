---
title: "Where MLLMs Attend and What They Rely On: Explaining Autoregressive Token Generation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2509.22496"
published: "2026-03-19"
fetched: "2026-03-19T16:25:46.951622"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 26 Sep 2025 (v1), last revised 18 Mar 2026 (this version, v5)]
Title:Where MLLMs Attend and What They Rely On: Explaining Autoregressive Token Generation
View PDF HTML (experimental)Abstract:Multimodal large language models (MLLMs) have demonstrated remarkable capabilities in aligning visual inputs with natural language outputs. Yet, the extent to which generated tokens depend on visual modalities remains poorly understood, limiting interpretability and reliability. In this work, we present EAGLE, a lightweight black-box framework for explaining autoregressive token generation in MLLMs. EAGLE attributes any selected tokens to compact perceptual regions while quantifying the relative influence of language priors and perceptual evidence. The framework introduces an objective function that unifies sufficiency (insight score) and indispensability (necessity score), optimized via greedy search over sparsified image regions for faithful and efficient attribution. Beyond spatial attribution, EAGLE performs modality-aware analysis that disentangles what tokens rely on, providing fine-grained interpretability of model decisions. Extensive experiments across open-source MLLMs show that EAGLE consistently outperforms existing methods in faithfulness, localization, and hallucination diagnosis, while requiring substantially less GPU memory. These results highlight its effectiveness and practicality for advancing the interpretability of MLLMs.
Submission history
From: Ruoyu Chen [view email][v1] Fri, 26 Sep 2025 15:38:42 UTC (31,024 KB)
[v2] Fri, 17 Oct 2025 07:14:57 UTC (30,972 KB)
[v3] Sat, 3 Jan 2026 06:21:43 UTC (31,216 KB)
[v4] Wed, 7 Jan 2026 03:38:30 UTC (31,216 KB)
[v5] Wed, 18 Mar 2026 11:46:46 UTC (31,214 KB)
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
