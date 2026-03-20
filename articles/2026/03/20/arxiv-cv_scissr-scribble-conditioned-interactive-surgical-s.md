---
title: "SCISSR: Scribble-Conditioned Interactive Surgical Segmentation and Refinement"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18544"
published: "2026-03-20"
fetched: "2026-03-20T16:08:23.917100"
---

Electrical Engineering and Systems Science > Image and Video Processing
[Submitted on 19 Mar 2026]
Title:SCISSR: Scribble-Conditioned Interactive Surgical Segmentation and Refinement
View PDF HTML (experimental)Abstract:Accurate segmentation of tissues and instruments in surgical scenes is annotation-intensive due to irregular shapes, thin structures, specularities, and frequent occlusions. While SAM models support point, box, and mask prompts, points are often too sparse and boxes too coarse to localize such challenging targets. We present SCISSR, a scribble-promptable framework for interactive surgical scene segmentation. It introduces a lightweight Scribble Encoder that converts freehand scribbles into dense prompt embeddings compatible with the mask decoder, enabling iterative refinement for a target object by drawing corrective strokes on error regions. Because all added modules (the Scribble Encoder, Spatial Gated Fusion, and LoRA adapters) interact with the backbone only through its standard embedding interfaces, the framework is not tied to a single model: we build on SAM 2 in this work, yet the same components transfer to other prompt-driven segmentation architectures such as SAM 3 without structural modification. To preserve pre-trained capabilities, we train only these lightweight additions while keeping the remaining backbone frozen. Experiments on EndoVis 2018 demonstrate strong in-domain performance, while evaluation on the out-of-distribution CholecSeg8k further confirms robustness across surgical domains. SCISSR achieves 95.41% Dice on EndoVis 2018 with five interaction rounds and 96.30% Dice on CholecSeg8k with three interaction rounds, outperforming iterative point prompting on both benchmarks.
Current browse context:
eess.IV
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
