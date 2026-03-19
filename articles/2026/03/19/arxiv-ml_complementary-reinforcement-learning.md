---
title: "Complementary Reinforcement Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17621"
published: "2026-03-19"
fetched: "2026-03-19T12:14:40.142310"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:Complementary Reinforcement Learning
View PDF HTML (experimental)Abstract:Reinforcement Learning (RL) has emerged as a powerful paradigm for training LLM-based agents, yet remains limited by low sample efficiency, stemming not only from sparse outcome feedback but also from the agent's inability to leverage prior experience across episodes. While augmenting agents with historical experience offers a promising remedy, existing approaches suffer from a critical weakness: the experience distilled from history is either stored statically or fail to coevolve with the improving actor, causing a progressive misalignment between the experience and the actor's evolving capability that diminishes its utility over the course of training. Inspired by complementary learning systems in neuroscience, we present Complementary RL to achieve seamless co-evolution of an experience extractor and a policy actor within the RL optimization loop. Specifically, the actor is optimized via sparse outcome-based rewards, while the experience extractor is optimized according to whether its distilled experiences demonstrably contribute to the actor's success, thereby evolving its experience management strategy in lockstep with the actor's growing capabilities. Empirically, Complementary RL outperforms outcome-based agentic RL baselines that do not learn from experience, achieving 10% performance improvement in single-task scenarios and exhibits robust scalability in multi-task settings. These results establish Complementary RL as a paradigm for efficient experience-driven agent learning.
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
