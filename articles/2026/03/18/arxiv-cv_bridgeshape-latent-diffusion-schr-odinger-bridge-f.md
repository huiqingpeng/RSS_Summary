---
title: "BridgeShape: Latent Diffusion Schr\"odinger Bridge for 3D Shape Completion"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2506.23205"
published: "2026-03-18"
fetched: "2026-03-18T18:26:16.294532"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 29 Jun 2025 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:BridgeShape: Latent Diffusion Schrödinger Bridge for 3D Shape Completion
View PDF HTML (experimental)Abstract:Existing diffusion-based 3D shape completion methods typically use a conditional paradigm, injecting incomplete shape information into the denoising network via deep feature interactions (e.g., concatenation, cross-attention) to guide sampling toward complete shapes, often represented by voxel-based distance functions. However, these approaches fail to explicitly model the optimal global transport path, leading to suboptimal completions. Moreover, performing diffusion directly in voxel space imposes resolution constraints, limiting the generation of fine-grained geometric details. To address these challenges, we propose BridgeShape, a novel framework for 3D shape completion via latent diffusion Schrödinger bridge. The key innovations lie in two aspects: (i) BridgeShape formulates shape completion as an optimal transport problem, explicitly modeling the transition between incomplete and complete shapes to ensure a globally coherent transformation. (ii) We introduce a Depth-Enhanced Vector Quantized Variational Autoencoder (VQ-VAE) to encode 3D shapes into a compact latent space, leveraging self-projected multi-view depth information enriched with strong DINOv2 features to enhance geometric structural perception. By operating in a compact yet structurally informative latent space, BridgeShape effectively mitigates resolution constraints and enables more efficient and high-fidelity 3D shape completion. BridgeShape achieves state-of-the-art performance on large-scale 3D shape completion benchmarks, demonstrating superior fidelity at higher resolutions and for unseen object classes.
Submission history
From: Dequan Kong [view email][v1] Sun, 29 Jun 2025 12:21:21 UTC (2,472 KB)
[v2] Tue, 17 Mar 2026 10:12:34 UTC (2,574 KB)
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
