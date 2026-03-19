---
title: "Symmetry-Reduced Physics-Informed Learning of Tensegrity Dynamics"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17824"
published: "2026-03-19"
fetched: "2026-03-19T12:17:06.927829"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:Symmetry-Reduced Physics-Informed Learning of Tensegrity Dynamics
View PDF HTML (experimental)Abstract:Tensegrity structures possess intrinsic geometric symmetries that govern their dynamic behavior. However, most existing physics-informed neural network (PINN) approaches for tensegrity dynamics do not explicitly exploit these symmetries, leading to high computational complexity and unstable optimization. In this work, we propose a symmetry-reduced physics-informed neural network (SymPINN) framework that embeds group-theory-based symmetry directly into both the solution expression and the neural network architecture to predict tensegrity dynamics. By decomposing nodes into symmetry orbits and representing free nodal coordinates using a symmetry basis, the proposed method constructs a reduced coordinate representation that preserves geometric symmetry of the structure. The full coordinates are then recovered via symmetry transformations of the reduced solution learned by the network, ensuring that the predicted configurations automatically satisfy the symmetry constraints. In this framework, equivariance is enforced through orbit-based coordinate generation, symmetry-consistent message passing, and physics residual constraints. In addition, SymPINN improves training effectiveness by encoding initial conditions as hard constraints, incorporating Fourier feature encoding to enhance the representation of dynamic motions, and employing a two-stage optimization strategy. Extensive numerical experiments on symmetric T-bars and lander structures demonstrate significantly improved prediction accuracy and computational efficiency compared to standard physics-informed models, indicating the great potential of symmetry-aware learning for structure-preserving modeling of tensegrity dynamics.
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
