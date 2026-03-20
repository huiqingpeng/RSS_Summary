---
title: "Context Bootstrapped Reinforcement Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18953"
published: "2026-03-20"
fetched: "2026-03-20T12:17:03.528090"
---

Computer Science > Machine Learning
[Submitted on 19 Mar 2026]
Title:Context Bootstrapped Reinforcement Learning
View PDF HTML (experimental)Abstract:Reinforcement Learning from Verifiable Rewards (RLVR) suffers from exploration inefficiency, where models struggle to generate successful rollouts, resulting in minimal learning signal. This challenge is particularly severe for tasks that require the acquisition of novel reasoning patterns or domain-specific knowledge. To address this, we propose Context Bootstrapped Reinforcement Learning (CBRL), which augments RLVR training by stochastically prepending few-shot demonstrations to training prompts. The injection probability follows a curriculum that starts high to bootstrap early exploration, then anneals to zero so the model must ultimately succeed without assistance. This forces the policy to internalize reasoning patterns from the demonstrations rather than relying on them at test time. We validate CBRL across two model families and five Reasoning Gym tasks. Our results demonstrate that CBRL consistently improves success rate, provides better exploration efficiency, and is algorithm-agnostic. We further demonstrate CBRL's practical applicability on Q, a domain-specific programming language that diverges significantly from mainstream language conventions.
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
