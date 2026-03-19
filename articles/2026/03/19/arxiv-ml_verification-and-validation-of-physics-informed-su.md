---
title: "Verification and Validation of Physics-Informed Surrogate Component Models for Dynamic Power-System Simulation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17836"
published: "2026-03-19"
fetched: "2026-03-19T13:16:04.255975"
---

Electrical Engineering and Systems Science > Systems and Control
[Submitted on 18 Mar 2026]
Title:Verification and Validation of Physics-Informed Surrogate Component Models for Dynamic Power-System Simulation
View PDF HTML (experimental)Abstract:Physics-informed machine learning surrogates are increasingly explored to accelerate dynamic simulation of generators, converters, and other power grid components. The key question, however, is not only whether a surrogate matches a stand-alone component model on average, but whether it remains accurate after insertion into a differential-algebraic simulator, where the surrogate outputs enter the algebraic equations coupling the component to the rest of the system. This paper formulates that in-simulator use as a verification and validation (V\&V) problem. A finite-horizon bound is derived that links allowable component-output error to algebraic-coupling sensitivity, dynamic error amplification, and the simulation horizon. Two complementary settings are then studied: model-based verification against a reference component solver, and data-based validation through conformal calibration of the component-output variables exchanged with the simulator. The framework is general, but the case study focuses on physics-informed neural-network surrogates of second-, fourth-, and sixth-order synchronous-machine models. Results show that good stand-alone surrogate accuracy does not by itself guarantee accurate in-simulator behavior, that the largest discrepancies concentrate in stressed operating regions, and that small equation residuals do not necessarily imply small state-trajectory errors.
Current browse context:
eess.SY
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
