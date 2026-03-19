---
title: "Gaussian Process Limit Reveals Structural Benefits of Graph Transformers"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17569"
published: "2026-03-19"
fetched: "2026-03-19T13:13:42.492810"
---

Statistics > Machine Learning
[Submitted on 18 Mar 2026]
Title:Gaussian Process Limit Reveals Structural Benefits of Graph Transformers
View PDF HTML (experimental)Abstract:Graph transformers are the state-of-the-art for learning from graph-structured data and are empirically known to avoid several pitfalls of message-passing architectures. However, there is limited theoretical analysis on why these models perform well in practice. In this work, we prove that attention-based architectures have structural benefits over graph convolutional networks in the context of node-level prediction tasks. Specifically, we study the neural network gaussian process limits of graph transformers (GAT, Graphormer, Specformer) with infinite width and infinite heads, and derive the node-level and edge-level kernels across the layers. Our results characterise how the node features and the graph structure propagate through the graph attention layers. As a specific example, we prove that graph transformers structurally preserve community information and maintain discriminative node representations even in deep layers, thereby preventing oversmoothing. We provide empirical evidence on synthetic and real-world graphs that validate our theoretical insights, such as integrating informative priors and positional encoding can improve performance of deep graph transformers.
Current browse context:
stat.ML
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
