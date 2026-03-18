---
title: "Spectral Property-Driven Data Augmentation for Hyperspectral Single-Source Domain Generalization"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16662"
published: "2026-03-18"
fetched: "2026-03-18T18:17:03.615457"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:Spectral Property-Driven Data Augmentation for Hyperspectral Single-Source Domain Generalization
View PDF HTML (experimental)Abstract:While hyperspectral images (HSI) benefit from numerous spectral channels that provide rich information for classification, the increased dimensionality and sensor variability make them more sensitive to distributional discrepancies across domains, which in turn can affect classification performance. To tackle this issue, hyperspectral single-source domain generalization (SDG) typically employs data augmentation to simulate potential domain shifts and enhance model robustness under the condition of single-source domain training data availability. However, blind augmentation may produce samples misaligned with real-world scenarios, while excessive emphasis on realism can suppress diversity, highlighting a tradeoff between realism and diversity that limits generalization to target domains. To address this challenge, we propose a spectral property-driven data augmentation (SPDDA) that explicitly accounts for the inherent properties of HSI, namely the device-dependent variation in the number of spectral channels and the mixing of adjacent channels. Specifically, SPDDA employs a spectral diversity module that resamples data from the source domain along the spectral dimension to generate samples with varying spectral channels, and constructs a channel-wise adaptive spectral mixer by modeling inter-channel similarity, thereby avoiding fixed augmentation patterns. To further enhance the realism of the augmented samples, we propose a spatial-spectral co-optimization mechanism, which jointly optimizes a spatial fidelity constraint and a spectral continuity self-constraint. Moreover, the weight of the spectral self-constraint is adaptively adjusted based on the spatial counterpart, thus preventing over-smoothing in the spectral dimension and preserving spatial structure. Extensive experiments conducted on three remote sensing benchmarks demonstrate that SPDDA outperforms state-of-the-art methods.
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
