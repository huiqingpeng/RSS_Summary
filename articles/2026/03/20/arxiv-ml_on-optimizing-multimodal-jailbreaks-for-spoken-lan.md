---
title: "On Optimizing Multimodal Jailbreaks for Spoken Language Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19127"
published: "2026-03-20"
fetched: "2026-03-20T12:18:42.208554"
---

Computer Science > Machine Learning
[Submitted on 19 Mar 2026]
Title:On Optimizing Multimodal Jailbreaks for Spoken Language Models
View PDF HTML (experimental)Abstract:As Spoken Language Models (SLMs) integrate speech and text modalities, they inherit the safety vulnerabilities of their LLM backbone and an expanded attack surface. SLMs have been previously shown to be susceptible to jailbreaking, where adversarial prompts induce harmful responses. Yet existing attacks largely remain unimodal, optimizing either text or audio in isolation. We explore gradient-based multimodal jailbreaks by introducing JAMA (Joint Audio-text Multimodal Attack), a joint multimodal optimization framework combining Greedy Coordinate Gradient (GCG) for text and Projected Gradient Descent (PGD) for audio, to simultaneously perturb both modalities. Evaluations across four state-of-the-art SLMs and four audio types demonstrate that JAMA surpasses unimodal jailbreak rate by 1.5x to 10x. We analyze the operational dynamics of this joint attack and show that a sequential approximation method makes it 4x to 6x faster. Our findings suggest that unimodal safety is insufficient for robust SLMs. The code and data are available at this https URL
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
