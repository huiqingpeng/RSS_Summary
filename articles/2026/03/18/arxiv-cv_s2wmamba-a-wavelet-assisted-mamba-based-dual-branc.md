---
title: "S2WMamba: A Wavelet-Assisted Mamba-Based Dual-Branch Network For Pansharpening"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2512.06330"
published: "2026-03-18"
fetched: "2026-03-18T18:30:20.792237"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 6 Dec 2025 (v1), last revised 17 Mar 2026 (this version, v3)]
Title:S2WMamba: A Wavelet-Assisted Mamba-Based Dual-Branch Network For Pansharpening
View PDF HTML (experimental)Abstract:Pansharpening fuses a high-resolution panchromatic (PAN) image with a low-resolution multispectral (LRMS) image to produce a high-resolution multispectral (HRMS) image. A key difficulty is that jointly processing PAN and MS features often entangles spatial detail enhancement with spectral fidelity. To address this feature entanglement, we propose S2WMamba, a framework that explicitly disentangles modality-specific frequency information for highly controlled crossmodal interaction. Concretely, unlike global frequency transforms, a localized 2D Haar DWT is applied to the PAN image to precisely isolate spatial edges and textures. Concurrently, a novel channel-wise 1D Haar DWT treats each pixel's spectrum as a 1D signal, isolating the shared spectral base from band-specific variations to strictly limit spectral distortion. The resulting Spectral branch injects wavelet-extracted spatial details into MS features, while the Spatial branch refines PAN features using spectra from the DWT1D process. To overcome inadequate frequency fusion, the two branches exchange information via Mambabased cross-modulation, which explicitly models long-range dependencies across these decoupled sub-bands with linear complexity. On WV3, GF2, and QB datasets, S2WMamba matches or surpasses recent strong baselines (FusionMamba, CANNet, U2Net, PanNet), improving PSNR by up to 0.23 dB and reaching an HQNR of 0.956 on full-resolution WV3. Extensive ablations justify the modality-specific DWT placement and the parallel dual-branch architecture.
Submission history
From: Yugang Cao [view email][v1] Sat, 6 Dec 2025 07:15:12 UTC (6,489 KB)
[v2] Sun, 15 Feb 2026 12:41:01 UTC (6,489 KB)
[v3] Tue, 17 Mar 2026 10:39:09 UTC (3,121 KB)
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
