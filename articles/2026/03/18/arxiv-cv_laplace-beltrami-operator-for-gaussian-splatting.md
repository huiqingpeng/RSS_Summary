---
title: "Laplace-Beltrami Operator for Gaussian Splatting"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2502.17531"
published: "2026-03-18"
fetched: "2026-03-18T19:05:42.266694"
---

Computer Science > Graphics
[Submitted on 24 Feb 2025 (v1), last revised 16 Mar 2026 (this version, v2)]
Title:Laplace-Beltrami Operator for Gaussian Splatting
View PDF HTML (experimental)Abstract:With the rising popularity of 3D Gaussian splatting and the expanse of applications from rendering to 3D reconstruction, there comes also a need for geometry processing applications directly on this new representation. While considering the centers of Gaussians as a point cloud or meshing them is an option that allows to apply existing algorithms, this might ignore information present in the data or be unnecessarily expensive. Additionally, Gaussian splatting tends to contain a large number of outliers which do not affect the rendering quality but need to be handled correctly in order not to produce noisy results in geometry processing applications. In this work, we propose a formulation to compute the Laplace-Beltrami operator, a widely used tool in geometry processing, directly on Gaussian splatting using the Mahalanobis distance. While conceptually similar to a point cloud Laplacian, our experiments show superior accuracy on the point clouds encoded in the Gaussian splatting centers and, additionally, the operator can be used to evaluate the quality of the output during optimization.
Submission history
From: Hongyu Zhou [view email][v1] Mon, 24 Feb 2025 14:29:33 UTC (8,043 KB)
[v2] Mon, 16 Mar 2026 18:02:34 UTC (16,650 KB)
Current browse context:
cs.GR
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
