---
title: "Attribution Upsampling should Redistribute, Not Interpolate"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16067"
published: "2026-03-18"
fetched: "2026-03-18T16:10:04.429926"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:Attribution Upsampling should Redistribute, Not Interpolate
View PDF HTML (experimental)Abstract:Attribution methods in explainable AI rely on upsampling techniques that were designed for natural images, not saliency maps. Standard bilinear and bicubic interpolation systematically corrupts attribution signals through aliasing, ringing, and boundary bleeding, producing spurious high-importance regions that misrepresent model reasoning. We identify that the core issue is treating attribution upsampling as an interpolation problem that operates in isolation from the model's reasoning, rather than a mass redistribution problem where model-derived semantic boundaries must govern how importance flows. We present Universal Semantic-Aware Upsampling (USU), a principled method that reformulates upsampling through ratio-form mass redistribution operators, provably preserving attribution mass and relative importance ordering. Extending the axiomatic tradition of feature attribution to upsampling, we formalize four desiderata for faithful upsampling and prove that interpolation structurally violates three of them. These same three force any redistribution operator into a ratio form; the fourth selects the unique potential within this family, yielding USU. Controlled experiments on models with known attribution priors verify USU's formal guarantees; evaluation across ImageNet, CIFAR-10, and CUB-200 confirms consistent faithfulness improvements and qualitatively superior, semantically coherent explanations.
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
