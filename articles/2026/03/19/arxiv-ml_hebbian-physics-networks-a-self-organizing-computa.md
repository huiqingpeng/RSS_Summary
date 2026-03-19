---
title: "Hebbian Physics Networks: A Self-Organizing Computational Architecture Based on Local Physical Laws"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2507.00641"
published: "2026-03-19"
fetched: "2026-03-19T14:16:01.947576"
---

Nonlinear Sciences > Adaptation and Self-Organizing Systems
[Submitted on 1 Jul 2025 (v1), last revised 18 Mar 2026 (this version, v3)]
Title:Hebbian Physics Networks: A Self-Organizing Computational Architecture Based on Local Physical Laws
View PDFAbstract:Physical transport processes organize through local interactions that redistribute imbalance while preserving conservation. Classical solvers enforce this organization by applying fixed discrete operators on rigid grids. We introduce the Hebbian Physics Network (HPN), a computational framework that replaces this rigid scaffolding with a plastic transport geometry. An HPN is a coupled dynamical system of physical states on nodes and constitutive weights on edges in a graph. Residuals--local violations of continuity, momentum balance, or energy conservation--act as thermodynamic forces that drive the joint evolution of both the state and the operator (i.e. the adaptive weights). The weights adapt through a three-factor Hebbian rule, which we prove constitutes a strictly local gradient descent on the residual energy. This mechanism ensures thermodynamic stability: near equilibrium, the learned operator naturally converges to a symmetric, positive-definite form, rigorously reproducing Onsagerś reciprocal relations without explicit enforcement. Far from equilibrium, the system undergoes a self-organizing search for a transport topology that restores global coercivity. Unlike optimization-based approaches that impose physics through global loss functions, HPNs embed conservation intrinsically: transport is restored locally by the evolving operator itself, without a global Poisson solve or backpropagated objective. We demonstrate the framework on scalar diffusion and incompressible lid-driven cavity flow, showing that physically consistent transport geometries and flow structures emerge from random initial conditions solely through residual-driven local adaptation. HPNs thus reframe computation not as the solution of a fixed equation, but as a thermodynamic relaxation process where the constitutive geometry and physical state co-evolve.
Submission history
From: Gunjan Auti [view email][v1] Tue, 1 Jul 2025 10:34:14 UTC (5,381 KB)
[v2] Tue, 9 Dec 2025 06:46:05 UTC (1,954 KB)
[v3] Wed, 18 Mar 2026 08:55:11 UTC (1,962 KB)
Current browse context:
nlin.AO
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
