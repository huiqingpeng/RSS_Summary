---
title: "VirPro: Visual-referred Probabilistic Prompt Learning for Weakly-Supervised Monocular 3D Detection"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17470"
published: "2026-03-19"
fetched: "2026-03-19T15:11:20.826642"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:VirPro: Visual-referred Probabilistic Prompt Learning for Weakly-Supervised Monocular 3D Detection
View PDF HTML (experimental)Abstract:Monocular 3D object detection typically relies on pseudo-labeling techniques to reduce dependency on real-world annotations. Recent advances demonstrate that deterministic linguistic cues can serve as effective auxiliary weak supervision signals, providing complementary semantic context. However, hand-crafted textual descriptions struggle to capture the inherent visual diversity of individuals across scenes, limiting the model's ability to learn scene-aware representations. To address this challenge, we propose Visual-referred Probabilistic Prompt Learning (VirPro), an adaptive multi-modal pretraining paradigm that can be seamlessly integrated into diverse weakly supervised monocular 3D detection frameworks. Specifically, we generate a diverse set of learnable, instance-conditioned prompts across scenes and store them in an Adaptive Prompt Bank (APB). Subsequently, we introduce Multi-Gaussian Prompt Modeling (MGPM), which incorporates scene-based visual features into the corresponding textual embeddings, allowing the text prompts to express visual uncertainties. Then, from the fused vision-language embeddings, we decode a prompt-targeted Gaussian, from which we derive a unified object-level prompt embedding for each instance. RoI-level contrastive matching is employed to enforce modality alignment, bringing embeddings of co-occurring objects within the same scene closer in the latent space, thus enhancing semantic coherence. Extensive experiments on the KITTI benchmark demonstrate that integrating our pretraining paradigm consistently yields substantial performance gains, achieving up to a 4.8% average precision improvement than the baseline.
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
