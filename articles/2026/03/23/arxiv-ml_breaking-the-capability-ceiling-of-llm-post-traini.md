---
title: "Breaking the Capability Ceiling of LLM Post-Training by Reintroducing Markov States"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19987"
published: "2026-03-23"
fetched: "2026-03-24T07:23:44.540817"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:Breaking the Capability Ceiling of LLM Post-Training by Reintroducing Markov States
View PDF HTML (experimental)Abstract:Reinforcement learning (RL) has become a standard paradigm for post-training and aligning Large Language Models (LLMs), yet recent evidence suggests it faces a persistent "capability ceiling": unlike classical RL systems that discover novel strategies, RL for LLMs often acts as a mere refiner of patterns already latent in pre-trained weights. In this work, we identify a fundamental structural bottleneck: while classical RL relies on compact, informative Markov states, current LLM post-training formulations are tethered to an ever-expanding history of actions.
We revisit a classical principle long central to RL yet absent from LLM post-training: explicit Markov states. Theoretically, we provide rigorous guarantees demonstrating that leveraging estimated Markov states can significantly reduce sample complexity. Empirically, we show that introducing Markov states consistently breaks the performance boundaries of standard RL post-training across a suite of complex logic puzzles. Our findings suggest that moving beyond "history-as-state" modeling in favor of structured Markovian representations is essential for unlocking open-ended discovery and genuinely new reasoning capabilities in Generative AI.
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
