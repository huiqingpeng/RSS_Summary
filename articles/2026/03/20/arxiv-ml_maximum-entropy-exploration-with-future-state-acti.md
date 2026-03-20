---
title: "Maximum-Entropy Exploration with Future State-Action Visitation Measures"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18965"
published: "2026-03-20"
fetched: "2026-03-20T12:17:32.224194"
---

Computer Science > Machine Learning
[Submitted on 19 Mar 2026]
Title:Maximum-Entropy Exploration with Future State-Action Visitation Measures
View PDF HTML (experimental)Abstract:Maximum entropy reinforcement learning motivates agents to explore states and actions to maximize the entropy of some distribution, typically by providing additional intrinsic rewards proportional to that entropy function. In this paper, we study intrinsic rewards proportional to the entropy of the discounted distribution of state-action features visited during future time steps. This approach is motivated by two results. First, we show that the expected sum of these intrinsic rewards is a lower bound on the entropy of the discounted distribution of state-action features visited in trajectories starting from the initial states, which we relate to an alternative maximum entropy objective. Second, we show that the distribution used in the intrinsic reward definition is the fixed point of a contraction operator and can therefore be estimated off-policy. Experiments highlight that the new objective leads to improved visitation of features within individual trajectories, in exchange for slightly reduced visitation of features in expectation over different trajectories, as suggested by the lower bound. It also leads to improved convergence speed for learning exploration-only agents. Control performance remains similar across most methods on the considered benchmarks.
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
