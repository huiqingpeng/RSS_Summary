---
title: "Exploring Silent Data Corruption as a Reliability Challenge in LLM Training"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00726"
published: "2026-04-02"
fetched: "2026-04-03T07:23:58.253352"
---

Computer Science > Machine Learning
[Submitted on 1 Apr 2026]
Title:Exploring Silent Data Corruption as a Reliability Challenge in LLM Training
View PDF HTML (experimental)Abstract:As Large Language Models (LLMs) scale in size and complexity, the consequences of failures during training become increasingly severe. A major challenge arises from Silent Data Corruption (SDC): hardware-induced faults that bypass system-level detection mechanisms. SDC may behave like benign numerical noise, but can also cause harmful gradient corruption that leads to loss spikes, divergence, or stalled progress.
This work provides a controlled study of how intermittent SDC affects LLM pretraining. Using targeted fault injection at the level of GPU matrix-multiply instructions, we characterize the sensitivity of different bit positions, kernel functions, and execution stages. Our analysis shows that locally originating faults can produce impactful corruption, including NaN propagation, short-lived spikes in loss, gradient norm, and attention logits, as well as persistent parameter divergence. Building on the observed corruption signatures, we propose a lightweight detection method that identifies potentially harmful parameter updates. Experiments on LLaMA models with 60M, 350M, and 1.3B parameters demonstrate that recomputing the most recent training step upon detection can effectively mitigate the impact of these events.
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
