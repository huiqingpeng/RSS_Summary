---
title: "Improving Joint Audio-Video Generation with Cross-Modal Context Learning"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18600"
published: "2026-03-20"
fetched: "2026-03-20T15:12:51.218280"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 19 Mar 2026]
Title:Improving Joint Audio-Video Generation with Cross-Modal Context Learning
View PDF HTML (experimental)Abstract:The dual-stream transformer architecture-based joint audio-video generation method has become the dominant paradigm in current research. By incorporating pre-trained video diffusion models and audio diffusion models, along with a cross-modal interaction attention module, high-quality, temporally synchronized audio-video content can be generated with minimal training data. In this paper, we first revisit the dual-stream transformer paradigm and further analyze its limitations, including model manifold variations caused by the gating mechanism controlling cross-modal interactions, biases in multi-modal background regions introduced by cross-modal attention, and the inconsistencies in multi-modal classifier-free guidance (CFG) during training and inference, as well as conflicts between multiple conditions. To alleviate these issues, we propose Cross-Modal Context Learning (CCL), equipped with several carefully designed modules. Temporally Aligned RoPE and Partitioning (TARP) effectively enhances the temporal alignment between audio latent and video latent representations. The Learnable Context Tokens (LCT) and Dynamic Context Routing (DCR) in the Cross-Modal Context Attention (CCA) module provide stable unconditional anchors for cross-modal information, while dynamically routing based on different training tasks, further enhancing the model's convergence speed and generation quality. During inference, Unconditional Context Guidance (UCG) leverages the unconditional support provided by LCT to facilitate different forms of CFG, improving train-inference consistency and further alleviating conflicts. Through comprehensive evaluations, CCL achieves state-of-the-art performance compared with recent academic methods while requiring substantially fewer resources.
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
