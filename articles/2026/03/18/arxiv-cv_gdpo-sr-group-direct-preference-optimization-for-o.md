---
title: "GDPO-SR: Group Direct Preference Optimization for One-Step Generative Image Super-Resolution"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16769"
published: "2026-03-18"
fetched: "2026-03-18T18:20:21.354165"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 16 Mar 2026]
Title:GDPO-SR: Group Direct Preference Optimization for One-Step Generative Image Super-Resolution
View PDF HTML (experimental)Abstract:Recently, reinforcement learning (RL) has been employed for improving generative image super-resolution (ISR) performance. However, the current efforts are focused on multi-step generative ISR, while one-step generative ISR remains underexplored due to its limited stochasticity. In addition, RL methods such as Direct Preference Optimization (DPO) require the generation of positive and negative sample pairs offline, leading to a limited number of samples, while Group Relative Policy Optimization (GRPO) only calculates the likelihood of the entire image, ignoring local details that are crucial for ISR. In this paper, we propose Group Direct Preference Optimization (GDPO), a novel approach to integrate RL into one-step generative ISR model training. First, we introduce a noise-aware one-step diffusion model that can generate diverse ISR outputs. To prevent performance degradation caused by noise injection, we introduce an unequal-timestep strategy to decouple the timestep of noise addition from that of diffusion. We then present the GDPO strategy, which integrates the principle of GRPO into DPO, to calculate the group-relative advantage of each online generated sample for model optimization. Meanwhile, an attribute-aware reward function is designed to dynamically evaluate the score of each sample based on its statistics of smooth and texture areas. Experiments demonstrate the effectiveness of GDPO in enhancing the performance of one-step generative ISR models. Code: this https URL.
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
