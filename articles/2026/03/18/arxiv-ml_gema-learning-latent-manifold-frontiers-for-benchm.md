---
title: "GeMA: Learning Latent Manifold Frontiers for Benchmarking Complex Systems"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16729"
published: "2026-03-18"
fetched: "2026-03-18T15:46:51.212115"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:GeMA: Learning Latent Manifold Frontiers for Benchmarking Complex Systems
View PDF HTML (experimental)Abstract:Benchmarking the performance of complex systems such as rail networks, renewable generation assets and national economies is central to transport planning, regulation and macroeconomic analysis. Classical frontier methods, notably Data Envelopment Analysis (DEA) and Stochastic Frontier Analysis (SFA), estimate an efficient frontier in the observed input-output space and define efficiency as distance to this frontier, but rely on restrictive assumptions on the production set and only indirectly address heterogeneity and scale effects.
We propose Geometric Manifold Analysis (GeMA), a latent manifold frontier framework implemented via a productivity-manifold variational autoencoder (ProMan-VAE). Instead of specifying a frontier function in the observed space, GeMA represents the production set as the boundary of a low-dimensional manifold embedded in the joint input-output space. A split-head encoder learns latent variables that capture technological structure and operational inefficiency. Efficiency is evaluated with respect to the learned manifold, endogenous peer groups arise as clusters in latent technology space, a quotient construction supports scale-invariant benchmarking, and a local certification radius, derived from the decoder Jacobian and a Lipschitz bound, quantifies the geometric robustness of efficiency scores.
We validate GeMA on synthetic data with non-convex frontiers, heterogeneous technologies and scale bias, and on four real-world case studies: global urban rail systems (COMET), British rail operators (ORR), national economies (Penn World Table) and a high-frequency wind-farm dataset. Across these domains GeMA behaves comparably to established methods when classical assumptions hold, and provides additional insight in settings with pronounced heterogeneity, non-convexity or size-related bias.
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
