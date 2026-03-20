---
title: "Balancing the Reasoning Load: Difficulty-Differentiated Policy Optimization with Length Redistribution for Efficient and Robust Reinforcement Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18533"
published: "2026-03-20"
fetched: "2026-03-20T12:12:23.969768"
---

Computer Science > Machine Learning
[Submitted on 19 Mar 2026]
Title:Balancing the Reasoning Load: Difficulty-Differentiated Policy Optimization with Length Redistribution for Efficient and Robust Reinforcement Learning
View PDF HTML (experimental)Abstract:Large Reasoning Models (LRMs) have shown exceptional reasoning capabilities, but they also suffer from the issue of overthinking, often generating excessively long and redundant answers.
For problems that exceed the model's capabilities, LRMs tend to exhibit the overconfidence phenomenon, generating overly short but incorrect answers, which may contribute to suboptimal performance.
To address these issues, we propose Difficulty-Differentiated Policy Optimization (DDPO), an efficient reinforcement learning algorithm that optimizes simple and complex tasks separately based on the overconfidence phenomenon.
Specifically, it reduces the output length for simple tasks without compromising accuracy, while for complex tasks, it expands the exploration space to improve performance. We further derive the theoretical conditions for maximizing expected accuracy, which require the length distribution to closely approximate the optimal length and be as concentrated as possible. Based on these conditions, we propose using the difficulty-level average as a well-founded reference for length optimization.
Extensive experiments on both in-domain and out-of-domain benchmarks validate the superiority and effectiveness of DDPO. Compared to GRPO, DDPO reduces the average answer length by 12% while improving accuracy by 1.85% across multiple benchmarks, achieving a better trade-off between accuracy and length. The code is available at this https URL.
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
