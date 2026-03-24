---
title: "Simple Projection-Free Algorithm for Contextual Recommendation with Logarithmic Regret and Robustness"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20826"
published: "2026-03-24"
fetched: "2026-03-25T07:14:38.690206"
---

Computer Science > Machine Learning
[Submitted on 21 Mar 2026]
Title:Simple Projection-Free Algorithm for Contextual Recommendation with Logarithmic Regret and Robustness
View PDF HTML (experimental)Abstract:Contextual recommendation is a variant of contextual linear bandits in which the learner observes an (optimal) action rather than a reward scalar. Recently, Sakaue et al. (2025) developed an efficient Online Newton Step (ONS) approach with an $O(d\log T)$ regret bound, where $d$ is the dimension of the action space and $T$ is the time horizon. In this paper, we present a simple algorithm that is more efficient than the ONS-based method while achieving the same regret guarantee. Our core idea is to exploit the improperness inherent in contextual recommendation, leading to an update rule akin to the second-order perceptron from online classification. This removes the Mahalanobis projection step required by ONS, which is often a major computational bottleneck. More importantly, the same algorithm remains robust to possibly suboptimal action feedback, whereas the prior ONS-based method required running multiple ONS learners with different learning rates for this extension. We describe how our method works in general Hilbert spaces (e.g., via kernelization), where eliminating Mahalanobis projections becomes even more beneficial.
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
