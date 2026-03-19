---
title: "FrescoDiffusion: 4K Image-to-Video with Prior-Regularized Tiled Diffusion"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17555"
published: "2026-03-19"
fetched: "2026-03-19T15:13:48.559894"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:FrescoDiffusion: 4K Image-to-Video with Prior-Regularized Tiled Diffusion
View PDF HTML (experimental)Abstract:Diffusion-based image-to-video (I2V) models are increasingly effective, yet they struggle to scale to ultra-high-resolution inputs (e.g., 4K). Generating videos at the model's native resolution often loses fine-grained structure, whereas high-resolution tiled denoising preserves local detail but breaks global layout consistency. This failure mode is particularly severe in the fresco animation setting: monumental artworks containing many distinct characters, objects, and semantically different sub-scenes that must remain spatially coherent over time. We introduce FrescoDiffusion, a training-free method for coherent large-format I2V generation from a single complex image. The key idea is to augment tiled denoising with a precomputed latent prior: we first generate a low-resolution video at the underlying model resolution and upsample its latent trajectory to obtain a global reference that captures long-range temporal and spatial structure. For 4K generation, we compute per-tile noise predictions and fuse them with this reference at every diffusion timestep by minimizing a single weighted least-squares objective in model-output space. The objective combines a standard tile-merging criterion with our regularization term, yielding a closed-form fusion update that strengthens global coherence while retaining fine detail. We additionally provide a spatial regularization variable that enables region-level control over where motion is allowed. Experiments on the VBench-I2V dataset and our proposed fresco I2V dataset show improved global consistency and fidelity over tiled baselines, while being computationally efficient. Our regularization enables explicit controllability of the trade-off between creativity and consistency.
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
