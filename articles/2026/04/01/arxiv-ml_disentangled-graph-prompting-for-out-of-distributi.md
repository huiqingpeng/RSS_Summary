---
title: "Disentangled Graph Prompting for Out-Of-Distribution Detection"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.29644"
published: "2026-04-01"
fetched: "2026-04-02T07:19:16.583333"
---

Computer Science > Machine Learning
[Submitted on 31 Mar 2026]
Title:Disentangled Graph Prompting for Out-Of-Distribution Detection
View PDF HTML (experimental)Abstract:When testing data and training data come from different distributions, deep neural networks (DNNs) will face significant safety risks in practical applications. Therefore, out-of-distribution (OOD) detection techniques, which can identify OOD samples at test time and alert the system, are urgently needed. Existing graph OOD detection methods usually characterize fine-grained in-distribution (ID) patterns from multiple perspectives, and train end-to-end graph neural networks (GNNs) for prediction. However, due to the unavailability of OOD data during training, the absence of explicit supervision signals could lead to sub-optimal performance of end-to-end encoders. To address this issue, we follow the pre-training+prompting paradigm to utilize pre-trained GNN encoders, and propose Disentangled Graph Prompting (DGP), to capture fine-grained ID patterns with the help of ID graph labels. Specifically, we design two prompt generators that respectively generate class-specific and class-agnostic prompt graphs by modifying the edge weights of an input graph. We also design several effective losses to train the prompt generators and prevent trivial solutions. We conduct extensive experiments on ten datasets to demonstrate the superiority of our proposed DGP, which achieves a relative AUC improvement of 3.63% over the best graph OOD detection baseline. Ablation studies and hyper-parameter experiments further show the effectiveness of DGP. Code is available at this https URL.
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
