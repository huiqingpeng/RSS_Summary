---
title: "Perceptio: Perception Enhanced Vision Language Models via Spatial Token Generation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18795"
published: "2026-03-20"
fetched: "2026-03-20T15:16:28.180346"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 19 Mar 2026]
Title:Perceptio: Perception Enhanced Vision Language Models via Spatial Token Generation
View PDF HTML (experimental)Abstract:Large Vision Language Models (LVLMs) excel at semantic understanding but struggle with fine grained spatial grounding, as the model must implicitly infer complex geometry without ever producing a spatial interpretation. We present Perceptio, a perception enhanced LVLM with 2D and 3D spatial reasoning abilities, enabled via explicit semantic segmentation tokens and depth tokens generated directly within the autoregressive sequence. Concretely, we (i) distill a VQVAE depth codebook from a strong monocular teacher to tokenize dense depth into compact sequences, and (ii) integrate SAM2 based semantic segmentation tokens and VQ-VAE depth tokens inside the LLM so the model first emits spatial tokens and then answers. To stabilize depth token generation, we introduce novel composite depth-token objectives (marker, token, and count losses) and a soft-merging technique for differentiable reconstruction. We adopt a multi-task co-training strategy across diverse datasets, letting the model learn perception tokens to tackle multiple downstream tasks. Building on InternVL, Perceptio achieves state-of-the-art performance across benchmarks: improving referring expression segmentation by +0.8/+1.4/+1.1 cIoU on RefCOCO/+/g HardBLINK spatial understanding accuracy by 10.3%, and MMBench accuracy by 1.0%, demonstrating that explicit spatial chain-of-thought materially strengthens spatial grounding in LVLMs.
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
