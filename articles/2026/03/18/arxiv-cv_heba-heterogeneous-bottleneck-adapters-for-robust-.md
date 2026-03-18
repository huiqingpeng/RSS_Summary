---
title: "HeBA: Heterogeneous Bottleneck Adapters for Robust Vision-Language Models"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16653"
published: "2026-03-18"
fetched: "2026-03-18T18:16:53.098744"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:HeBA: Heterogeneous Bottleneck Adapters for Robust Vision-Language Models
View PDF HTML (experimental)Abstract:Adapting large-scale Vision-Language Models (VLMs) like CLIP to downstream tasks often suffers from a "one-size-fits-all" architectural approach, where visual and textual tokens are processed uniformly by wide, generic adapters. We argue that this homogeneity ignores the distinct structural nature of the modalities -- spatial locality in images versus semantic density in text. To address this, we propose HeBA (Heterogeneous Bottleneck Adapter), a unified architectural framework that introduces modality-specific structural inductive biases. HeBA departs from conventional designs through three key architectural innovations: (1) Heterogeneity: It processes visual tokens via 2D depthwise-separable convolutions to preserve spatial correlations, while distinctively processing text tokens via dense linear projections to capture semantic relationships; (2) Bottleneck Regularization: Unlike standard expanding adapters, HeBA employs a compression bottleneck (D -> D/4) that explicitly forces the model to learn compact, robust features and acts as a structural regularizer; and (3) Active Gradient Initialization: We challenge the restrictive zero-initialization paradigm, utilizing a Kaiming initialization strategy that ensures sufficient initial gradient flow to accelerate convergence without compromising the frozen backbone's pre-trained knowledge. Extensive experiments demonstrate that HeBA's architecturally specialized design achieves superior stability and accuracy, establishing a new state-of-the-art on 11 few-shot benchmarks. Code is available at this https URL.
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
