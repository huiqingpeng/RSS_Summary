---
title: "Flow Matching Policy with Entropy Regularization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17685"
published: "2026-03-19"
fetched: "2026-03-19T12:15:14.687843"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:Flow Matching Policy with Entropy Regularization
View PDF HTML (experimental)Abstract:Diffusion-based policies have gained significant popularity in Reinforcement Learning (RL) due to their ability to represent complex, non-Gaussian distributions. Stochastic Differential Equation (SDE)-based diffusion policies often rely on indirect entropy control due to the intractability of the exact entropy, while also suffering from computationally prohibitive policy gradients through the iterative denoising chain. To overcome these issues, we propose Flow Matching Policy with Entropy Regularization (FMER), an Ordinary Differential Equation (ODE)-based online RL framework. FMER parameterizes the policy via flow matching and samples actions along a straight probability path, motivated by optimal transport. FMER leverages the model's generative nature to construct an advantage-weighted target velocity field from a candidate set, steering policy updates toward high-value regions. By deriving a tractable entropy objective, FMER enables principled maximum-entropy optimization for enhanced exploration. Experiments on sparse multi-goal FrankaKitchen benchmarks demonstrate that FMER outperforms state-of-the-art methods, while remaining competitive on standard MuJoco benchmarks. Moreover, FMER reduces training time by 7x compared to heavy diffusion baselines (QVPO) and 10-15% relative to efficient variants.
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
