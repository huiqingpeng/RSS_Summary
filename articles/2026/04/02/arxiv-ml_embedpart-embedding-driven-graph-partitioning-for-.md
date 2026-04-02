---
title: "EmbedPart: Embedding-Driven Graph Partitioning for Scalable Graph Neural Network Training"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.01000"
published: "2026-04-02"
fetched: "2026-04-03T07:26:39.365287"
---

Computer Science > Machine Learning
[Submitted on 1 Apr 2026]
Title:EmbedPart: Embedding-Driven Graph Partitioning for Scalable Graph Neural Network Training
View PDF HTML (experimental)Abstract:Graph Neural Networks (GNNs) are widely used for learning on graph-structured data, but scaling GNN training to massive graphs remains challenging. To enable scalable distributed training, graphs are divided into smaller partitions that are distributed across multiple machines such that inter-machine communication is minimized and computational load is balanced. In practice, existing partitioning approaches face a fundamental trade-off between partitioning overhead and partitioning quality. We propose EmbedPart, an embedding-driven partitioning approach that achieves both speed and quality. Instead of operating directly on irregular graph structures, EmbedPart leverages node embeddings produced during the actual GNN training workload and clusters these dense embeddings to derive a partitioning. EmbedPart achieves more than 100x speedup over Metis while maintaining competitive partitioning quality and accelerating distributed GNN training. Moreover, EmbedPart naturally supports graph updates and fast repartitioning, and can be applied to graph reordering to improve data locality and accelerate single-machine GNN training. By shifting partitioning from irregular graph structures to dense embeddings, EmbedPart enables scalable and high-quality graph data optimization.
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
