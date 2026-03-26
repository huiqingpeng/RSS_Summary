---
title: "StateLinFormer: Stateful Training Enhancing Long-term Memory in Navigation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23571"
published: "2026-03-26"
fetched: "2026-03-27T07:14:51.705990"
---

Computer Science > Machine Learning
[Submitted on 24 Mar 2026]
Title:StateLinFormer: Stateful Training Enhancing Long-term Memory in Navigation
View PDF HTML (experimental)Abstract:Effective navigation intelligence relies on long-term memory to support both immediate generalization and sustained adaptation. However, existing approaches face a dilemma: modular systems rely on explicit mapping but lack flexibility, while Transformer-based end-to-end models are constrained by fixed context windows, limiting persistent memory across extended interactions. We introduce StateLinFormer, a linear-attention navigation model trained with a stateful memory mechanism that preserves recurrent memory states across consecutive training segments instead of reinitializing them at each batch boundary. This training paradigm effectively approximates learning on infinitely long sequences, enabling the model to achieve long-horizon memory retention. Experiments across both MAZE and ProcTHOR environments demonstrate that StateLinFormer significantly outperforms its stateless linear-attention counterpart and standard Transformer baselines with fixed context windows. Notably, as interaction length increases, persistent stateful training substantially improves context-dependent adaptation, suggesting an enhancement in the model's In-Context Learning (ICL) capabilities for navigation tasks.
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
