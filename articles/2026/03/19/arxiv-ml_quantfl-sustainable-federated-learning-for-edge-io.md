---
title: "QuantFL: Sustainable Federated Learning for Edge IoT via Pre-Trained Model Quantisation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17507"
published: "2026-03-19"
fetched: "2026-03-19T12:12:26.722633"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:QuantFL: Sustainable Federated Learning for Edge IoT via Pre-Trained Model Quantisation
View PDF HTML (experimental)Abstract:Federated Learning (FL) enables privacy-preserving intelligence on Internet of Things (IoT) devices but incurs a significant carbon footprint due to the high energy cost of frequent uplink transmission. While pre-trained models are increasingly available on edge devices, their potential to reduce the energy overhead of fine-tuning remains underexplored. In this work, we propose QuantFL, a sustainable FL framework that leverages pre-trained initialisation to enable aggressive, computationally lightweight quantisation. We demonstrate that pre-training naturally concentrates update statistics, allowing us to use memory-efficient bucket quantisation without the energy-intensive overhead of complex error-feedback mechanisms. On MNIST and CIFAR-100, QuantFL reduces total communication by 40\% ($\simeq40\%$ total-bit reduction with full-precision downlink; $\geq80\%$ on uplink or when downlink is quantised) while matching or exceeding uncompressed baselines under strict bandwidth budgets; BU attains 89.00\% (MNIST) and 66.89\% (CIFAR-100) test accuracy with orders of magnitude fewer bits. We also account for uplink and downlink costs and provide ablations on quantisation levels and initialisation. QuantFL delivers a practical, "green" recipe for scalable training on battery-constrained IoT networks.
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
