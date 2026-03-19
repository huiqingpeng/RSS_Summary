---
title: "Revisiting Cross-Attention Mechanisms: Leveraging Beneficial Noise for Domain-Adaptive Learning"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17474"
published: "2026-03-19"
fetched: "2026-03-19T15:11:31.141849"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:Revisiting Cross-Attention Mechanisms: Leveraging Beneficial Noise for Domain-Adaptive Learning
View PDF HTML (experimental)Abstract:Unsupervised Domain Adaptation (UDA) seeks to transfer knowledge from a labeled source domain to an unlabeled target domain but often suffers from severe domain and scale gaps that degrade performance. Existing cross-attention-based transformers can align features across domains, yet they struggle to preserve content semantics under large appearance and scale variations. To explicitly address these challenges, we introduce the concept of beneficial noise, which regularizes cross-attention by injecting controlled perturbations, encouraging the model to ignore style distractions and focus on content. We propose the Domain-Adaptive Cross-Scale Matching (DACSM) framework, which consists of a Domain-Adaptive Transformer (DAT) for disentangling domain-shared content from domain-specific style, and a Cross-Scale Matching (CSM) module that adaptively aligns features across multiple resolutions. DAT incorporates beneficial noise into cross-attention, enabling progressive domain translation with enhanced robustness, yielding content-consistent and style-invariant representations. Meanwhile, CSM ensures semantic consistency under scale changes. Extensive experiments on VisDA-2017, Office-Home, and DomainNet demonstrate that DACSM achieves state-of-the-art performance, with up to +2.3% improvement over CDTrans on VisDA-2017. Notably, DACSM achieves a +5.9% gain on the challenging "truck" class of VisDA, evidencing the strength of beneficial noise in handling scale discrepancies. These results highlight the effectiveness of combining domain translation, beneficial-noise-enhanced attention, and scale-aware alignment for robust cross-domain representation learning.
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
