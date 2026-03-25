---
title: "Mitigating Premature Discretization with Progressive Quantization for Robust Vector Tokenization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22304"
published: "2026-03-25"
fetched: "2026-03-26T07:09:07.738106"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:Mitigating Premature Discretization with Progressive Quantization for Robust Vector Tokenization
View PDF HTML (experimental)Abstract:Vector Quantization (VQ) has become the cornerstone of tokenization for many multimodal Large Language Models and diffusion synthesis. However, existing VQ paradigms suffer from a fundamental conflict: they enforce discretization before the encoder has captured the underlying data manifold. We term this phenomenon Premature Discretization. To resolve this, we propose Progressive Quantization (ProVQ), which incorporates the dynamics of quantization hardness as a fundamental yet previously overlooked axis in VQ training. By treating quantization as a curriculum that smoothly anneals from a continuous latent space to a discrete one, ProVQ effectively guides the codebook toward the well-expanded manifolds. Extensive experimental results demonstrate the broad effectiveness of ProVQ across diverse modalities. We report improved reconstruction and generative performance on the ImageNet-1K and ImageNet-100 benchmarks, highlighting the ProVQ's boost for generative modeling. Furthermore, ProVQ proves highly effective for modeling complex biological sequences, establishing a new performance ceiling for protein structure tokenization on the StrutTokenBench leaderboard.
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
