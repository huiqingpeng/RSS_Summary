---
title: "Lightweight Fairness for LLM-Based Recommendations via Kernelized Projection and Gated Adapters"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23780"
published: "2026-03-26"
fetched: "2026-03-27T07:16:50.867037"
---

Computer Science > Machine Learning
[Submitted on 24 Mar 2026]
Title:Lightweight Fairness for LLM-Based Recommendations via Kernelized Projection and Gated Adapters
View PDF HTML (experimental)Abstract:Large Language Models (LLMs) have introduced new capabilities to recommender systems, enabling dynamic, context-aware, and conversational recommendations. However, LLM-based recommender systems inherit and may amplify social biases embedded in their pre-training data, especially when demographic cues are present. Existing fairness solutions either require extra parameters fine-tuning, or suffer from optimization instability. We propose a lightweight and scalable bias mitigation method that combines a kernelized Iterative Null-space Projection (INLP) with a gated Mixture-of-Experts (MoE) adapter. Our approach estimates a closed-form projection that removes single or multiple sensitive attributes from LLM representations with no additional trainable parameters. To preserve task utility, we introduce a two-level MoE adapter that selectively restores useful signals without reintroducing bias. Experiments on two public datasets show that our method reduces attribute leakage across multiple protected variables while maintaining competitive recommendation accuracy.
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
