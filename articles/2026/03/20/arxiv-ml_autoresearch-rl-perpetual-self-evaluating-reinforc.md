---
title: "AutoResearch-RL: Perpetual Self-Evaluating Reinforcement Learning Agents for Autonomous Neural Architecture Discovery"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.07300"
published: "2026-03-20"
fetched: "2026-03-20T14:12:07.962365"
---

Computer Science > Machine Learning
This paper has been withdrawn by arXiv Admin
[Submitted on 7 Mar 2026 (v1), last revised 19 Mar 2026 (this version, v2)]
Title:AutoResearch-RL: Perpetual Self-Evaluating Reinforcement Learning Agents for Autonomous Neural Architecture Discovery
No PDF available, click to view other formatsAbstract:We present AutoResearch-RL, a framework in which a reinforcement learning agent conducts open-ended neural architecture and hyperparameter research without human supervision, running perpetually until a termination oracle signals convergence or resource exhaustion. At each step the agent proposes a code modification to a target training script, executes it under a fixed wall clock time budget, observes a scalar reward derived from validation bits-per-byte (val-bpb), and updates its policy via Proximal Policy Optimisation (PPO).
The key design insight is the separation of three concerns: (i) a frozen environment (data pipeline, evaluation protocol, and constants) that guarantees fair cross-experiment comparison; (ii) a mutable target file (this http URL) that represents the agent's editable state; and (iii) a meta-learner (the RL agent itself) that accumulates a growing trajectory of experiment outcomes and uses them to inform subsequent proposals.
We formalise this as a Markov Decision Process, derive convergence guarantees under mild assumptions, and demonstrate empirically on a single GPU nanochat pretraining benchmark that AutoResearch-RL discovers configurations that match or exceed hand-tuned baselines after approximately 300 overnight iterations, with no human in the loop.
Submission history
From: arXiv Admin [view email][v1] Sat, 7 Mar 2026 17:49:44 UTC (14 KB)
[v2] Thu, 19 Mar 2026 13:59:07 UTC (1 KB) (withdrawn)
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
