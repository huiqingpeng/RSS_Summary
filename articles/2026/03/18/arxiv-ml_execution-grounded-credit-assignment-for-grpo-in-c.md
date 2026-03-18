---
title: "Execution-Grounded Credit Assignment for GRPO in Code Generation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16158"
published: "2026-03-18"
fetched: "2026-03-18T15:41:14.466309"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:Execution-Grounded Credit Assignment for GRPO in Code Generation
View PDF HTML (experimental)Abstract:Critic-free reinforcement learning with verifiable rewards (RLVR) improves code generation by optimizing unit-test pass rates, but GRPO-style updates suffer from coarse credit assignment: a single outcome signal is spread uniformly across long programs even when failure stems from a localized semantic error. We propose Execution-Grounded Credit Assignment (EGCA), which localizes GRPO updates using execution traces. For programs that satisfy algorithmic constraints but fail tests, EGCA executes the candidate and a canonical reference solution (curated once offline; used for analysis, not supervision) under identical instrumentation, identifies the earliest semantic divergence, and assigns advantage only to the corresponding token span while masking downstream tokens. EGCA is a drop-in modification requiring no critic, auxiliary loss, or learned verifier, yielding 82.1% pass@1 on HumanEval (+3.1 over GRPO) and 68.9% on MBPP (+1.5) with 18% wall-clock overhead.
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
