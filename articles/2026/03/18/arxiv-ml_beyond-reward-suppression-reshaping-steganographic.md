---
title: "Beyond Reward Suppression: Reshaping Steganographic Communication Protocols in MARL via Dynamic Representational Circuit Breaking"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15655"
published: "2026-03-18"
fetched: "2026-03-18T15:33:19.283100"
---

Computer Science > Machine Learning
[Submitted on 7 Mar 2026]
Title:Beyond Reward Suppression: Reshaping Steganographic Communication Protocols in MARL via Dynamic Representational Circuit Breaking
View PDF HTML (experimental)Abstract:In decentralized Multi-Agent Reinforcement Learning (MARL), steganographic collusion -- where agents develop private protocols to evade monitoring -- presents a critical AI safety threat. Existing defenses, limited to behavioral or reward layers, fail to detect coordination in latent communication channels. We introduce the Dynamic Representational Circuit Breaker (DRCB), an architectural defense operating at the optimization substrate.
Building on the AI Mother Tongue (AIM) framework, DRCB utilizes a Vector Quantized Variational Autoencoder (VQ-VAE) bottleneck to convert unobservable messages into auditable statistical objects. DRCB monitors signals including Jensen-Shannon Divergence drift, L2-norm codebook displacement, and Randomized Observer Pool accuracy to compute an EMA-based Collusion Score. Threshold breaches trigger four escalating interventions: dynamic adaptation, gradient-space penalty injection into the Advantage function A^pi, temporal reward suppression, and full substrate circuit breaking via codebook shuffling and optimizer state reset.
Experiments on a Contextual Prisoner's Dilemma with MNIST labels show that while static monitoring fails (p = 0.3517), DRCB improves observer mean accuracy from 0.858 to 0.938 (+9.3 percent) and reduces volatility by 43 percent, while preserving mean joint reward (p = 0.854). Analysis of 214,298 symbol samples confirms "Semantic Degradation," where high-frequency sequences converge to zero entropy, foreclosing complex steganographic encodings. We identify a "Transparency Paradox" where agents achieve surface-level determinism while preserving residual capacity in long-tail distributions, reflecting Goodhart's Law. This task-agnostic methodology provides a technical path toward MICA-compliant (Multi-Agent Internal Coupling Audit) pre-deployment auditing for autonomous systems.
Current browse context:
cs.LG
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
