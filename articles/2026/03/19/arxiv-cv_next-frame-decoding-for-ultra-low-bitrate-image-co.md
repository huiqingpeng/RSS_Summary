---
title: "Next-Frame Decoding for Ultra-Low-Bitrate Image Compression with Video Diffusion Priors"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.15129"
published: "2026-03-19"
fetched: "2026-03-19T17:04:50.894758"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 16 Mar 2026 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:Next-Frame Decoding for Ultra-Low-Bitrate Image Compression with Video Diffusion Priors
View PDF HTML (experimental)Abstract:We present a novel paradigm for ultra-low-bitrate image compression (ULB-IC) that exploits the "temporal" evolution in generative image compression. Specifically, we define an explicit intermediate state during decoding: a compact anchor frame, which preserves the scene geometry and semantic layout while discarding high-frequency details. We then reinterpret generative decoding as a virtual temporal transition from this anchor to the final reconstructed this http URL model this progression, we leverage a pretrained video diffusion model (VDM) as temporal priors: the anchor frame serves as the initial frame and the original image as the target frame, transforming the decoding process into a next-frame prediction this http URL contrast to image diffusion-based ULB-IC models, our decoding proceeds from a visible, semantically faithful anchor, which improves both fidelity and realism for perceptual image compression. Extensive experiments demonstrate that our method achieves superior objective and subjective performance. On the CLIC2020 test set, our method achieves over 50% bitrate savings across LPIPS, DISTS, FID, and KID compared to DiffC, while also delivering a significant decoding speedup of up to $\times$5. Code will be released later.
Submission history
From: Yunuo Chen [view email][v1] Mon, 16 Mar 2026 11:24:26 UTC (5,000 KB)
[v2] Wed, 18 Mar 2026 05:45:53 UTC (5,000 KB)
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
