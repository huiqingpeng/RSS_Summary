---
title: "MKA: Memory-Keyed Attention for Efficient Long-Context Reasoning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20586"
published: "2026-03-24"
fetched: "2026-03-25T07:11:48.285695"
---

Computer Science > Machine Learning
[Submitted on 21 Mar 2026]
Title:MKA: Memory-Keyed Attention for Efficient Long-Context Reasoning
View PDF HTML (experimental)Abstract:As long-context language modeling becomes increasingly important, the cost of maintaining and attending to large Key/Value (KV) caches grows rapidly, becoming a major bottleneck in both training and inference. While prior works such as Multi-Query Attention (MQA) and Multi-Latent Attention (MLA) reduce memory by sharing or compressing KV features, they often trade off representation quality or incur runtime overhead. We propose Memory-Keyed Attention (MKA), a hierarchical attention mechanism that integrates multi-level KV caches (local, session, and long-term) and learns to route attention across them dynamically. We further introduce Route-Fused MKA (FastMKA), a broadcast-routed variant that fuses memory sources before attention computation for improved efficiency. Experiments on different sequence lengths show that FastMKA achieves a favorable accuracy-efficiency trade-off: comparable perplexity to MLA while achieving up to 5x faster training throughput and 1.8x lower evaluation latency. These results highlight MKA as a practical and extensible framework for efficient long-context attention.
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
