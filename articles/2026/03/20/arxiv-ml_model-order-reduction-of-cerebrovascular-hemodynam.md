---
title: "Model Order Reduction of Cerebrovascular Hemodynamics Using POD_Galerkin and Reservoir Computing_based Approach"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18837"
published: "2026-03-20"
fetched: "2026-03-20T13:16:11.244956"
---

Mathematics > Numerical Analysis
[Submitted on 19 Mar 2026]
Title:Model Order Reduction of Cerebrovascular Hemodynamics Using POD_Galerkin and Reservoir Computing_based Approach
View PDF HTML (experimental)Abstract:We investigate model order reduction (MOR) strategies for simulating unsteady hemodynamics within cerebrovascular systems, contrasting a physics-based intrusive approach with a data-driven non-intrusive framework. High-fidelity 3D Computational Fluid Dynamics (CFD) snapshots of an idealised basilar artery bifurcation are first compressed into a low-dimensional latent space using Proper Orthogonal Decomposition (POD). We evaluate the performance of a POD-Galerkin (POD-G) model, which projects the Navier-Stokes equations onto the reduced basis, against a POD-Reservoir Computing (POD-RC) model that learns the temporal evolution of coefficients through a recurrent architecture. A multi-harmonic and multi-amplitude training signal is introduced to improve training efficiency. Both methodologies achieve computational speed-ups on the order of 10^2 to 10^3 compared to full-order simulations, demonstrating their potential as efficient and accurate surrogates for predicting flow quantities such as wall shear stress.
Submission history
From: Kabir Bakhshaei [view email][v1] Thu, 19 Mar 2026 12:38:34 UTC (16,274 KB)
Current browse context:
math.NA
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
