---
title: "CompDiff: Hierarchical Compositional Diffusion for Fair and Zero-Shot Intersectional Medical Image Generation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16551"
published: "2026-03-18"
fetched: "2026-03-18T18:14:38.473184"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:CompDiff: Hierarchical Compositional Diffusion for Fair and Zero-Shot Intersectional Medical Image Generation
View PDF HTML (experimental)Abstract:Generative models are increasingly used to augment medical imaging datasets for fairer AI. Yet a key assumption often goes unexamined: that generators themselves produce equally high-quality images across demographic groups. Models trained on imbalanced data can inherit these imbalances, yielding degraded synthesis quality for rare subgroups and struggling with demographic intersections absent from training. We refer to this as the imbalanced generator problem. Existing remedies such as loss reweighting operate at the optimization level and provide limited benefit when training signal is scarce or absent for certain combinations. We propose CompDiff, a hierarchical compositional diffusion framework that addresses this problem at the representation level. A dedicated Hierarchical Conditioner Network (HCN) decomposes demographic conditioning, producing a demographic token concatenated with CLIP embeddings as cross-attention context. This structured factorization encourages parameter sharing across subgroups and supports compositional generalization to rare or unseen demographic intersections. Experiments on chest X-rays (MIMIC-CXR) and fundus images (FairGenMed) show that CompDiff compares favorably against both standard fine-tuning and FairDiffusion across image quality (FID: 64.3 vs. 75.1), subgroup equity (ES-FID), and zero-shot intersectional generalization (up to 21% FID improvement on held-out intersections). Downstream classifiers trained on CompDiff-generated data also show improved AUROC and reduced demographic bias, suggesting that architectural design of demographic conditioning is an important and underexplored factor in fair medical image generation. Code is available at this https URL.
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
