---
title: "GAPSL: A Gradient-Aligned Parallel Split Learning on Heterogeneous Data"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18540"
published: "2026-03-20"
fetched: "2026-03-20T12:12:53.592850"
---

Computer Science > Machine Learning
[Submitted on 19 Mar 2026]
Title:GAPSL: A Gradient-Aligned Parallel Split Learning on Heterogeneous Data
View PDF HTML (experimental)Abstract:The increasing complexity of neural networks poses significant challenges for democratizing FL on resource?constrained client devices. Parallel split learning (PSL) has emerged as a promising solution by offloading substantial computing workload to a server via model partitioning, shrinking client-side computing load, and eliminating the client-side model aggregation for reduced communication and deployment costs. Since PSL is aggregation-free, it suffers from severe training divergence stemming from gradient directional inconsistency across clients. To address this challenge, we propose GAPSL, a gradient-aligned PSL framework that comprises two key components: leader gradient identification (LGI) and gradient direction alignment (GDA). LGI dynamically selects a set of directionally consistent client gradients to construct a leader gradient that captures the global convergence trend. GDA employs a direction-aware regularization to align each client's gradient with the leader gradient, thereby mitigating inter-device gradient directional inconsistency and enhancing model convergence. We evaluate GAPSL on a prototype computing testbed. Extensive experiments demonstrate that GAPSL consistently outperforms state-of-the-art benchmarks in training accuracy and latency.
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
