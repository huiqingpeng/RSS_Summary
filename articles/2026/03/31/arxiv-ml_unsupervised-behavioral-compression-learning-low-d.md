---
title: "Unsupervised Behavioral Compression: Learning Low-Dimensional Policy Manifolds through State-Occupancy Matching"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.27044"
published: "2026-03-31"
fetched: "2026-04-01T07:21:00.927208"
---

Computer Science > Machine Learning
[Submitted on 27 Mar 2026]
Title:Unsupervised Behavioral Compression: Learning Low-Dimensional Policy Manifolds through State-Occupancy Matching
View PDF HTML (experimental)Abstract:Deep Reinforcement Learning (DRL) is widely recognized as sample-inefficient, a limitation attributable in part to the high dimensionality and substantial functional redundancy inherent to the policy parameter space. A recent framework, which we refer to as Action-based Policy Compression (APC), mitigates this issue by compressing the parameter space $\Theta$ into a low-dimensional latent manifold $\mathcal Z$ using a learned generative mapping $g:\mathcal Z \to \Theta$. However, its performance is severely constrained by relying on immediate action-matching as a reconstruction loss, a myopic proxy for behavioral similarity that suffers from compounding errors across sequential decisions. To overcome this bottleneck, we introduce Occupancy-based Policy Compression (OPC), which enhances APC by shifting behavior representation from immediate action-matching to long-horizon state-space coverage. Specifically, we propose two principal improvements: (1) we curate the dataset generation with an information-theoretic uniqueness metric that delivers a diverse population of policies; and (2) we propose a fully differentiable compression objective that directly minimizes the divergence between the true and reconstructed mixture occupancy distributions. These modifications force the generative model to organize the latent space around true functional similarity, promoting a latent representation that generalizes over a broad spectrum of behaviors while retaining most of the original parameter space's expressivity. Finally, we empirically validate the advantages of our contributions across multiple continuous control benchmarks.
Submission history
From: Davide Tenedini [view email][v1] Fri, 27 Mar 2026 23:16:27 UTC (42,368 KB)
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
