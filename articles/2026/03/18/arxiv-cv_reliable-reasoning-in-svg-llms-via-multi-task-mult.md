---
title: "Reliable Reasoning in SVG-LLMs via Multi-Task Multi-Reward Reinforcement Learning"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16189"
published: "2026-03-18"
fetched: "2026-03-18T18:08:04.054869"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:Reliable Reasoning in SVG-LLMs via Multi-Task Multi-Reward Reinforcement Learning
View PDF HTML (experimental)Abstract:With the rapid advancement of vision-language models, an increasing number of studies have explored their potential for SVG generation tasks. Although existing approaches improve performance by constructing large-scale SVG datasets and introducing SVG-specific tokens, they still suffer from limited generalization, redundant paths in code outputs, and a lack of explicit reasoning. In this work, we present CTRL-S (Chain-of-Thought Reinforcement Learning for SVG), a unified framework that introduces a chain-of-thought mechanism to explicitly expose the model's reasoning process during SVG generation. To support this structured reasoning, we construct SVG-Sophia, a high-quality dataset containing 145K samples across SVG code refinement, Text-to-SVG, and Image-to-SVG tasks. By training the model to generate group-level structured SVG code, CTRL-S significantly improves structural coherence and visual fidelity. Furthermore, we adopt the GRPO algorithm and design a multi-reward optimization framework, incorporating DINO, image-text similarity, format, and code efficiency rewards. Through joint multi-reward optimization and multi-task training, our approach systematically enhances overall generation capabilities. Extensive experiments show that CTRL-S outperforms existing methods, achieving higher task success rates, superior SVG code quality, and exceptional visual fidelity.
Submission history
From: Haomin Wang H. Wang [view email][v1] Tue, 17 Mar 2026 07:16:30 UTC (1,518 KB)
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
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
