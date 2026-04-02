---
title: "Learning Shared Representations for Multi-Task Linear Bandits"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00531"
published: "2026-04-02"
fetched: "2026-04-03T07:22:30.237083"
---

Computer Science > Machine Learning
[Submitted on 1 Apr 2026]
Title:Learning Shared Representations for Multi-Task Linear Bandits
View PDF HTML (experimental)Abstract:Multi-task representation learning is an approach that learns shared latent representations across related tasks, facilitating knowledge transfer and improving sample efficiency. This paper introduces a novel approach to multi-task representation learning in linear bandits. We consider a setting with T concurrent linear bandit tasks, each with feature dimension d, that share a common latent representation of dimension r \ll min{d,T}$, capturing their underlying relatedness. We propose a new Optimism in the Face of Uncertainty Linear (OFUL) algorithm that leverages shared low-rank representations to enhance decision-making in a sample-efficient manner. Our algorithm first collects data through an exploration phase, estimates the shared model via spectral initialization, and then conducts OFUL based learning over a newly constructed confidence set. We provide theoretical guarantees for the confidence set and prove that the unknown reward vectors lie within the confidence set with high probability. We derive cumulative regret bounds and show that the proposed approach achieves \tilde{O}(\sqrt{drNT}), a significant improvement over solving the T tasks independently, resulting in a regret of \tilde{O}(dT\sqrt{N}). We performed numerical simulations to validate the performance of our algorithm for different problem sizes.
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
