---
title: "Big2Small: A Unifying Neural Network Framework for Model Compression"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.29768"
published: "2026-04-01"
fetched: "2026-04-02T07:20:08.080502"
---

Computer Science > Machine Learning
[Submitted on 31 Mar 2026]
Title:Big2Small: A Unifying Neural Network Framework for Model Compression
View PDF HTML (experimental)Abstract:With the development of foundational models, model compression has become a critical requirement. Various model compression approaches have been proposed such as low-rank decomposition, pruning, quantization, ergodic dynamic systems, and knowledge distillation, which are based on different heuristics. To elevate the field from fragmentation to a principled discipline, we construct a unifying mathematical framework for model compression grounded in measure theory. We further demonstrate that each model compression technique is mathematically equivalent to a neural network subject to a regularization. Building upon this mathematical and structural equivalence, we propose an experimentally-verified data-free model compression framework, termed \textit{Big2Small}, which translates Implicit Neural Representations (INRs) from data domain to the domain of network parameters. \textit{Big2Small} trains compact INRs to encode the weights of larger models and reconstruct the weights during inference. To enhance reconstruction fidelity, we introduce Outlier-Aware Preprocessing to handle extreme weight values and a Frequency-Aware Loss function to preserve high-frequency details. Experiments on image classification and segmentation demonstrate that \textit{Big2Small} achieves competitive accuracy and compression ratios compared to state-of-the-art baselines.
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
