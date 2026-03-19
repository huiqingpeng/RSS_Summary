---
title: "ProGVC: Progressive-based Generative Video Compression via Auto-Regressive Context Modeling"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17546"
published: "2026-03-19"
fetched: "2026-03-19T15:13:30.619209"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:ProGVC: Progressive-based Generative Video Compression via Auto-Regressive Context Modeling
View PDF HTML (experimental)Abstract:Perceptual video compression leverages generative priors to reconstruct realistic textures and motions at low bitrates. However, existing perceptual codecs often lack native support for variable bitrate and progressive delivery, and their generative modules are weakly coupled with entropy coding, limiting bitrate reduction. Inspired by the next-scale prediction in the Visual Auto-Regressive (VAR) models, we propose ProGVC, a Progressive-based Generative Video Compression framework that unifies progressive transmission, efficient entropy coding, and detail synthesis within a single codec. ProGVC encodes videos into hierarchical multi-scale residual token maps, enabling flexible rate adaptation by transmitting a coarse-to-fine subset of scales in a progressive manner. A Transformer-based multi-scale autoregressive context model estimates token probabilities, utilized both for efficient entropy coding of the transmitted tokens and for predicting truncated fine-scale tokens at the decoder to restore perceptual details. Extensive experiments demonstrate that as a new coding paradigm, ProGVC delivers promising perceptual compression performance at low bitrates while offering practical scalability at the same time.
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
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
