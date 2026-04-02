---
title: "Phase space integrity in neural network models of Hamiltonian dynamics: A Lagrangian descriptor approach"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00473"
published: "2026-04-02"
fetched: "2026-04-03T07:21:35.425306"
---

Computer Science > Machine Learning
[Submitted on 1 Apr 2026]
Title:Phase space integrity in neural network models of Hamiltonian dynamics: A Lagrangian descriptor approach
View PDF HTML (experimental)Abstract:We propose Lagrangian Descriptors (LDs) as a diagnostic framework for evaluating neural network models of Hamiltonian systems beyond conventional trajectory-based metrics. Standard error measures quantify short-term predictive accuracy but provide little insight into global geometric structures such as orbits and separatrices. Existing evaluation tools in dissipative systems are inadequate for Hamiltonian dynamics due to fundamental differences in the systems. By constructing probability density functions weighted by LD values, we embed geometric information into a statistical framework suitable for information-theoretic comparison. We benchmark physically constrained architectures (SympNet, HénonNet, Generalized Hamiltonian Neural Networks) against data-driven Reservoir Computing across two canonical systems. For the Duffing oscillator, all models recover the homoclinic orbit geometry with modest data requirements, though their accuracy near critical structures varies. For the three-mode nonlinear Schrödinger equation, however, clear differences emerge: symplectic architectures preserve energy but distort phase-space topology, while Reservoir Computing, despite lacking explicit physical constraints, reproduces the homoclinic structure with high fidelity. These results demonstrate the value of LD-based diagnostics for assessing not only predictive performance but also the global dynamical integrity of learned Hamiltonian models.
Submission history
From: Abrari Noor Hasmi [view email][v1] Wed, 1 Apr 2026 04:34:54 UTC (12,069 KB)
Current browse context:
cs.LG
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
