---
title: "SoulX-LiveAct: Towards Hour-Scale Real-Time Human Animation with Neighbor Forcing and ConvKV Memory"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.11746"
published: "2026-03-20"
fetched: "2026-03-20T16:18:44.937257"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 12 Mar 2026 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:SoulX-LiveAct: Towards Hour-Scale Real-Time Human Animation with Neighbor Forcing and ConvKV Memory
View PDF HTML (experimental)Abstract:Autoregressive (AR) diffusion models offer a promising framework for sequential generation tasks such as video synthesis by combining diffusion modeling with causal inference. Although they support streaming generation, existing AR diffusion methods struggle to scale efficiently. In this paper, we identify two key challenges in hour-scale real-time human animation. First, most forcing strategies propagate sample-level representations with mismatched diffusion states, causing inconsistent learning signals and unstable convergence. Second, historical representations grow unbounded and lack structure, preventing effective reuse of cached states and severely limiting inference efficiency. To address these challenges, we propose Neighbor Forcing, a diffusion-step-consistent AR formulation that propagates temporally adjacent frames as latent neighbors under the same noise condition. This design provides a distribution-aligned and stable learning signal while preserving drifting throughout the AR chain. Building upon this, we introduce a structured ConvKV memory mechanism that compresses the keys and values in causal attention into a fixed-length representation, enabling constant-memory inference and truly infinite video generation without relying on short-term motion-frame memory. Extensive experiments demonstrate that our approach significantly improves training convergence, hour-scale generation quality, and inference efficiency compared to existing AR diffusion methods. Numerically, LiveAct enables hour-scale real-time human animation and supports 20 FPS real-time streaming inference on as few as two NVIDIA H100 or H200 GPUs. Quantitative results demonstrate that our method attains state-of-the-art performance in lip-sync accuracy, human animation quality, and emotional expressiveness, with the lowest inference cost.
Submission history
From: Xu Zheng [view email][v1] Thu, 12 Mar 2026 09:49:58 UTC (2,356 KB)
[v2] Wed, 18 Mar 2026 19:19:24 UTC (2,357 KB)
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
