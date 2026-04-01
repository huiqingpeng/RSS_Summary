---
title: "DiSGMM: A Method for Time-varying Microscopic Weight Completion on Road Networks"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.29837"
published: "2026-04-01"
fetched: "2026-04-02T07:20:57.385835"
---

Computer Science > Machine Learning
[Submitted on 31 Mar 2026]
Title:DiSGMM: A Method for Time-varying Microscopic Weight Completion on Road Networks
View PDF HTML (experimental)Abstract:Microscopic road-network weights represent fine-grained, time-varying traffic conditions obtained from individual vehicles. An example is travel speeds associated with road segments as vehicles traverse them. These weights support tasks including traffic microsimulation and vehicle routing with reliability guarantees. We study the problem of time-varying microscopic weight completion. During a time slot, the available weights typically cover only some road segments. Weight completion recovers distributions for the weights of every road segment at the current time slot. This problem involves two challenges: (i) contending with two layers of sparsity, where weights are missing at both the network layer (many road segments lack weights) and the segment layer (a segment may have insufficient weights to enable accurate distribution estimation); and (ii) achieving a weight distribution representation that is closed-form and can capture complex conditions flexibly, including heavy tails and multiple clusters.
To address these challenges, we propose DiSGMM that combines sparsity-aware embeddings with spatiotemporal modeling to leverage sparse known weights alongside learned segment properties and long-range correlations for distribution estimation. DiSGMM represents distributions of microscopic weights as learnable Gaussian mixture models, providing closed-form distributions capable of capturing complex conditions flexibly. Experiments on two real-world datasets show that DiSGMM can outperform state-of-the-art methods.
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
