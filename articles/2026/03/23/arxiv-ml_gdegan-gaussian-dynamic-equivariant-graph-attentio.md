---
title: "GDEGAN: Gaussian Dynamic Equivariant Graph Attention Network for Ligand Binding Site Prediction"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19817"
published: "2026-03-23"
fetched: "2026-03-24T07:22:34.191040"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:GDEGAN: Gaussian Dynamic Equivariant Graph Attention Network for Ligand Binding Site Prediction
View PDF HTML (experimental)Abstract:Accurate prediction of binding sites of a given protein, to which ligands can bind, is a critical step in structure-based computational drug discovery. Recently, Equivariant Graph Neural Networks (GNNs) have emerged as a powerful paradigm for binding site identification methods due to the large-scale availability of 3D structures of proteins via protein databases and AlphaFold predictions. The state-of-the-art equivariant GNN methods implement dot product attention, disregarding the variation in the chemical and geometric properties of the neighboring residues. To capture this variation, we propose GDEGAN (Gaussian Dynamic Equivariant Graph Attention Network), which replaces dot-product attention with adaptive kernels that recognize binding sites. The proposed attention mechanism captures variation in neighboring residues using statistics of their characteristic local feature distributions. Our mechanism dynamically computes neighborhood statistics at each layer, using local variance as an adaptive bandwidth parameter with learnable per-head temperatures, enabling each protein region to determine its own context-specific importance. GDEGAN outperforms existing methods with relative improvements of 37-66% in DCC and 7-19% DCA success rates across COACH420, HOLO4k, and PDBBind2020 datasets. These advances have direct application in accelerating protein-ligand docking by identifying potential binding sites for therapeutic target identification.
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
