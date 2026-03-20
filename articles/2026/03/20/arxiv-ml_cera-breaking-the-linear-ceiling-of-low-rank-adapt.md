---
title: "CeRA: Breaking the Linear Ceiling of Low-Rank Adaptation via Manifold Expansion"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2602.22911"
published: "2026-03-20"
fetched: "2026-03-20T14:11:33.323877"
---

Computer Science > Machine Learning
[Submitted on 26 Feb 2026 (v1), last revised 18 Mar 2026 (this version, v4)]
Title:CeRA: Breaking the Linear Ceiling of Low-Rank Adaptation via Manifold Expansion
View PDF HTML (experimental)Abstract:Low-Rank Adaptation (LoRA) dominates parameter-efficient fine-tuning (PEFT). However, it faces a critical ``linear ceiling'' in complex reasoning tasks: simply increasing the rank yields diminishing returns due to intrinsic linear constraints. We introduce CeRA (Capacity-enhanced Rank Adaptation), a weight-level parallel adapter that injects SiLU gating and structural dropout to induce manifold expansion. On the SlimOrca benchmark, CeRA breaks this linear barrier: at rank 64 (PPL 3.89), it outperforms LoRA at rank 512 (PPL 3.90), demonstrating superior spectral efficiency. This advantage generalizes to downstream mathematical reasoning. We reveal a profound impact of task complexity: In fundamental arithmetic (GSM8K), CeRA matches standard baselines, but in the highly complex MATH dataset, CeRA demonstrates extreme parameter efficiency. Remarkably, CeRA at rank 64 (Pass@1 16.36\%) outperforms LoRA at rank 512 (Pass@1 15.72\%), achieving superior reasoning accuracy with only 1/8 of the parameter budget. Mechanism analysis via Singular Value Decomposition (SVD) confirms that CeRA activates the dormant tail of the singular value spectrum, effectively preventing the rank collapse observed in linear methods.
Submission history
From: Hung-Hsuan Chen [view email][v1] Thu, 26 Feb 2026 11:55:25 UTC (116 KB)
[v2] Mon, 2 Mar 2026 22:35:44 UTC (115 KB)
[v3] Mon, 9 Mar 2026 06:40:14 UTC (115 KB)
[v4] Wed, 18 Mar 2026 23:49:58 UTC (117 KB)
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
