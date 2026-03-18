---
title: "Parallelised Differentiable Straightest Geodesics for 3D Meshes"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15780"
published: "2026-03-18"
fetched: "2026-03-18T16:07:43.306106"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 16 Mar 2026]
Title:Parallelised Differentiable Straightest Geodesics for 3D Meshes
View PDFAbstract:Machine learning has been progressively generalised to operate within non-Euclidean domains, but geometrically accurate methods for learning on surfaces are still falling behind. The lack of closed-form Riemannian operators, the non-differentiability of their discrete counterparts, and poor parallelisation capabilities have been the main obstacles to the development of the field on meshes. A principled framework to compute the exponential map on Riemannian surfaces discretised as meshes is straightest geodesics, which also allows to trace geodesics and parallel-transport vectors as a by-product. We provide a parallel GPU implementation and derive two different methods for differentiating through the straightest geodesics, one leveraging an extrinsic proxy function and one based upon a geodesic finite differences scheme. After proving our parallelisation performance and accuracy, we demonstrate how our differentiable exponential map can improve learning and optimisation pipelines on general geometries. In particular, to showcase the versatility of our method, we propose a new geodesic convolutional layer, a new flow matching method for learning on meshes, and a second-order optimiser that we apply to centroidal Voronoi tessellation. Our code, models, and pip-installable library (digeo) are available at: this http URL.
Current browse context:
cs.CV
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
