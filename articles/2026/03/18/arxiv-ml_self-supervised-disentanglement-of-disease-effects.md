---
title: "Self-supervised Disentanglement of Disease Effects from Aging in 3D Medical Shapes"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15862"
published: "2026-03-18"
fetched: "2026-03-18T16:08:22.567653"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 16 Mar 2026]
Title:Self-supervised Disentanglement of Disease Effects from Aging in 3D Medical Shapes
View PDF HTML (experimental)Abstract:Disentangling pathological changes from physiological aging in 3D medical shapes is crucial for developing interpretable biomarkers and patient stratification. However, this separation is challenging when diagnosis labels are limited or unavailable, since disease and aging often produce overlapping effects on shape changes, obscuring clinically relevant shape patterns. To address this challenge, we propose a two-stage framework combining unsupervised disease discovery with self-supervised disentanglement of implicit shape representations. In the first stage, we train an implicit neural model with signed distance functions to learn stable shape embeddings. We then apply clustering on the shape latent space, which yields pseudo disease labels without using ground-truth diagnosis during discovery. In the second stage, we disentangle factors in a compact variational space using pseudo disease labels discovered in the first stage and the ground truth age labels available for all subjects. We enforce separation and controllability with a multi-objective disentanglement loss combining covariance and a supervised contrastive loss. On ADNI hippocampus and OAI distal femur shapes, we achieve near-supervised performance, improving disentanglement and reconstruction over state-of-the-art unsupervised baselines, while enabling high-fidelity reconstruction, controllable synthesis, and factor-based explainability. Code and checkpoints are available at this https URL
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
