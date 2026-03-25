---
title: "The Coordinate System Problem in Persistent Structural Memory for Neural Architectures"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22858"
published: "2026-03-25"
fetched: "2026-03-26T07:17:34.118050"
---

Computer Science > Machine Learning
[Submitted on 24 Mar 2026]
Title:The Coordinate System Problem in Persistent Structural Memory for Neural Architectures
View PDF HTML (experimental)Abstract:We introduce the Dual-View Pheromone Pathway Network (DPPN), an architecture that routes sparse attention through a persistent pheromone field over latent slot transitions, and use it to discover two independent requirements for persistent structural memory in neural networks. Through five progressively refined experiments using up to 10 seeds per condition across 5 model variants and 4 transfer targets, we identify a core principle: persistent memory requires a stable coordinate system, and any coordinate system learned jointly with the model is inherently unstable. We characterize three obstacles -- pheromone saturation, surface-structure entanglement, and coordinate incompatibility -- and show that neither contrastive updates, multi-source distillation, Hungarian alignment, nor semantic decomposition resolves the instability when embeddings are learned from scratch. Fixed random Fourier features provide extrinsic coordinates that are stable, structure-blind, and informative, but coordinate stability alone is insufficient: routing-bias pheromone does not transfer (10 seeds, p>0.05). DPPN outperforms transformer and random sparse baselines for within-task learning (AULC 0.700 vs 0.680 vs 0.670). Replacing routing bias with learning-rate modulation eliminates negative transfer: warm pheromone as a learning-rate prior achieves +0.003 on same-family tasks (17 seeds, p<0.05) while never reducing performance. A structure completion function over extrinsic coordinates produces +0.006 same-family bonus beyond regularization, showing the catch-22 between stability and informativeness is partially permeable to learned functions. The contribution is two independent requirements for persistent structural memory: (a) coordinate stability and (b) graceful transfer mechanism.
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
