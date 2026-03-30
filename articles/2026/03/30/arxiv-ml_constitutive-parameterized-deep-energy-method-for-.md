---
title: "Constitutive parameterized deep energy method for solid mechanics problems with random material parameters"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26030"
published: "2026-03-30"
fetched: "2026-03-31T07:20:55.796782"
---

Computer Science > Machine Learning
[Submitted on 27 Mar 2026]
Title:Constitutive parameterized deep energy method for solid mechanics problems with random material parameters
View PDF HTML (experimental)Abstract:In practical structural design and solid mechanics simulations, material properties inherently exhibit random variations within bounded intervals. However, evaluating mechanical responses under continuous material uncertainty remains a persistent challenge. Traditional numerical approaches, such as the Finite Element Method (FEM), incur prohibitive computational costs as they require repeated mesh discretization and equation solving for every parametric realization. Similarly, data-driven surrogate models depend heavily on massive, high-fidelity datasets, while standard physics-informed frameworks (e.g., the Deep Energy Method) strictly demand complete retraining from scratch whenever material parameters change. To bridge this critical gap, we propose the Constitutive Parameterized Deep Energy Method (CPDEM). In this purely physics-driven framework, the strain energy density functional is reformulated by encoding a latent representation of stochastic constitutive parameters. By embedding material parameters directly into the neural network alongside spatial coordinates, CPDEM transforms conventional spatial collocation points into parameter-aware material points. Trained in an unsupervised manner via expected energy minimization over the parameter domain, the pre-trained model continuously learns the solution manifold. Consequently, it enables zero-shot, real-time inference of displacement fields for unknown material parameters without requiring any dataset generation or model retraining. The proposed method is rigorously validated across diverse benchmarks, including linear elasticity, finite-strain hyperelasticity, and complex highly nonlinear contact mechanics. To the best of our knowledge, CPDEM represents the first purely physics-driven deep learning paradigm capable of simultaneously and efficiently handling continuous multi-parameter variations in solid mechanics.
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
