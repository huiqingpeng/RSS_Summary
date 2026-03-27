---
title: "MoE-GRPO: Optimizing Mixture-of-Experts via Reinforcement Learning in Vision-Language Models"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.24984"
published: "2026-03-27"
fetched: "2026-03-28T07:19:16.814050"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 26 Mar 2026]
Title:MoE-GRPO: Optimizing Mixture-of-Experts via Reinforcement Learning in Vision-Language Models
View PDF HTML (experimental)Abstract:Mixture-of-Experts (MoE) has emerged as an effective approach to reduce the computational overhead of Transformer architectures by sparsely activating a subset of parameters for each token while preserving high model capacity. This paradigm has recently been extended to Vision-Language Models (VLMs), enabling scalable multi-modal understanding with reduced computational cost. However, the widely adopted deterministic top-K routing mechanism may overlook more optimal expert combinations and lead to expert overfitting. To address this limitation and improve the diversity of expert selection, we propose MoE-GRPO, a reinforcement learning (RL)-based framework for optimizing expert routing in MoE-based VLMs. Specifically, we formulate expert selection as a sequential decision-making problem and optimize it using Group Relative Policy Optimization (GRPO), allowing the model to learn adaptive expert routing policies through exploration and reward-based feedback. Furthermore, we introduce a modality-aware router guidance that enhances training stability and efficiency by discouraging the router from exploring experts that are infrequently activated for a given modality. Extensive experiments on multi-modal image and video benchmarks show that MoE-GRPO consistently outperforms standard top-K routing and its variants by promoting more diverse expert selection, thereby mitigating expert overfitting and enabling a task-level expert specialization.
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
