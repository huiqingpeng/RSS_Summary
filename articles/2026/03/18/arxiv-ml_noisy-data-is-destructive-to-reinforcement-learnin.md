---
title: "Noisy Data is Destructive to Reinforcement Learning with Verifiable Rewards"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16140"
published: "2026-03-18"
fetched: "2026-03-18T15:40:44.491492"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:Noisy Data is Destructive to Reinforcement Learning with Verifiable Rewards
View PDF HTML (experimental)Abstract:Reinforcement learning with verifiable rewards (RLVR) has driven recent capability advances of large language models across various domains. Recent studies suggest that improved RLVR algorithms allow models to learn effectively from incorrect annotations, achieving performance comparable to learning from clean data. In this work, we show that these findings are invalid because the claimed 100% noisy training data is "contaminated" with clean data. After rectifying the dataset with a rigorous re-verification pipeline, we demonstrate that noise is destructive to RLVR. We show that existing RLVR algorithm improvements fail to mitigate the impact of noise, achieving similar performance to that of the basic GRPO. Furthermore, we find that the model trained on truly incorrect annotations performs 8-10% worse than the model trained on clean data across mathematical reasoning benchmarks. Finally, we show that these findings hold for real-world noise in Text2SQL tasks, where training on real-world, human annotation errors cause 5-12% lower accuracy than clean data. Our results show that current RLVR methods cannot yet compensate for poor data quality. High-quality data remains essential.
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
