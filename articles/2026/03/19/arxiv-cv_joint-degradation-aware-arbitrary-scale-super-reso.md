---
title: "Joint Degradation-Aware Arbitrary-Scale Super-Resolution for Variable-Rate Extreme Image Compression"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17408"
published: "2026-03-19"
fetched: "2026-03-19T15:10:24.042708"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:Joint Degradation-Aware Arbitrary-Scale Super-Resolution for Variable-Rate Extreme Image Compression
View PDF HTML (experimental)Abstract:Recent diffusion-based extreme image compression methods have demonstrated remarkable performance at ultra-low bitrates. However, most approaches require training separate diffusion models for each target bitrate, resulting in substantial computational overhead and hindering practical deployment. Meanwhile, recent studies have shown that joint super-resolution can serve as an effective approach for enhancing low-bitrate reconstruction. However, when moving toward ultra-low bitrate regimes, these methods struggle due to severe information loss, and their reliance on fixed super-resolution scales prevents flexible adaptation across diverse bitrates.
To address these limitations, we propose ASSR-EIC, a novel image compression framework that leverages arbitrary-scale super-resolution (ASSR) to support variable-rate extreme image compression (EIC). An arbitrary-scale downsampling module is introduced at the encoder side to provide controllable rate reduction, while a diffusion-based, joint degradation-aware ASSR decoder enables rate-adaptive reconstruction within a single model. We exploit the compression- and rescaling-aware diffusion prior to guide the reconstruction, yielding high fidelity and high realism restoration across diverse compression and rescaling settings. Specifically, we design a global compression-rescaling adaptor that offers holistic guidance for rate adaptation, and a local compression-rescaling modulator that dynamically balances generative and fidelity-oriented behaviors to achieve fine-grained, bitrate-adaptive detail restoration. To further enhance reconstruction quality, we introduce a dual semantic-enhanced design.
Extensive experiments demonstrate that ASSR-EIC delivers state-of-the-art performance in extreme image compression while simultaneously supporting flexible bitrate control and adaptive rate-dependent reconstruction.
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
