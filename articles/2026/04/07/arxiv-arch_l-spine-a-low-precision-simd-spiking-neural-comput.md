---
title: "L-SPINE: A Low-Precision SIMD Spiking Neural Compute Engine for Resource-efficient Edge Inference"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2604.03626"
published: "2026-04-07"
fetched: "2026-04-08T07:02:18.639019"
---

Computer Science > Hardware Architecture
[Submitted on 4 Apr 2026]
Title:L-SPINE: A Low-Precision SIMD Spiking Neural Compute Engine for Resource-efficient Edge Inference
View PDF HTML (experimental)Abstract:Spiking Neural Networks (SNNs) offer a promising solution for energy-efficient edge intelligence; however, their hardware deployment is constrained by memory overhead, inefficient scaling operations, and limited parallelism. This work proposes L-SPINE, a low-precision SIMD-enabled spiking neural compute engine for efficient edge inference. The architecture features a unified multi-precision datapath supporting 2-bit, 4-bit, and 8-bit operations, leveraging a multiplier-less shift-add model for neuron dynamics and synaptic accumulation. Implemented on an AMD VC707 FPGA, the proposed neuron requires only 459 LUTs and 408 FFs, achieving a critical delay of 0.39 ns and 4.2 mW power. At the system level, L-SPINE achieves 46.37K LUTs, 30.4K FFs, 2.38 ms latency, and 0.54 W power. Compared to CPU and GPU platforms, it reduces inference latency from seconds to milliseconds, achieving an up to three orders-of-magnitude improvement in energy efficiency. Quantisation analysis shows that INT2/INT4 configurations significantly reduce memory footprint with minimal accuracy loss. These results establish L-SPINE as a scalable and efficient solution for real-time edge SNN deployment.
Current browse context:
cs.AR
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
ScienceCast (What is ScienceCast?)
Demos
Recommenders and Search Tools
Influence Flower (What are Influence Flowers?)
CORE Recommender (What is CORE?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
