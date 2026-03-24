---
title: "Does This Gradient Spark Joy?"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20526"
published: "2026-03-24"
fetched: "2026-03-25T07:10:57.703978"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:Does This Gradient Spark Joy?
View PDF HTML (experimental)Abstract:Policy gradient computes a backward pass for every sample, even though the backward pass is expensive and most samples carry little learning value. The Delightful Policy Gradient (DG) provides a forward-pass signal of learning value: \emph{delight}, the product of advantage and surprisal (negative log-probability). We introduce the \emph{Kondo gate}, which compares delight against a compute price and pays for a backward pass only when the sample is worth it, thereby tracing a quality--cost Pareto frontier. In bandits, zero-price gating preserves useful gradient signal while removing perpendicular noise, and delight is a more reliable screening signal than additive combinations of value and surprise. On MNIST and transformer token reversal, the Kondo gate skips most backward passes while retaining nearly all of DG's learning quality, with gains that grow as problems get harder and backward passes become more expensive. Because the gate tolerates approximate delight, a cheap forward pass can screen samples before expensive backpropagation, suggesting a speculative-decoding-for-training paradigm.
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
