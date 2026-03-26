---
title: "BXRL: Behavior-Explainable Reinforcement Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23738"
published: "2026-03-26"
fetched: "2026-03-27T07:16:30.320933"
---

Computer Science > Machine Learning
[Submitted on 24 Mar 2026]
Title:BXRL: Behavior-Explainable Reinforcement Learning
View PDF HTML (experimental)Abstract:A major challenge of Reinforcement Learning is that agents often learn undesired behaviors that seem to defy the reward structure they were given. Explainable Reinforcement Learning (XRL) methods can answer queries such as "explain this specific action", "explain this specific trajectory", and "explain the entire policy". However, XRL lacks a formal definition for behavior as a pattern of actions across many episodes. We provide such a definition, and use it to enable a new query: "Explain this behavior".
We present Behavior-Explainable Reinforcement Learning (BXRL), a new problem formulation that treats behaviors as first-class objects. BXRL defines a behavior measure as any function $m : \Pi \to \mathbb{R}$, allowing users to precisely express the pattern of actions that they find interesting and measure how strongly the policy exhibits it. We define contrastive behaviors that reduce the question "why does the agent prefer $a$ to $a'$?" to "why is $m(\pi)$ high?" which can be explored with differentiation. We do not implement an explainability method; we instead analyze three existing methods and propose how they could be adapted to explain behavior. We present a port of the HighwayEnv driving environment to JAX, which provides an interface for defining, measuring, and differentiating behaviors with respect to the model parameters.
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
