---
title: "High-Fidelity Compression of Seismic Velocity Models via SIREN Auto-Decoders"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.14284"
published: "2026-03-18"
fetched: "2026-03-18T17:06:52.248702"
---

Computer Science > Machine Learning
[Submitted on 15 Mar 2026 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:High-Fidelity Compression of Seismic Velocity Models via SIREN Auto-Decoders
View PDF HTML (experimental)Abstract:Implicit Neural Representations (INRs) have emerged as a powerful paradigm for representing continuous signals independently of grid resolution. In this paper, we propose a high-fidelity neural compression framework based on a SIREN (Sinusoidal Representation Networks) auto-decoder to represent multi-structural seismic velocity models from the OpenFWI benchmark. Our method compresses each 70x70 velocity map (4,900 points) into a compact 256-dimensional latent vector, achieving a compression ratio of 19:1. We evaluate the framework on 1,000 samples across five diverse geological families: FlatVel, CurveVel, FlatFault, CurveFault, and Style. Experimental results demonstrate an average PSNR of 32.47 dB and SSIM of 0.956, indicating high-quality reconstruction. Furthermore, we showcase two key advantages of our implicit representation: (1) smooth latent space interpolation that generates plausible intermediate velocity structures, and (2) zero-shot super-resolution capability that reconstructs velocity fields at arbitrary resolutions up to 280x280 without additional training. The results highlight the potential of INR-based auto-decoders for efficient storage, multi-scale analysis, and downstream geophysical applications such as full waveform inversion.
Submission history
From: Xiaoxue Luo [view email][v1] Sun, 15 Mar 2026 08:43:39 UTC (3,294 KB)
[v2] Tue, 17 Mar 2026 13:22:14 UTC (3,116 KB)
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
