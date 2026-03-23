---
title: "NASimJax: GPU-Accelerated Policy Learning Framework for Penetration Testing"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19864"
published: "2026-03-23"
fetched: "2026-03-24T07:22:50.383400"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:NASimJax: GPU-Accelerated Policy Learning Framework for Penetration Testing
View PDF HTML (experimental)Abstract:Penetration testing, the practice of simulating cyberattacks to identify vulnerabilities, is a complex sequential decision-making task that is inherently partially observable and features large action spaces. Training reinforcement learning (RL) policies for this domain faces a fundamental bottleneck: existing simulators are too slow to train on realistic network scenarios at scale, resulting in policies that fail to generalize. We present NASimJax, a complete JAX-based reimplementation of the Network Attack Simulator (NASim), achieving up to 100x higher environment throughput than the original simulator. By running the entire training pipeline on hardware accelerators, NASimJax enables experimentation on larger networks under fixed compute budgets that were previously infeasible. We formulate automated penetration testing as a Contextual POMDP and introduce a network generation pipeline that produces structurally diverse and guaranteed-solvable scenarios. Together, these provide a principled basis for studying zero-shot policy generalization. We use the framework to investigate action-space scaling and generalization across networks of up to 40 hosts. We find that Prioritized Level Replay better handles dense training distributions than Domain Randomization, particularly at larger scales, and that training on sparser topologies yields an implicit curriculum that improves out-of-distribution generalization, even on topologies denser than those seen during training. To handle linearly growing action spaces, we propose a two-stage action decomposition (2SAS) that substantially outperforms flat action masking at scale. Finally, we identify a failure mode arising from the interaction between Prioritized Level Replay's episode-reset behaviour and 2SAS's credit assignment structure. NASimJax thus provides a fast, flexible, and realistic platform for advancing RL-based penetration testing.
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
