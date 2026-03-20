---
title: "Discovering What You Can Control: Interventional Boundary Discovery for Reinforcement Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18257"
published: "2026-03-20"
fetched: "2026-03-20T12:09:19.331104"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:Discovering What You Can Control: Interventional Boundary Discovery for Reinforcement Learning
View PDF HTML (experimental)Abstract:Selecting relevant state dimensions in the presence of confounded distractors is a causal identification problem: observational statistics alone cannot reliably distinguish dimensions that correlate with actions from those that actions cause. We formalize this as discovering the agent's Causal Sphere of Influence and propose Interventional Boundary Discovery IBD, which applies Pearl's do-operator to the agent's own actions and uses two-sample testing to produce an interpretable binary mask over observation dimensions. IBD requires no learned models and composes with any downstream RL algorithm as a preprocessing step. Across 12 continuous control settings with up to 100 distractor dimensions, we find that: (1) observational feature selection can actively select confounded distractors while discarding true causal dimensions; (2) full-state RL degrades sharply once distractors outnumber relevant features by roughly 3:1 in our benchmarks; and (3)IBD closely tracks oracle performance across all distractor levels tested, with gains transferring across SAC and TD3.
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
