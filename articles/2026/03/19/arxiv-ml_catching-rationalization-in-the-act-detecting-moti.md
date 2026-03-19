---
title: "Catching rationalization in the act: detecting motivated reasoning before and after CoT via activation probing"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17199"
published: "2026-03-19"
fetched: "2026-03-19T12:08:55.028561"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:Catching rationalization in the act: detecting motivated reasoning before and after CoT via activation probing
View PDF HTML (experimental)Abstract:Large language models (LLMs) can produce chains of thought (CoT) that do not accurately reflect the actual factors driving their answers. In multiple-choice settings with an injected hint favoring a particular option, models may shift their final answer toward the hinted option and produce a CoT that rationalizes the response without acknowledging the hint - an instance of motivated reasoning. We study this phenomenon across multiple LLM families and datasets demonstrating that motivated reasoning can be identified by probing internal activations even in cases when it cannot be easily determined from CoT. Using supervised probes trained on the model's residual stream, we show that (i) pre-generation probes, applied before any CoT tokens are generated, predict motivated reasoning as well as a LLM-based CoT monitor that accesses the full CoT trace, and (ii) post-generation probes, applied after CoT generation, outperform the same monitor. Together, these results show that motivated reasoning is detected more reliably from internal representations than from CoT monitoring. Moreover, pre-generation probing can flag motivated behavior early, potentially avoiding unnecessary generation.
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
