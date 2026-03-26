---
title: "An Invariant Compiler for Neural ODEs in AI-Accelerated Scientific Simulation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23861"
published: "2026-03-26"
fetched: "2026-03-27T07:17:57.663269"
---

Computer Science > Machine Learning
[Submitted on 25 Mar 2026]
Title:An Invariant Compiler for Neural ODEs in AI-Accelerated Scientific Simulation
View PDF HTML (experimental)Abstract:Neural ODEs are increasingly used as continuous-time models for scientific and sensor data, but unconstrained neural ODEs can drift and violate domain invariants (e.g., conservation laws), yielding physically implausible solutions. In turn, this can compound error in long-horizon prediction and surrogate simulation. Existing solutions typically aim to enforce invariance by soft penalties or other forms of regularization, which can reduce overall error but do not guarantee that trajectories will not leave the constraint manifold. We introduce the invariant compiler, a framework that enforces invariants by construction: it treats invariants as first-class types and uses an LLM-driven compilation workflow to translate a generic neural ODE specification into a structure-preserving architecture whose trajectories remain on the admissible manifold in continuous time (and up to numerical integration error in practice). This compiler view cleanly separates what must be preserved (scientific structure) from what is learned from data (dynamics within that structure). It provides a systematic design pattern for invariant-respecting neural surrogates across scientific domains.
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
