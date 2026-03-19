---
title: "Learning to See and Act: Task-Aware Virtual View Exploration for Robotic Manipulation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2508.05186"
published: "2026-03-19"
fetched: "2026-03-19T17:05:09.446969"
---

Computer Science > Robotics
[Submitted on 7 Aug 2025 (v1), last revised 18 Mar 2026 (this version, v5)]
Title:Learning to See and Act: Task-Aware Virtual View Exploration for Robotic Manipulation
View PDF HTML (experimental)Abstract:Recent vision-language-action (VLA) models for multi-task robot manipulation often rely on fixed camera setups and shared visual encoders, which limit their performance under occlusions and during cross-task transfer. To address these challenges, we propose Task-aware Virtual View Exploration (TVVE), a framework that learns to select task-relevant virtual camera viewpoints and dynamically re-render observations from a reconstructed scene representation using the selected viewpoints. To enable efficient view selection, we train an exploration policy in a pseudo-environment. In addition, we introduce a Task-aware Mixture-of-Experts (TaskMoE) visual encoder that routes visual features to task-specialized experts, mitigating interference in multi-task learning. To evaluate robustness under distribution shifts, we construct RLBench-OG, an out-of-distribution benchmark with visual perturbations and camera pose variations. Experiments on RLBench and RLBench-OG demonstrate that TVVE achieves higher success rates than strong baselines, while real-robot experiments further confirm its robustness to visual disturbances and unseen instructions. Code and visualizations are available at: this https URL.
Submission history
From: Yongjie Bai [view email][v1] Thu, 7 Aug 2025 09:21:20 UTC (4,998 KB)
[v2] Tue, 21 Oct 2025 15:55:58 UTC (5,035 KB)
[v3] Tue, 28 Oct 2025 03:21:38 UTC (5,036 KB)
[v4] Mon, 24 Nov 2025 03:28:59 UTC (11,003 KB)
[v5] Wed, 18 Mar 2026 07:06:22 UTC (11,075 KB)
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
