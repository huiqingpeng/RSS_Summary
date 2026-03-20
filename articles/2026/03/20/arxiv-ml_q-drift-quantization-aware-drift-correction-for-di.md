---
title: "Q-Drift: Quantization-Aware Drift Correction for Diffusion Model Sampling"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18095"
published: "2026-03-20"
fetched: "2026-03-20T13:08:28.428382"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:Q-Drift: Quantization-Aware Drift Correction for Diffusion Model Sampling
View PDF HTML (experimental)Abstract:Post-training quantization (PTQ) is a practical path to deploy large diffusion models, but quantization noise can accumulate over the denoising trajectory and degrade generation quality. We propose Q-Drift, a principled sampler-side correction that treats quantization error as an implicit stochastic perturbation on each denoising step and derives a marginal-distribution-preserving drift adjustment. Q-Drift estimates a timestep-wise variance statistic from calibration, in practice requiring as few as 5 paired full-precision/quantized calibration runs. The resulting sampler correction is plug-and-play with common samplers, diffusion models, and PTQ methods, while incurring negligible overhead at inference. Across six diverse text-to-image models (spanning DiT and U-Net), three samplers (Euler, flow-matching, DPM-Solver++), and two PTQ methods (SVDQuant, MixDQ), Q-Drift improves FID over the corresponding quantized baseline in most settings, with up to 4.59 FID reduction on PixArt-Sigma (SVDQuant W3A4), while preserving CLIP scores.
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
