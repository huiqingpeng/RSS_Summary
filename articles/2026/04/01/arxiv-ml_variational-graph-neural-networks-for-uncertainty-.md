---
title: "Variational Graph Neural Networks for Uncertainty Quantification in Inverse Problems"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.29515"
published: "2026-04-01"
fetched: "2026-04-02T07:18:51.852086"
---

Computer Science > Machine Learning
[Submitted on 31 Mar 2026]
Title:Variational Graph Neural Networks for Uncertainty Quantification in Inverse Problems
View PDF HTML (experimental)Abstract:The increasingly wide use of deep machine learning techniques in computational mechanics has significantly accelerated simulations of problems that were considered unapproachable just a few years ago. However, in critical applications such as Digital Twins for engineering or medicine, fast responses are not enough; reliable results must also be provided. In certain cases, traditional deterministic methods may not be optimal as they do not provide a measure of confidence in their predictions or results, especially in inverse problems where the solution may not be unique or the initial data may not be entirely reliable due to the presence of noise, for instance. Classic deep neural networks also lack a clear measure to quantify the uncertainty of their predictions. In this work, we present a variational graph neural network (VGNN) architecture that integrates variational layers into its architecture to model the probability distribution of weights. Unlike computationally expensive full Bayesian networks, our approach strategically introduces variational layers exclusively in the decoder, allowing us to estimate cognitive uncertainty and statistical uncertainty at a relatively lower cost.
In this work, we validate the proposed methodology in two cases of solid mechanics: the identification of the value of the elastic modulus with nonlinear distribution in a 2D elastic problem and the location and quantification of the loads applied to a 3D hyperelastic beam, in both cases using only the displacement field of each test as input data. The results show that the model not only recovers the physical parameters with high precision, but also provides confidence intervals consistent with the physics of the problem, as well as being able to locate the position of the applied load and estimate its value, giving a confidence interval for that experiment.
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
