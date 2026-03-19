---
title: "Motion-Adaptive Temporal Attention for Lightweight Video Generation with Stable Diffusion"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17398"
published: "2026-03-19"
fetched: "2026-03-19T15:10:12.199367"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:Motion-Adaptive Temporal Attention for Lightweight Video Generation with Stable Diffusion
View PDF HTML (experimental)Abstract:We present a motion-adaptive temporal attention mechanism for parameter-efficient video generation built upon frozen Stable Diffusion models. Rather than treating all video content uniformly, our method dynamically adjusts temporal attention receptive fields based on estimated motion content: high-motion sequences attend locally across frames to preserve rapidly changing details, while low-motion sequences attend globally to enforce scene consistency. We inject lightweight temporal attention modules into all UNet transformer blocks via a cascaded strategy -- global attention in down-sampling and middle blocks for semantic stabilization, motion-adaptive attention in up-sampling blocks for fine-grained refinement. Combined with temporally correlated noise initialization and motion-aware gating, the system adds only 25.8M trainable parameters (2.9\% of the base UNet) while achieving competitive results on WebVid validation when trained on 100K videos. We demonstrate that the standard denoising objective alone provides sufficient implicit temporal regularization, outperforming approaches that add explicit temporal consistency losses. Our ablation studies reveal a clear trade-off between noise correlation and motion amplitude, providing a practical inference-time control for diverse generation behaviors.
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
