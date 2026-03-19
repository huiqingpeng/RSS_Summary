---
title: "AR-CoPO: Align Autoregressive Video Generation with Contrastive Policy Optimization"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17461"
published: "2026-03-19"
fetched: "2026-03-19T15:11:15.643313"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:AR-CoPO: Align Autoregressive Video Generation with Contrastive Policy Optimization
View PDF HTML (experimental)Abstract:Streaming autoregressive (AR) video generators combined with few-step distillation achieve low-latency, high-quality synthesis, yet remain difficult to align via reinforcement learning from human feedback (RLHF). Existing SDE-based GRPO methods face challenges in this setting: few-step ODEs and consistency model samplers deviate from standard flow-matching ODEs, and their short, low-stochasticity trajectories are highly sensitive to initialization noise, rendering intermediate SDE exploration ineffective. We propose AR-CoPO (AutoRegressive Contrastive Policy Optimization), a framework that adapts the Neighbor GRPO contrastive perspective to streaming AR generation. AR-CoPO introduces chunk-level alignment via a forking mechanism that constructs neighborhood candidates at a randomly selected chunk, assigns sequence-level rewards, and performs localized GRPO updates. We further propose a semi-on-policy training strategy that complements on-policy exploration with exploitation over a replay buffer of reference rollouts, improving generation quality across domains. Experiments on Self-Forcing demonstrate that AR-CoPO improves both out-of-domain generalization and in-domain human preference alignment over the baseline, providing evidence of genuine alignment rather than reward hacking.
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
