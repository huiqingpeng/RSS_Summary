---
title: "Probabilistic Federated Learning on Uncertain and Heterogeneous Data with Model Personalization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18083"
published: "2026-03-20"
fetched: "2026-03-20T12:07:16.113024"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:Probabilistic Federated Learning on Uncertain and Heterogeneous Data with Model Personalization
View PDF HTML (experimental)Abstract:Conventional federated learning (FL) frameworks often suffer from training degradation due to data uncertainty and heterogeneity across local clients. Probabilistic approaches such as Bayesian neural networks (BNNs) can mitigate this issue by explicitly modeling uncertainty, but they introduce additional runtime, latency, and bandwidth overhead that has rarely been studied in federated settings. To address these challenges, we propose Meta-BayFL, a personalized probabilistic FL method that combines meta-learning with BNNs to improve training under uncertain and heterogeneous data. The framework is characterized by three main features: (1) BNN-based client models incorporate uncertainty across hidden layers to stabilize training on small and noisy datasets, (2) meta-learning with adaptive learning rates enables personalized updates that enhance local training under non-IID conditions, and (3) a unified probabilistic and personalized design improves the robustness of global model aggregation. We provide a theoretical convergence analysis and characterize the upper bound of the global model over communication rounds. In addition, we evaluate computational costs (runtime, latency, and communication) and discuss the feasibility of deployment on resource-constrained devices such as edge nodes and IoT systems. Extensive experiments on CIFAR-10, CIFAR-100, and Tiny-ImageNet show that Meta-BayFL consistently outperforms state-of-the-art methods, including both standard and personalized FL approaches (e.g., pFedMe, Ditto, FedFomo), with up to 7.42\% higher test accuracy.
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
