---
title: "From Broad Exploration to Stable Synthesis: Entropy-Guided Optimization for Autoregressive Image Generation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.02355"
published: "2026-04-07"
fetched: "2026-04-08T07:02:37.629304"
---

Computer Science > Machine Learning
[Submitted on 12 Mar 2026]
Title:From Broad Exploration to Stable Synthesis: Entropy-Guided Optimization for Autoregressive Image Generation
View PDF HTML (experimental)Abstract:Combining Chain-of-Thought (CoT) with Reinforcement Learning (RL) improves text-to-image (T2I) generation, yet the underlying interaction between CoT's exploration and RL's optimization remains unclear. We present a systematic entropy-based analysis that yields three key insights: (1) CoT expands the generative exploration space, while RL contracts it toward high-reward regions; (2) final reward is strongly negatively correlated with both the mean and variance of image-token entropy, highlighting the need to reduce uncertainty and instability; and (3) the entropy of the textual CoT directly governs downstream image quality, with lower-entropy CoTs leading to better generations. Motivated by these findings, we propose Entropy-Guided Group Relative Policy Optimization (EG-GRPO), a fine-tuning strategy that reallocates optimization budget by uncertainty: low-entropy tokens are excluded from reward-driven updates to preserve stability, while high-entropy tokens receive an entropy bonus that encourages structured exploration without collapse. Experiments on standard T2I benchmarks demonstrate that EG-GRPO achieves state-of-the-art performance.
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
