---
title: "A Deep Dive into Scaling RL for Code Generation with Synthetic Data and Curricula"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24202"
published: "2026-03-26"
fetched: "2026-03-27T07:21:41.230718"
---

Computer Science > Machine Learning
[Submitted on 25 Mar 2026]
Title:A Deep Dive into Scaling RL for Code Generation with Synthetic Data and Curricula
View PDF HTML (experimental)Abstract:Reinforcement learning (RL) has emerged as a powerful paradigm for improving large language models beyond supervised fine-tuning, yet sustaining performance gains at scale remains an open challenge, as data diversity and structure, rather than volume alone, become the limiting factor. We address this by introducing a scalable multi-turn synthetic data generation pipeline in which a teacher model iteratively refines problems based on in-context student performance summaries, producing structured difficulty progressions without any teacher fine-tuning. Compared to single-turn generation, this multi-turn approach substantially improves the yield of valid synthetic problems and naturally produces stepping stones, i.e. easier and harder variants of the same core task, that support curriculum-based training. We systematically study how task difficulty, curriculum scheduling, and environment diversity interact during RL training across the Llama3.1-8B Instruct and Qwen3-8B Base model families, with additional scaling experiments on Qwen2.5-32B. Our results show that synthetic augmentation consistently improves in-domain code and in most cases out-of-domain math performance, and we provide empirical insights into how curriculum design and data diversity jointly shape RL training dynamics.
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
