---
title: "The Cost of Reasoning: Chain-of-Thought Induces Overconfidence in Vision-Language Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16728"
published: "2026-03-18"
fetched: "2026-03-18T15:46:42.563209"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:The Cost of Reasoning: Chain-of-Thought Induces Overconfidence in Vision-Language Models
View PDF HTML (experimental)Abstract:Vision-language models (VLMs) are increasingly deployed in high-stakes settings where reliable uncertainty quantification (UQ) is as important as predictive accuracy. Extended reasoning via chain-of-thought (CoT) prompting or reasoning-trained models has become ubiquitous in modern VLM pipelines, yet its effect on UQ reliability remains poorly understood. We show that reasoning consistently degrades the quality of most uncertainty estimates, even when it improves task accuracy. We identify implicit answer conditioning as the primary mechanism: as reasoning traces converge on a conclusion before the final answer is generated, token probabilities increasingly reflect consistency with the model's own reasoning trace rather than uncertainty about correctness. In effect, the model becomes overconfident in its answer. In contrast, agreement-based consistency remains robust and often improves under reasoning, making it a practical choice for uncertainty estimation in reasoning-enabled VLMs.
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
