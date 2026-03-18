---
title: "Self-Aware Markov Models for Discrete Reasoning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16661"
published: "2026-03-18"
fetched: "2026-03-18T15:45:50.244755"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:Self-Aware Markov Models for Discrete Reasoning
View PDF HTML (experimental)Abstract:Standard masked discrete diffusion models face limitations in reasoning tasks due to their inability to correct their own mistakes on the masking path. Since they rely on a fixed number of denoising steps, they are unable to adjust their computation to the complexity of a given problem. To address these limitations, we introduce a method based on learning a Markov transition kernel that is trained on its own outputs. This design enables tokens to be remasked, allowing the model to correct its previous mistakes. Furthermore, we do not need a fixed time schedule but use a trained stopping criterion. This allows for adaptation of the number of function evaluations to the difficulty of the reasoning problem. Our adaptation adds two lightweight prediction heads, enabling reuse and fine-tuning of existing pretrained models. On the Sudoku-Extreme dataset we clearly outperform other flow based methods with a validity of 95%. For the Countdown-4 we only need in average of 10 steps to solve almost 96% of them correctly, while many problems can be solved already in 2 steps.
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
