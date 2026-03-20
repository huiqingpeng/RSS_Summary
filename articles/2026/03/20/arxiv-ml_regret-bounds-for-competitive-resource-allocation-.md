---
title: "Regret Bounds for Competitive Resource Allocation with Endogenous Costs"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18999"
published: "2026-03-20"
fetched: "2026-03-20T13:18:46.570643"
---

Computer Science > Artificial Intelligence
[Submitted on 19 Mar 2026]
Title:Regret Bounds for Competitive Resource Allocation with Endogenous Costs
View PDFAbstract:We study online resource allocation among N interacting modules over T rounds. Unlike standard online optimization, costs are endogenous: they depend on the full allocation vector through an interaction matrix W encoding pairwise cooperation and competition.
We analyze three paradigms: (I) uniform allocation (cost-ignorant), (II) gated allocation (cost-estimating), and (III) competitive allocation via multiplicative weights update with interaction feedback (cost-revealing). Our main results establish a strict separation under adversarial sequences with bounded variation: uniform incurs Omega(T) regret, gated achieves O(T^{2/3}), and competitive achieves O(sqrt(T log N)). The performance gap stems from competitive allocation's ability to exploit endogenous cost information revealed through interactions.
We further show that W's topology governs a computation-regret tradeoff. Full interaction (|E|=O(N^2)) yields the tightest bound but highest per-step cost, while sparse topologies (|E|=O(N)) increase regret by at most O(sqrt(log N)) while reducing per-step cost from O(N^2) to O(N). Ring-structured topologies with both cooperative and competitive links - of which the five-element Wuxing topology is canonical - minimize the computation x regret product.
These results provide the first formal regret-theoretic justification for decentralized competitive allocation in modular architectures and establish cost endogeneity as a fundamental challenge distinct from partial observability.
Keywords: online learning, regret bounds, resource allocation, endogenous costs, interaction topology, multiplicative weights, modular systems, Wuxing topology
Current browse context:
cs.AI
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
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
