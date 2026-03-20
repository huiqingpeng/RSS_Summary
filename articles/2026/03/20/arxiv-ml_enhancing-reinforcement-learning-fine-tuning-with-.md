---
title: "Enhancing Reinforcement Learning Fine-Tuning with an Online Refiner"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18088"
published: "2026-03-20"
fetched: "2026-03-20T12:07:27.522994"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:Enhancing Reinforcement Learning Fine-Tuning with an Online Refiner
View PDF HTML (experimental)Abstract:Constraints are essential for stabilizing reinforcement learning fine-tuning (RFT) and preventing degenerate outputs, yet they inherently conflict with the optimization objective because stronger constraints limit the ability of a fine-tuned model to discover better solutions. We propose \textit{dynamic constraints} that resolve this tension by adapting to the evolving capabilities of the fine-tuned model based on the insight that constraints should only intervene when degenerate outputs occur. We implement this by using a reference model as an \textit{online refiner} that takes the response from the fine-tuned model and generates a minimally corrected version which preserves correct content verbatim while fixing errors. A supervised fine-tuning loss then trains the fine-tuned model to produce the refined output. This mechanism yields a constraint that automatically strengthens or relaxes based on output quality. Experiments on dialogue and code generation show that dynamic constraints outperform both KL regularization and unconstrained baselines, achieving substantially higher task rewards while maintaining training stability.
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
