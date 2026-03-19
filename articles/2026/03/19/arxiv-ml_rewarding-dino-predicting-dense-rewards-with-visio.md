---
title: "Rewarding DINO: Predicting Dense Rewards with Vision Foundation Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16978"
published: "2026-03-19"
fetched: "2026-03-19T13:07:52.599000"
---

Computer Science > Robotics
[Submitted on 17 Mar 2026]
Title:Rewarding DINO: Predicting Dense Rewards with Vision Foundation Models
View PDF HTML (experimental)Abstract:Well-designed dense reward functions in robot manipulation not only indicate whether a task is completed but also encode progress along the way. Generally, designing dense rewards is challenging and usually requires access to privileged state information available only in simulation, not in real-world experiments. This makes reward prediction models that infer task state information from camera images attractive. A common approach is to predict rewards from expert demonstrations based on visual similarity or sequential frame ordering. However, this biases the resulting reward function towards a specific solution and leaves it undefined in states not covered by the demonstrations. In this work, we introduce Rewarding DINO, a method for language-conditioned reward modeling that learns actual reward functions rather than specific trajectories. The model's compact size allows it to serve as a direct replacement for analytical reward functions with comparatively low computational overhead. We train our model on data sampled from 24 Meta-World+ tasks using a rank-based loss and evaluate pairwise accuracy, rank correlation, and calibration. Rewarding DINO achieves competitive performance in tasks from the training set and generalizes to new settings in simulation and the real world, indicating that it learns task semantics. We also test the model with off-the-shelf reinforcement learning algorithms to solve tasks from our Meta-World+ training set.
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
