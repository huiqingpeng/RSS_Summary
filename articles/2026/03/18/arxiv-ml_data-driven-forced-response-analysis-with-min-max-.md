---
title: "Data-driven forced response analysis with min-max representations of nonlinear restoring forces"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16746"
published: "2026-03-18"
fetched: "2026-03-18T16:14:12.896315"
---

Mathematics > Dynamical Systems
[Submitted on 17 Mar 2026]
Title:Data-driven forced response analysis with min-max representations of nonlinear restoring forces
View PDF HTML (experimental)Abstract:This paper discusses a novel data-driven nonlinearity identification method for mechanical systems with nonlinear restoring forces such as polynomial, piecewise-linear, and general displacement-dependent nonlinearities. The proposed method is built upon the universal approximation theorem that states that a nonlinear function can be approximated by a linear combination of activation functions in artificial neural network framework. The proposed approach utilizes piecewise linear springs with initial gaps to act as the activation functions of the neurons of artificial neural networks. A library of piecewise linear springs with initial gaps are constructed, and the contributions of the springs on the nonlinear restoring force are determined by solving the linear regression problems. The piecewise linear springs are realized by combinations of min and max functions with biases. The proposed method is applied to a Duffing oscillator with cubic stiffness, and a piecewise linear oscillator with a gap and their nonlinearities are successfully determined from their free responses. The obtained models are then used for conducting forced response analysis and the results match well with those of the original system. The method is then applied to experimentally-obtained free response data of a cantilevered plate that is subjected to magnetic restoring force, and successfully finds the piecewise linear representation of the magnetic force. It is also shown that the obtained model is capable of accurately capturing the steady-state response of the system subject to harmonic base excitation.
Current browse context:
math.DS
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
