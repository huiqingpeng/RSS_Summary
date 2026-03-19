---
title: "Steering Video Diffusion Transformers with Massive Activations"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17825"
published: "2026-03-19"
fetched: "2026-03-19T16:16:49.844622"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:Steering Video Diffusion Transformers with Massive Activations
View PDF HTML (experimental)Abstract:Despite rapid progress in video diffusion transformers, how their internal model signals can be leveraged with minimal overhead to enhance video generation quality remains underexplored. In this work, we study the role of Massive Activations (MAs), which are rare, high-magnitude hidden state spikes in video diffusion transformers. We observed that MAs emerge consistently across all visual tokens, with a clear magnitude hierarchy: first-frame tokens exhibit the largest MA magnitudes, latent-frame boundary tokens (the head and tail portions of each temporal chunk in the latent space) show elevated but slightly lower MA magnitudes than the first frame, and interior tokens within each latent frame remain elevated, yet are comparatively moderate in magnitude. This structured pattern suggests that the model implicitly prioritizes token positions aligned with the temporal chunking in the latent space. Based on this observation, we propose Structured Activation Steering (STAS), a training-free self-guidance-like method that steers MA values at first-frame and boundary tokens toward a scaled global maximum reference magnitude. STAS achieves consistent improvements in terms of video quality and temporal coherence across different text-to-video models, while introducing negligible computational overhead.
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
