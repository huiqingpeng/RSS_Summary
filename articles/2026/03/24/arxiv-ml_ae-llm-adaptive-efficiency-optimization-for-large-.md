---
title: "AE-LLM: Adaptive Efficiency Optimization for Large Language Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20492"
published: "2026-03-24"
fetched: "2026-03-25T07:10:31.157876"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:AE-LLM: Adaptive Efficiency Optimization for Large Language Models
View PDF HTML (experimental)Abstract:Large Language Models (LLMs) have achieved remarkable success across diverse applications, yet their deployment remains challenging due to substantial computational costs, memory requirements, and energy consumption. Recent empirical studies have demonstrated that no single efficiency technique is universally optimal; instead, the effectiveness of methods such as efficient attention mechanisms, mixture-of-experts (MoE), parameter-efficient fine-tuning, and quantization varies significantly depending on task characteristics, resource constraints, and model scales. Building upon these insights, we propose AE-LLM, a unified framework that automatically selects and combines optimal efficiency techniques tailored to specific deployment scenarios. Our approach introduces a multi-objective optimization framework that jointly considers accuracy, latency, memory footprint, and energy consumption, while accounting for hardware constraints and task requirements. We develop an efficient search algorithm that explores the combinatorial space of efficiency techniques across architecture, fine-tuning, and inference stages, identifying Pareto-optimal configurations. Extensive experiments across 15 models (0.5B-70B parameters) and 10 diverse tasks demonstrate that AE-LLM achieves an average of $2.8\times$ improvement in efficiency metrics while maintaining competitive accuracy (within 1.2\% of baseline), compared to static efficiency configurations. Furthermore, our framework generalizes effectively to vision-language models, achieving similar efficiency gains. Our contributions provide practitioners with an automated tool for navigating the complex trade-off landscape of LLM efficiency optimization.
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
