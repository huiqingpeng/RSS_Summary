---
title: "Slow-Fast Policy Optimization: Reposition-Before-Update for LLM Reasoning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2510.04072"
published: "2026-03-19"
fetched: "2026-03-19T14:07:24.779319"
---

Computer Science > Machine Learning
[Submitted on 5 Oct 2025 (v1), last revised 17 Mar 2026 (this version, v4)]
Title:Slow-Fast Policy Optimization: Reposition-Before-Update for LLM Reasoning
View PDF HTML (experimental)Abstract:Reinforcement learning (RL) has become central to enhancing reasoning in large language models (LLMs). Yet on-policy algorithms such as Group Relative Policy Optimization (GRPO) often suffer in early training: noisy gradients from low-quality rollouts lead to unstable updates and inefficient exploration. We introduce Slow-Fast Policy Optimization (SFPO), a simple yet efficient framework to address the above limitations via decomposing each step into three stages: a short fast trajectory of inner steps on the same batch, a reposition mechanism to control off-policy drift, and a final slow correction. This reposition-before-update design preserves the objective and rollout process unchanged, making SFPO plug-compatible with existing policy-gradient pipelines. Extensive experiments demonstrate that SFPO consistently improves stability, reduces number of rollouts, and accelerates convergence of reasoning RL training. Specifically, it outperforms GRPO by up to 2.80 points in average on math reasoning benchmarks. It also achieves up to 4.93\texttimes{} fewer rollouts and an up to 4.19\texttimes{} reduction in wall-clock time to match GRPO's best accuracy. Project website is available at this https URL.
Submission history
From: Ziyan Wang [view email][v1] Sun, 5 Oct 2025 07:22:54 UTC (19,748 KB)
[v2] Wed, 8 Oct 2025 04:24:36 UTC (19,748 KB)
[v3] Sun, 15 Mar 2026 05:57:00 UTC (13,570 KB)
[v4] Tue, 17 Mar 2026 22:44:24 UTC (23,889 KB)
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
