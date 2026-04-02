---
title: "Predicting Wave Reflection and Transmission in Heterogeneous Media via Fourier Operator-Based Transformer Modeling"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00132"
published: "2026-04-02"
fetched: "2026-04-03T07:17:27.374505"
---

Computer Science > Machine Learning
[Submitted on 31 Mar 2026]
Title:Predicting Wave Reflection and Transmission in Heterogeneous Media via Fourier Operator-Based Transformer Modeling
View PDF HTML (experimental)Abstract:We develop a machine learning (ML) surrogate model to approximate solutions to Maxwell's equations in one dimension, focusing on scenarios involving a material interface that reflects and transmits electro-magnetic waves. Derived from high-fidelity Finite Volume (FV) simulations, our training data includes variations of the initial conditions, as well as variations in one material's speed of light, allowing for the model to learn a range of wave-material interaction behaviors. The ML model autoregressively learns both the physical and frequency embeddings in a vision transformer-based framework. By incorporating Fourier transforms in the latent space, the wave number spectra of the solutions aligns closely with the simulation data. Prediction errors exhibit an approximately linear growth over time with a sharp increase at the material interface. Test results show that the ML solution has adequate relative errors below $10\%$ in over $75$ time step rollouts, despite the presence of the discontinuity and unknown material properties.
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
