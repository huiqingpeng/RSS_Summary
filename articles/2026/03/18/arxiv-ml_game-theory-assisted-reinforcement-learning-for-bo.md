---
title: "Game-Theory-Assisted Reinforcement Learning for Border Defense: Early Termination based on Analytical Solutions"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15907"
published: "2026-03-18"
fetched: "2026-03-18T15:37:00.439539"
---

Computer Science > Machine Learning
[Submitted on 16 Mar 2026]
Title:Game-Theory-Assisted Reinforcement Learning for Border Defense: Early Termination based on Analytical Solutions
View PDF HTML (experimental)Abstract:Game theory provides the gold standard for analyzing adversarial engagements, offering strong optimality guarantees. However, these guarantees often become brittle when assumptions such as perfect information are violated. Reinforcement learning (RL), by contrast, is adaptive but can be sample-inefficient in large, complex domains. This paper introduces a hybrid approach that leverages game-theoretic insights to improve RL training efficiency. We study a border defense game with limited perceptual range, where defender performance depends on both search and pursuit strategies, making classical differential game solutions inapplicable. Our method employs the Apollonius Circle (AC) to compute equilibrium in the post-detection phase, enabling early termination of RL episodes without learning pursuit dynamics. This allows RL to concentrate on learning search strategies while guaranteeing optimal continuation after detection. Across single- and multi-defender settings, this early termination method yields 10-20% higher rewards, faster convergence, and more efficient search trajectories. Extensive experiments validate these findings and demonstrate the overall effectiveness of our approach.
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
