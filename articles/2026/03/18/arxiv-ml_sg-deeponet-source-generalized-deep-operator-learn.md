---
title: "SG-DeepONet: Source-generalized deep operator learning for full waveform inversion"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2408.08005"
published: "2026-03-18"
fetched: "2026-03-18T16:16:21.836444"
---

Computer Science > Machine Learning
[Submitted on 15 Aug 2024 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:SG-DeepONet: Source-generalized deep operator learning for full waveform inversion
View PDF HTML (experimental)Abstract:Full waveform inversion (FWI) aims to reconstruct subsurface velocity models from observed seismic wavefields and has recently benefited from advances in deep learning (DL). The performance of DL-based FWI critically depends on the diversity of training data, yet existing datasets such as OpenFWI rely on fixed or weakly varying source conditions, limiting their ability to represent realistic seismic scenarios and hindering source generalization. To address this issue, we construct a new source-variable seismic dataset, termed SVFWI, by systematically varying the frequencies and horizontal locations of multiple surface sources. SVFWI is further divided into three subsets that respectively model frequency variations, location variations, and their combined effects, providing a challenging benchmark in data-driven FWI. We further propose SG-DeepONet, a novel DeepONet-based encoder-decoder framework tailored for FWI. The branch network extracts multi-scale time-frequency features from seismic observations, the trunk network explicitly embeds source physical parameters, and an interactive decoding network enables effective nonlinear fusion and high-fidelity velocity reconstruction. Extensive experiments on SVFWI demonstrate that SG-DeepONet achieves superior inversion accuracy and robustness under varying source conditions compared with existing DL-based FWI methods.
Submission history
From: Ze-Kai Guo [view email][v1] Thu, 15 Aug 2024 08:15:06 UTC (1,568 KB)
[v2] Tue, 17 Mar 2026 08:35:41 UTC (628 KB)
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
IArxiv Recommender
(What is IArxiv?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
