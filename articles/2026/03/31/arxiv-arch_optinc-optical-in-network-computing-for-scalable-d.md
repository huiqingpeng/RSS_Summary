---
title: "OptINC: Optical In-Network-Computing for Scalable Distributed Learning"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.28290"
published: "2026-03-31"
fetched: "2026-04-01T07:17:01.478850"
---

Computer Science > Machine Learning
[Submitted on 30 Mar 2026]
Title:OptINC: Optical In-Network-Computing for Scalable Distributed Learning
View PDF HTML (experimental)Abstract:Distributed learning is widely used for training large models on large datasets by distributing parts of the model or dataset across multiple devices and aggregating the computed results for subsequent computations or parameter updates. Existing communication algorithms for distributed learning such as ring all-reduce result in heavy communication overhead between servers. Since communication in large-scale systems uses optical fibers, we propose an Optical In-Network-Computing (OptINC) architecture to offload the computation in servers onto the optical interconnects. To execute gradient averaging and quantization in the optical domain, we incorporate optical devices such as Mach-Zehnder-Interferometers (MZIs) into the interconnects. Such a de facto optical neural network (ONN) can effectively reduce the communication overhead in existing distributed training solutions. To reduce dataset complexity for training this neural network, a preprocessing algorithm implemented in the optical domain is also proposed. Hardware cost is lowered by approximating the weight matrices of the optical neural network with unitary and diagonal matrices, while the accuracy is maintained by a proposed hardware-aware training algorithm. The proposed solution was evaluated on real distributed learning tasks, including ResNet50 on CIFAR-100, and a LLaMA-based network on Wikipedia-1B. In both cases, the proposed framework can achieve comparable training accuracy to the ring all-reduce baseline, while eliminating communication overhead.
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
