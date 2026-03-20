---
title: "WarPGNN: A Parametric Thermal Warpage Analysis Framework with Physics-aware Graph Neural Network"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.18581"
published: "2026-03-20"
fetched: "2026-03-20T12:04:16.604169"
---

Computer Science > Hardware Architecture
[Submitted on 19 Mar 2026]
Title:WarPGNN: A Parametric Thermal Warpage Analysis Framework with Physics-aware Graph Neural Network
View PDF HTML (experimental)Abstract:With the advent of system-in-package (SiP) chiplet-based design and heterogeneous 2.5D/3D integration, thermal-induced warpage has become a critical reliability concern. While conventional numerical approaches can deliver highly accurate results, they often incur prohib- itively high computational costs, limiting their scalability for complex chiplet-package systems. In this paper, we present WarPGNN, an ef- ficient and accurate parametric thermal warpage analysis framework powered by Graph Neural Networks (GNNs). By operating directly on graphs constructed from the floorplans, WarPGNN enables fast warpage-aware floorplan exploration and exhibits strong transfer- ability across diverse package configurations. Our method first en- codes multi-die floorplans into reduced Transitive Closure Graphs (rTCGs), then a Graph Convolution Network (GCN)-based encoder extracts hierarchical structural features, followed by a U-Net inspired decoder that reconstructs warpage maps from graph feature embed- dings. Furthermore, to address the long-tailed pattern of warpage data distribution, we developed a physics-informed loss and revised a message-passing encoder based on Graph Isomorphic Network (GIN) that further enhance learning performance for extreme cases and expressiveness of graph embeddings. Numerical results show that WarPGNN achieves more than 205.91x speedup compared with the 2-D efficient FEM-based method and over 119766.64x acceleration with 3-D FEM method COMSOL, respectively, while maintaining comparable accuracy at only 1.26% full-scale normalized RMSE and 2.21% warpage value error. Compared with recent DeepONet-based model, our method achieved comparable prediction accuracy and in- ference speedup with 3.4x lower training time. In addition, WarPGNN demonstrates remarkable transferability on unseen datasets with up to 3.69% normalized RMSE and similar runtime.
Current browse context:
cs.AR
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
