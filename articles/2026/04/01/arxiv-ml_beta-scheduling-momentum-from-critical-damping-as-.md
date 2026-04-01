---
title: "Beta-Scheduling: Momentum from Critical Damping as a Diagnostic and Correction Tool for Neural Network Training"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.28921"
published: "2026-04-01"
fetched: "2026-04-02T07:13:11.970399"
---

Computer Science > Machine Learning
[Submitted on 30 Mar 2026]
Title:Beta-Scheduling: Momentum from Critical Damping as a Diagnostic and Correction Tool for Neural Network Training
View PDF HTML (experimental)Abstract:Standard neural network training uses constant momentum (typically 0.9), a convention dating to 1964 with limited theoretical justification for its
optimality. We derive a time-varying momentum schedule from the critically damped harmonic oscillator: mu(t) = 1 - 2*sqrt(alpha(t)), where alpha(t) is
the current learning rate. This beta-schedule requires zero free parameters beyond the existing learning rate schedule. On ResNet-18/CIFAR-10,
beta-scheduling delivers 1.9x faster convergence to 90% accuracy compared to constant momentum. More importantly, the per-layer gradient attribution
under this schedule produces a cross-optimizer invariant diagnostic: the same three problem layers are identified regardless of whether the model was
trained with SGD or Adam (100% overlap). Surgical correction of only these layers fixes 62 misclassifications while retraining only 18% of parameters.
A hybrid schedule -- physics momentum for fast early convergence, then constant momentum for the final refinement -- reaches 95% accuracy fastest
among five methods tested. The main contribution is not an accuracy improvement but a principled, parameter-free tool for localizing and correcting
specific failure modes in trained networks.
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
