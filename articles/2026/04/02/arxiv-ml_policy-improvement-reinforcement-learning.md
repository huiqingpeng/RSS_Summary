---
title: "Policy Improvement Reinforcement Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00860"
published: "2026-04-02"
fetched: "2026-04-03T07:25:34.422963"
---

Computer Science > Machine Learning
[Submitted on 1 Apr 2026]
Title:Policy Improvement Reinforcement Learning
View PDF HTML (experimental)Abstract:Reinforcement Learning with Verifiable Rewards (RLVR) has become a central post-training paradigm for improving the reasoning capabilities of large language models. Yet existing methods share a common blind spot: they optimize policies based on instantaneous group-level or batch-level statistics without ever verifying whether the resulting update actually improved the model. This open-loop design -- updating in isolation at each step, guided only by within-group (batch) reward signals -- means optimization can drift or collapse with no mechanism to detect and correct these failures. We argue that the missing ingredient is policy improvement feedback: the ability to measure and optimize inter-iteration progress directly. To this end, we introduce Policy Improvement Reinforcement Learning (PIRL), a framework that replaces surrogate reward maximization with the explicit objective of maximizing cumulative policy improvement across iterations, and prove this temporal objective is perfectly aligned with maximizing final task performance. Building on PIRL, we propose Policy Improvement Policy Optimization (PIPO), which implements closed-loop optimization through retrospective verification. At each iteration, PIPO evaluates whether the previous update yielded genuine improvement against a sliding-window historical baseline, then actively reinforces beneficial updates and suppresses the harmful ones -- transforming an open-loop process into a self-correcting one. We provide theoretical analysis showing that PIPO performs ascent on the PIRL objective in expectation, and experiments on mathematical reasoning benchmarks demonstrate improved stability and performance over GRPO and its variants.
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
