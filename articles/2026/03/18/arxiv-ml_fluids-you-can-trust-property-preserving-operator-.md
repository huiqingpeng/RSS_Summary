---
title: "Fluids You Can Trust: Property-Preserving Operator Learning for Incompressible Flows"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2602.15472"
published: "2026-03-18"
fetched: "2026-03-18T17:14:18.013317"
---

Physics > Fluid Dynamics
[Submitted on 17 Feb 2026 (v1), last revised 17 Mar 2026 (this version, v3)]
Title:Fluids You Can Trust: Property-Preserving Operator Learning for Incompressible Flows
View PDFAbstract:We present a novel property-preserving kernel-based operator learning method for incompressible flows governed by the incompressible Navier--Stokes equations. Traditional numerical solvers incur significant computational costs to respect incompressibility. Operator learning offers efficient surrogate models, but current neural operators fail to exactly enforce physical properties such as incompressibility, periodicity, and turbulence. Our kernel method maps input functions to expansion coefficients of output functions in a property-preserving kernel basis, ensuring that predicted velocity fields $\textit{analytically}$ and $\textit{simultaneously}$ preserve the aforementioned physical properties. Our method leverages efficient numerical linear algebra, simple rootfinding, and streaming to allow for training at-scale on desktop GPUs. We also present universal approximation results and both pessimistic and more realistic $\textit{a priori}$ convergence rates for our framework. We evaluate the method on challenging 2D and 3D, laminar and turbulent, incompressible flow problems. Our method achieves up to six orders of magnitude lower relative $\ell_2$ errors upon generalization and trains up to five orders of magnitude faster compared to neural operators, despite our method being trained on desktop GPUs and neural operators being trained on cutting-edge GPU servers. Moreover, while our method enforces incompressibility analytically, neural operators exhibit very large deviations. Our results show that our method provides an accurate and efficient surrogate for incompressible flows.
Submission history
From: Ramansh Sharma [view email][v1] Tue, 17 Feb 2026 10:20:46 UTC (9,237 KB)
[v2] Fri, 27 Feb 2026 03:00:26 UTC (9,238 KB)
[v3] Tue, 17 Mar 2026 17:44:47 UTC (9,256 KB)
Current browse context:
physics.flu-dyn
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
