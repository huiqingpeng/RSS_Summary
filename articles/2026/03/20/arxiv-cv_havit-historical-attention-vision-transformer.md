---
title: "HAViT: Historical Attention Vision Transformer"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18585"
published: "2026-03-20"
fetched: "2026-03-20T15:11:51.584984"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 19 Mar 2026]
Title:HAViT: Historical Attention Vision Transformer
View PDF HTML (experimental)Abstract:Vision Transformers have excelled in computer vision but their attention mechanisms operate independently across layers, limiting information flow and feature learning. We propose an effective cross-layer attention propagation method that preserves and integrates historical attention matrices across encoder layers, offering a principled refinement of inter-layer information flow in Vision Transformers. This approach enables progressive refinement of attention patterns throughout the transformer hierarchy, enhancing feature acquisition and optimization dynamics. The method requires minimal architectural changes, adding only attention matrix storage and blending operations. Comprehensive experiments on CIFAR-100 and TinyImageNet demonstrate consistent accuracy improvements, with ViT performance increasing from 75.74% to 77.07% on CIFAR-100 (+1.33%) and from 57.82% to 59.07% on TinyImageNet (+1.25%). Cross-architecture validation shows similar gains across transformer variants, with CaiT showing 1.01% enhancement. Systematic analysis identifies the blending hyperparameter of historical attention (alpha = 0.45) as optimal across all configurations, providing the ideal balance between current and historical attention information. Random initialization consistently outperforms zero initialization, indicating that diverse initial attention patterns accelerate convergence and improve final performance. Our code is publicly available at this https URL.
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
