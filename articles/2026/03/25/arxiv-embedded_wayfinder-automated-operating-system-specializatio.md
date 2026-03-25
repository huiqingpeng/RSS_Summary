---
title: "Wayfinder: Automated Operating System Specialization"
source: "arXiv Embedded Systems"
url: "https://arxiv.org/abs/2603.23425"
published: "2026-03-25"
fetched: "2026-03-26T07:05:16.980005"
---

Computer Science > Operating Systems
[Submitted on 24 Mar 2026]
Title:Wayfinder: Automated Operating System Specialization
View PDF HTML (experimental)Abstract:Specializing an OS to optimize the performance of a particular application is typically a manual process that requires great expertise. Specialization through configuration lends itself well to automation; however, it is challenging due to the sheer size of the configuration space of modern OSes, the difficulty to quantify that space, the long time it takes to evaluate a configuration, and the large number of invalid configurations. Hence, existing attempts at specializing OSes automatically are limited to switching features on and off to minimize memory consumption or attack surface, and cannot target metrics such as performance.
We present Wayfinder, a framework specializing the configuration of OSes completely automatically and without expert knowledge. It can specialize all aspects of an OS configuration (compile-/boot-/run-time) towards any quantifiable performance, resource consumption, or security metric, for an application processing a given workload on a given hardware setup. Wayfinder consists of an automated OS benchmarking platform, and a neural network-based search algorithm driving the specialization process. This is achieved by learning on the fly which configuration parameters and values impact performance the most, and which ones lead to runtime failures. Optionally, a model pre-trained on one application can be reused to accelerate the specialization of related applications. We evaluate Wayfinder on two OSes, four applications, and two target metrics: Wayfinder fully automatically identifies specialized configurations with up to 24% application performance improvement and 8.5% memory usage reduction compared to default configurations. We highlight the benefits of our neural network, reaching good solutions faster than competing approaches (random and Bayesian), and successfully transferring knowledge between related applications.
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
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
