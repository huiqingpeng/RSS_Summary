---
title: "PEANUT: Perturbations by Eigenvalue Alignment for Attacking GNNs Under Topology-Driven Message Passing"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26136"
published: "2026-03-30"
fetched: "2026-03-31T07:22:04.776487"
---

Computer Science > Machine Learning
[Submitted on 27 Mar 2026]
Title:PEANUT: Perturbations by Eigenvalue Alignment for Attacking GNNs Under Topology-Driven Message Passing
View PDF HTML (experimental)Abstract:Graph Neural Networks (GNNs) have achieved remarkable performance on tasks involving relational data. However, small perturbations to the graph structure can significantly alter GNN outputs, raising concerns about their robustness in real-world deployments. In this work, we explore the core vulnerability of GNNs which explicitly consume graph topology in the form of the adjacency matrix or Laplacian as a means for message passing, and propose PEANUT, a simple, gradient-free, restricted black-box attack that injects virtual nodes to capitalize on this vulnerability. PEANUT is a injection based attack, which is widely considered to be more practical and realistic scenario than graph modification attacks, where the attacker is able to modify the original graph structure directly. Our method works at the inference phase, making it an evasion attack, and is applicable almost immediately, since it does not involve lengthy iterative optimizations or parameter learning, which add computational and time overhead, or training surrogate models, which are susceptible to failure due to differences in model priors and generalization capabilities. PEANUT also does not require any features on the injected node and consequently demonstrates that GNN performance can be significantly deteriorated even with injected nodes with zeros for features, highlighting the significance of effectively designed connectivity in such attacks. Extensive experiments on real-world datasets across three graph tasks demonstrate the effectiveness of our attack despite its simplicity.
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
