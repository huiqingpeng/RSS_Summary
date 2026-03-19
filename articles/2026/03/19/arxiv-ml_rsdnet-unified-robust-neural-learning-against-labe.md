---
title: "rSDNet: Unified Robust Neural Learning against Label Noise and Adversarial Attacks"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17628"
published: "2026-03-19"
fetched: "2026-03-19T13:14:02.762313"
---

Statistics > Machine Learning
[Submitted on 18 Mar 2026]
Title:rSDNet: Unified Robust Neural Learning against Label Noise and Adversarial Attacks
View PDF HTML (experimental)Abstract:Neural networks are central to modern artificial intelligence, yet their training remains highly sensitive to data contamination. Standard neural classifiers are trained by minimizing the categorical cross-entropy loss, corresponding to maximum likelihood estimation under a multinomial model. While statistically efficient under ideal conditions, this approach is highly vulnerable to contaminated observations including label noises corrupting supervision in the output space, and adversarial perturbations inducing worst-case deviations in the input space. In this paper, we propose a unified and statistically grounded framework for robust neural classification that addresses both forms of contamination within a single learning objective. We formulate neural network training as a minimum-divergence estimation problem and introduce rSDNet, a robust learning algorithm based on the general class of $S$-divergences. The resulting training objective inherits robustness properties from classical statistical estimation, automatically down-weighting aberrant observations through model probabilities. We establish essential population-level properties of rSDNet, including Fisher consistency, classification calibration implying Bayes optimality, and robustness guarantees under uniform label noise and infinitesimal feature contamination. Experiments on three benchmark image classification datasets show that rSDNet improves robustness to label corruption and adversarial attacks while maintaining competitive accuracy on clean data, Our results highlight minimum-divergence learning as a principled and effective framework for robust neural classification under heterogeneous data contamination.
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
