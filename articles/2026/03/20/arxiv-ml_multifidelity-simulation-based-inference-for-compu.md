---
title: "Multifidelity Simulation-based Inference for Computationally Expensive Simulators"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2502.08416"
published: "2026-03-20"
fetched: "2026-03-20T14:14:46.168448"
---

Statistics > Machine Learning
[Submitted on 12 Feb 2025 (v1), last revised 19 Mar 2026 (this version, v4)]
Title:Multifidelity Simulation-based Inference for Computationally Expensive Simulators
View PDF HTML (experimental)Abstract:Across many domains of science, stochastic models are an essential tool to understand the mechanisms underlying empirically observed data. Models can be of different levels of detail and accuracy, with models of high-fidelity (i.e., high accuracy) to the phenomena under study being often preferable. However, inferring parameters of high-fidelity models via simulation-based inference is challenging, especially when the simulator is computationally expensive. We introduce a multifidelity approach to neural posterior estimation that uses transfer learning to leverage inexpensive low-fidelity simulations to efficiently infer parameters of high-fidelity simulators. Our method applies the multifidelity scheme to both amortized and non-amortized neural posterior estimation. We further improve simulation efficiency by introducing a sequential variant that uses an acquisition function targeting the predictive uncertainty of the density estimator to adaptively select high-fidelity parameters. On established benchmark and neuroscience tasks, our approaches require up to two orders of magnitude fewer high-fidelity simulations than current methods, while showing comparable performance. Overall, our approaches open new opportunities to perform efficient Bayesian inference on computationally expensive simulators.
Submission history
From: Anastasia Nastya Krouglova [view email][v1] Wed, 12 Feb 2025 13:59:22 UTC (9,147 KB)
[v2] Fri, 14 Feb 2025 14:55:02 UTC (1,889 KB)
[v3] Wed, 22 Oct 2025 18:47:14 UTC (9,197 KB)
[v4] Thu, 19 Mar 2026 13:55:55 UTC (9,442 KB)
Current browse context:
stat.ML
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
