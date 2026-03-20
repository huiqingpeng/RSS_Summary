---
title: "DuoTeach: Dual Role Self-Teaching for Coarse-to-Fine Decision Coordination in Vision--Language Models"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2511.18415"
published: "2026-03-20"
fetched: "2026-03-20T17:04:25.416282"
---

Computer Science > Multimedia
[Submitted on 23 Nov 2025 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:DuoTeach: Dual Role Self-Teaching for Coarse-to-Fine Decision Coordination in Vision--Language Models
View PDF HTML (experimental)Abstract:Coarse-to-fine path decision-making requires predicting a valid taxonomy path in which earlier decisions constrain later ones. However, existing benchmarks score each level independently, obscuring cross-level validity and consistency. To better align evaluation with this setting, we introduce a Joint Path Decision (JPD) protocol that requires predicting the full path in one call, together with Depth-Weighted Prefix Accuracy (DWPA), a metric family that measures path reliability with tunable emphasis on deeper levels. Under JPD, strong vision-language models (VLMs) frequently produce invalid parent-child pairs and brittle full-path predictions, suggesting that their failures stem not only from incomplete taxonomic knowledge but also from unstable cross-level decision coordination. To address this problem, we propose DuoTeach, a dual-role self-teaching distillation framework that requires no ground-truth labels and reuses the same pretrained VLM in two roles. Its Decision-Conditioned Rollout (DCR) generates more coherent teacher traces by conditioning each level on prior decisions, and distills this coordinated behavior into the student without additional test-time rollouts. Across multiple taxonomy-structured benchmarks and VLM base models, DuoTeach improves in-domain DWPA (alpha = 0.95) by up to 30.24 points and boosts zero-shot performance on unseen taxonomies from 17.17% to 43.66%. Further analyses attribute these gains to improved within-call multi-level decision coordination.
Submission history
From: Wei Yang [view email][v1] Sun, 23 Nov 2025 12:03:09 UTC (1,936 KB)
[v2] Wed, 18 Mar 2026 07:18:32 UTC (4,472 KB)
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
