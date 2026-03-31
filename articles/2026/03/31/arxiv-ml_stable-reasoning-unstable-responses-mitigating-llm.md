---
title: "Stable Reasoning, Unstable Responses: Mitigating LLM Deception via Stability Asymmetry"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26846"
published: "2026-03-31"
fetched: "2026-04-01T07:20:04.138656"
---

Computer Science > Machine Learning
[Submitted on 27 Mar 2026]
Title:Stable Reasoning, Unstable Responses: Mitigating LLM Deception via Stability Asymmetry
View PDF HTML (experimental)Abstract:As Large Language Models (LLMs) expand in capability and application scope, their trustworthiness becomes critical. A vital risk is intrinsic deception, wherein models strategically mislead users to achieve their own objectives. Existing alignment approaches based on chain-of-thought (CoT) monitoring supervise explicit reasoning traces. However, under optimization pressure, models are incentivized to conceal deceptive reasoning, rendering semantic supervision fundamentally unreliable. Grounded in cognitive psychology, we hypothesize that a deceptive LLM maintains a stable internal belief in its CoT while its external response remains fragile under perturbation. We term this phenomenon stability asymmetry and quantify it by measuring the contrast between internal CoT stability and external response stability under perturbation. Building on this structural signature, we propose the Stability Asymmetry Regularization (SAR), a novel alignment objective that penalizes this distributional asymmetry during reinforcement learning. Unlike CoT monitoring, SAR targets the statistical structure of model outputs, rendering it robust to semantic concealment. Extensive experiments confirm that stability asymmetry reliably identifies deceptive behavior, and that SAR effectively suppresses intrinsic deception without degrading general model capability.
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
