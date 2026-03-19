---
title: "AdaRadar: Rate Adaptive Spectral Compression for Radar-based Perception"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17979"
published: "2026-03-19"
fetched: "2026-03-19T16:19:47.605163"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:AdaRadar: Rate Adaptive Spectral Compression for Radar-based Perception
View PDF HTML (experimental)Abstract:Radar is a critical perception modality in autonomous driving systems due to its all-weather characteristics and ability to measure range and Doppler velocity. However, the sheer volume of high-dimensional raw radar data saturates the communication link to the computing engine (e.g., an NPU), which is often a low-bandwidth interface with data rate provisioned only for a few low-resolution range-Doppler frames. A generalized codec for utilizing high-dimensional radar data is notably absent, while existing image-domain approaches are unsuitable, as they typically operate at fixed compression ratios and fail to adapt to varying or adversarial conditions. In light of this, we propose radar data compression with adaptive feedback. It dynamically adjusts the compression ratio by performing gradient descent from the proxy gradient of detection confidence with respect to the compression rate. We employ a zeroth-order gradient approximation as it enables gradient computation even with non-differentiable core operations--pruning and quantization. This also avoids transmitting the gradient tensors over the band-limited link, which, if estimated, would be as large as the original radar data. In addition, we have found that radar feature maps are heavily concentrated on a few frequency components. Thus, we apply the discrete cosine transform to the radar data cubes and selectively prune out the coefficients effectively. We preserve the dynamic range of each radar patch through scaled quantization. Combining those techniques, our proposed online adaptive compression scheme achieves over 100x feature size reduction at minimal performance drop (~1%p). We validate our results on the RADIal, CARRADA, and Radatron datasets.
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
