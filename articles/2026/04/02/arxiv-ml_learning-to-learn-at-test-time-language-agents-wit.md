---
title: "Learning to Learn-at-Test-Time: Language Agents with Learnable Adaptation Policies"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00830"
published: "2026-04-02"
fetched: "2026-04-03T07:25:25.530033"
---

Computer Science > Machine Learning
[Submitted on 1 Apr 2026]
Title:Learning to Learn-at-Test-Time: Language Agents with Learnable Adaptation Policies
View PDF HTML (experimental)Abstract:Test-Time Learning (TTL) enables language agents to iteratively refine their performance through repeated interactions with the environment at inference time. At the core of TTL is an adaptation policy that updates the actor policy based on experience from previous episodes, thereby improving future behavior. Existing methods rely on fixed, hand-crafted adaptation policies rather than optimizing them for downstream improvement. We argue that optimal adaptation policies should be learned from task environments, not hand-engineered based on human intuition. To achieve this, we introduce Meta-TTL, a framework that formulates the discovery of effective adaptation policies as a bi-level optimization problem. Within this framework, the inner loop executes the standard TTL process, measuring how effectively a candidate adaptation policy helps an agent correct errors across sequential episodes. Guided by the agent's performance, the outer loop employs evolutionary search over a diverse distribution of training tasks to iteratively refine the adaptation policy. We evaluate Meta-TTL on Jericho and WebArena-Lite across both in-distribution (ID) and out-of-distribution (OOD) settings, using multiple meta-agent backbones. Results on both benchmarks show that Meta-TTL consistently outperforms hand-crafted baselines, suggesting that the optimized adaptation policy encodes transferable strategies that generalize beyond the training task distribution.
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
