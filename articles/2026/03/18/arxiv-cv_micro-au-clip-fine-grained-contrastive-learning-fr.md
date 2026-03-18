---
title: "Micro-AU CLIP: Fine-Grained Contrastive Learning from Local Independence to Global Dependency for Micro-Expression Action Unit Detection"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16302"
published: "2026-03-18"
fetched: "2026-03-18T18:10:40.014526"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:Micro-AU CLIP: Fine-Grained Contrastive Learning from Local Independence to Global Dependency for Micro-Expression Action Unit Detection
View PDF HTML (experimental)Abstract:Micro-expression (ME) action units (Micro-AUs) provide objective clues for fine-grained genuine emotion analysis. Most existing Micro-AU detection methods learn AU features from the whole facial image/video, which conflicts with the inherent locality of AU, resulting in insufficient perception of AU regions. In fact, each AU independently corresponds to specific localized facial muscle movements (local independence), while there is an inherent dependency between some AUs under specific emotional states (global dependency). Thus, this paper explores the effectiveness of the independence-to-dependency pattern and proposes a novel micro-AU detection framework, micro-AU CLIP, that uniquely decomposes the AU detection process into local semantic independence modeling (LSI) and global semantic dependency (GSD) modeling. In LSI, Patch Token Attention (PTA) is designed, mapping several local features within the AU region to the same feature space; In GSD, Global Dependency Attention (GDA) and Global Dependency Loss (GDLoss) are presented to model the global dependency relationships between different AUs, thereby enhancing each AU feature. Furthermore, considering CLIP's native limitations in micro-semantic alignment, a microAU contrastive loss (MiAUCL) is designed to learn AU features by a fine-grained alignment of visual and text features. Also, Micro-AU CLIP is effectively applied to ME recognition in an emotion-label-free way. The experimental results demonstrate that Micro-AU CLIP can fully learn fine-grained micro-AU features, achieving state-of-the-art performance.
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
