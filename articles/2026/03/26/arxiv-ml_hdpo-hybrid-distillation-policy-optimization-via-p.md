---
title: "HDPO: Hybrid Distillation Policy Optimization via Privileged Self-Distillation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23871"
published: "2026-03-26"
fetched: "2026-03-27T07:18:18.657487"
---

Computer Science > Machine Learning
[Submitted on 25 Mar 2026]
Title:HDPO: Hybrid Distillation Policy Optimization via Privileged Self-Distillation
View PDF HTML (experimental)Abstract:Large language models trained with reinforcement learning (RL) for mathematical reasoning face a fundamental challenge: on problems the model cannot solve at all - "cliff" prompts - the RL gradient vanishes entirely, preventing any learning signal from reaching these failure modes. We introduce Hybrid Distillation Policy Optimization (HDPO), which augments standard RL with privileged self-distillation targeting cliff prompts. On each training step, HDPO identifies prompts where all rollouts fail, generates privileged rollouts by providing the model with ground-truth information, filters for correct solutions, and distills the teacher's token-level distribution into the student. Because teacher and student share the same weights - differing only in their input - the realizability gap is provably bounded, unlike cross-model distillation. We prove that R=1 filtered privileged generation recovers the optimal KL-regularized RL policy in the hard-threshold limit. Experiments on OpenMathInstruct-2 with Qwen2.5-Math-1.5B-Instruct show that HDPO consistently improves coverage metrics (pass@4 by +0.8-1.1%, pass@8 by +0.4-1.7%) while maintaining greedy accuracy, with the distillation weight lambda providing direct control over the exploration-exploitation tradeoff.
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
