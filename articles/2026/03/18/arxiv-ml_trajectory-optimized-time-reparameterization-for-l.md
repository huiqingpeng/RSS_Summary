---
title: "Trajectory-Optimized Time Reparameterization for Learning-Compatible Reduced-Order Modeling of Stiff Dynamical Systems"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16583"
published: "2026-03-18"
fetched: "2026-03-18T15:45:34.887869"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:Trajectory-Optimized Time Reparameterization for Learning-Compatible Reduced-Order Modeling of Stiff Dynamical Systems
View PDF HTML (experimental)Abstract:Stiff dynamical systems present a challenge for machine-learning reduced-order models (ML-ROMs), as explicit time integration becomes unstable in stiff regimes while implicit integration within learning loops is computationally expensive and often degrades training efficiency. Time reparameterization (TR) offers an alternative by transforming the independent variable so that rapid physical-time transients are spread over a stretched-time coordinate, enabling stable explicit integration on uniformly sampled grids. Although several TR strategies have been proposed, their effect on learnability in ML-ROMs remains incompletely understood. This work investigates time reparameterization as a stiffness-mitigation mechanism for neural ODE reduced-order modeling and introduces a trajectory-optimized TR (TOTR) formulation. The proposed approach casts time reparameterization as an optimization problem in arc-length coordinates, in which a traversal-speed profile is selected to penalize acceleration in stretched time. By targeting the smoothness of the training dynamics, this formulation produces reparameterized trajectories that are better conditioned and easier to learn than existing TR methods. TOTR is evaluated on three stiff problems: a parameterized stiff linear system, the van der Pol oscillator, and the HIRES chemical kinetics model. Across all cases, the proposed approach yields smoother reparameterizations and improved physical-time predictions under identical training regimens than other TR approaches. Quantitative results demonstrate loss reductions of one to two orders of magnitude compared to benchmark algorithms. These results highlight that effective stiffness mitigation in ML-ROMs depends critically on the regularity and learnability of the time map itself, and that optimization-based TR provides a robust framework for explicit reduced-order modeling of multiscale dynamical systems.
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
