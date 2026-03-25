---
title: "SkillRouter: Retrieve-and-Rerank Skill Selection for LLM Agents at Scale"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22455"
published: "2026-03-25"
fetched: "2026-03-26T07:14:41.090460"
---

Computer Science > Machine Learning
[Submitted on 23 Mar 2026]
Title:SkillRouter: Retrieve-and-Rerank Skill Selection for LLM Agents at Scale
View PDF HTML (experimental)Abstract:As LLM agent ecosystems grow, the number of available skills (tools, plugins) has reached tens of thousands, making it infeasible to inject all skills into an agent's context. This creates a need for skill routing -- retrieving the most relevant skills from a large pool given a user task. The problem is compounded by pervasive functional overlap in community skill repositories, where many skills share similar names and purposes yet differ in implementation details. Despite its practical importance, skill routing remains under-explored. Current agent architectures adopt a progressive disclosure design -- exposing only skill names and descriptions to the agent while keeping the full implementation body hidden -- implicitly treating metadata as sufficient for selection. We challenge this assumption through a systematic empirical study on a benchmark of ~$80K skills and 75 expert-verified queries. Our key finding is that the skill body (full implementation text) is the decisive signal: removing it causes 29--44 percentage point degradation across all retrieval methods, and cross-encoder attention analysis reveals 91.7% of attention concentrating on the body field. Motivated by this finding, we propose SkillRouter, a two-stage retrieve-and-rerank pipeline totaling only 1.2B parameters (0.6B encoder + 0.6B reranker). SkillRouter achieves 74.0% top-1 routing accuracy and delivers the strongest average result among the compact and zero-shot baselines we evaluate, while remaining deployable on consumer hardware.
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
