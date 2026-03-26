---
title: "Reservoir-Based Graph Convolutional Networks"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24131"
published: "2026-03-26"
fetched: "2026-03-27T07:21:10.022704"
---

Computer Science > Machine Learning
[Submitted on 25 Mar 2026]
Title:Reservoir-Based Graph Convolutional Networks
View PDF HTML (experimental)Abstract:Message passing is a core mechanism in Graph Neural Networks (GNNs), enabling the iterative update of node embeddings by aggregating information from neighboring nodes. Graph Convolutional Networks (GCNs) exemplify this approach by adapting convolutional operations for graph structures, allowing features from adjacent nodes to be combined effectively. However, GCNs encounter challenges with complex or dynamic data. Capturing long-range dependencies often requires deeper layers, which not only increase computational costs but also lead to over-smoothing, where node embeddings become indistinguishable. To overcome these challenges, reservoir computing has been integrated into GNNs, leveraging iterative message-passing dynamics for stable information propagation without extensive parameter tuning. Despite its promise, existing reservoir-based models lack structured convolutional mechanisms, limiting their ability to accurately aggregate multi-hop neighborhood information. To address these limitations, we propose RGC-Net (Reservoir-based Graph Convolutional Network), which integrates reservoir dynamics with structured graph convolution. Key contributions include: (i) a reimagined convolutional framework with fixed random reservoir weights and a leaky integrator to enhance feature retention; (ii) a robust, adaptable model for graph classification; and (iii) an RGC-Net-powered transformer for graph generation with application to dynamic brain connectivity. Extensive experiments show that RGC-Net achieves state-of-the-art performance in classification and generative tasks, including brain graph evolution, with faster convergence and reduced over-smoothing. Source code is available at this https URL .
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
