---
title: "RHYME-XT: A Neural Operator for Spatiotemporal Control Systems"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17867"
published: "2026-03-19"
fetched: "2026-03-19T12:17:31.798787"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:RHYME-XT: A Neural Operator for Spatiotemporal Control Systems
View PDF HTML (experimental)Abstract:We propose RHYME-XT, an operator-learning framework for surrogate modeling of spatiotemporal control systems governed by input-affine nonlinear partial integro-differential equations (PIDEs) with localized rhythmic behavior. RHYME-XT uses a Galerkin projection to approximate the infinite-dimensional PIDE on a learned finite-dimensional subspace with spatial basis functions parameterized by a neural network. This yields a projected system of ODEs driven by projected inputs. Instead of integrating this non-autonomous system, we directly learn its flow map using an architecture for learning flow functions, avoiding costly computations while obtaining a continuous-time and discretization-invariant representation. Experiments on a neural field PIDE show that RHYME-XT outperforms a state-of-the-art neural operator and is able to transfer knowledge effectively across models trained on different datasets, through a fine-tuning process.
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
