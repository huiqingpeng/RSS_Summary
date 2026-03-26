---
title: "Resolving gradient pathology in physics-informed epidemiological models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23799"
published: "2026-03-26"
fetched: "2026-03-27T07:17:14.429784"
---

Computer Science > Machine Learning
[Submitted on 25 Mar 2026]
Title:Resolving gradient pathology in physics-informed epidemiological models
View PDF HTML (experimental)Abstract:Physics-informed neural networks (PINNs) are increasingly used in mathematical epidemiology to bridge the gap between noisy clinical data and compartmental models, such as the susceptible-exposed-infected-removed (SEIR) model. However, training these hybrid networks is often unstable due to competing optimization objectives. As established in recent literature on ``gradient pathology," the gradient vectors derived from the data loss and the physical residual often point in conflicting directions, leading to slow convergence or optimization deadlock. While existing methods attempt to resolve this by balancing gradient magnitudes or projecting conflicting vectors, we propose a novel method, conflict-gated gradient scaling (CGGS), to address gradient conflicts in physics-informed neural networks for epidemiological modelling, ensuring stable and efficient training and a computationally efficient alternative. This method utilizes the cosine similarity between the data and physics gradients to dynamically modulate the penalty weight. Unlike standard annealing schemes that only normalize scales, CGGS acts as a geometric gate: it suppresses the physical constraint when directional conflict is high, allowing the optimizer to prioritize data fidelity, and restores the constraint when gradients align. We prove that this gating mechanism preserves the standard $O(1/T)$ convergence rate for smooth non-convex objectives, a guarantee that fails under fixed-weight or magnitude-balanced training when gradients conflict. We demonstrate that this mechanism autonomously induces a curriculum learning effect, improving parameter estimation in stiff epidemiological systems compared to magnitude-based baselines. Our empirical results show improved peak recovery and convergence over magnitude-based methods.
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
