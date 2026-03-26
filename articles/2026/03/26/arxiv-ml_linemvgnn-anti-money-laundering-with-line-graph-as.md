---
title: "LineMVGNN: Anti-Money Laundering with Line-Graph-Assisted Multi-View Graph Neural Networks"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23584"
published: "2026-03-26"
fetched: "2026-03-27T07:15:51.868557"
---

Computer Science > Machine Learning
[Submitted on 24 Mar 2026]
Title:LineMVGNN: Anti-Money Laundering with Line-Graph-Assisted Multi-View Graph Neural Networks
View PDF HTML (experimental)Abstract:Anti-money laundering (AML) systems are important for protecting the global economy. However, conventional rule-based methods rely on domain knowledge, leading to suboptimal accuracy and a lack of scalability. Graph neural networks (GNNs) for digraphs (directed graphs) can be applied to transaction graphs and capture suspicious transactions or accounts. However, most spectral GNNs do not naturally support multi-dimensional edge features, lack interpretability due to edge modifications, and have limited scalability owing to their spectral nature. Conversely, most spatial methods may not capture the money flow well. Therefore, in this work, we propose LineMVGNN (Line-Graph-Assisted Multi-View Graph Neural Network), a novel spatial method that considers payment and receipt transactions. Specifically, the LineMVGNN model extends a lightweight MVGNN module, which performs two-way message passing between nodes in a transaction graph. Additionally, LineMVGNN incorporates a line graph view of the original transaction graph to enhance the propagation of transaction information. We conduct experiments on two real-world account-based transaction datasets: the Ethereum phishing transaction network dataset and a financial payment transaction dataset from one of our industry partners. The results show that our proposed method outperforms state-of-the-art methods, reflecting the effectiveness of money laundering detection with line-graph-assisted multi-view graph learning. We also discuss scalability, adversarial robustness, and regulatory considerations of our proposed method.
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
