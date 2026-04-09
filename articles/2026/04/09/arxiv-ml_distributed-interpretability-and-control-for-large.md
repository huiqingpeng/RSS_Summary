---
title: "Distributed Interpretability and Control for Large Language Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.06483"
published: "2026-04-09"
fetched: "2026-04-10T07:05:00.891879"
---

Computer Science > Machine Learning
[Submitted on 7 Apr 2026]
Title:Distributed Interpretability and Control for Large Language Models
View PDF HTML (experimental)Abstract:Large language models that require multiple GPU cards to host are usually the most capable models. It is necessary to understand and steer these models, but the current technologies do not support the interpretability and steering of these models in the multi-GPU setting as well as the single-GPU setting. We present a practical implementation of activation-level interpretability (logit lens) and steering (steering vector) that scales up to multi-GPU language models. Our system implements design choices that reduce the activation memory by up to 7x and increase the throughput by up to 41x compared to a baseline on identical hardware. We demonstrate the method across LLaMA-3.1 (8B, 70B) and Qwen-3 (4B, 14B, 32B), sustaining 20-100 tokens/s while collecting full layer-wise activation trajectories for sequences of 1,500 tokens. Using label-position steering vectors injected post-LayerNorm, we show controllable, monotonic shifts in model outputs with a mean steerability slope of 0.702 across evaluated datasets, without fine-tuning or additional forward passes. We release detailed benchmarks, ablations, and a reproducible instrumentation recipe to enable practical interpretability and real-time behavioral control for frontier LLMs at this https URL.
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
