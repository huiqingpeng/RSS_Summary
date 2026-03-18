---
title: "NeuroSim V1.5: Improved Software Backbone for Benchmarking Compute-in-Memory Accelerators with Device and Circuit-level Non-idealities"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2505.02314"
published: "2026-03-18"
fetched: "2026-03-18T15:31:56.520820"
---

Computer Science > Hardware Architecture
[Submitted on 5 May 2025 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:NeuroSim V1.5: Improved Software Backbone for Benchmarking Compute-in-Memory Accelerators with Device and Circuit-level Non-idealities
View PDF HTML (experimental)Abstract:The exponential growth of artificial intelligence (AI) applications has exposed the inefficiency of conventional von Neumann architectures, where frequent data transfers between compute units and memory create significant energy and latency bottlenecks. Analog Computing-in-Memory (ACIM) addresses this challenge by performing multiply-accumulate (MAC) operations directly in the memory arrays, substantially reducing data movement. However, designing robust ACIM accelerators requires accurate modeling of device- and circuit-level non-idealities. In this work, we present NeuroSim V1.5, introducing several key advances: (1) seamless integration with TensorRT's post-training quantization flow enabling support for more neural networks including transformers, (2) a flexible noise injection methodology built on pre-characterized statistical models, making it straightforward to incorporate data from SPICE simulations or silicon measurements, (3) expanded device support including emerging non-volatile capacitive memories, and (4) up to 6.5x faster runtime than NeuroSim V1.4 through optimized behavioral simulation. The combination of these capabilities uniquely enables systematic design space exploration across both accuracy and hardware efficiency metrics. Through multiple case studies, we demonstrate optimization of critical design parameters while maintaining network accuracy. By bridging high-fidelity noise modeling with efficient simulation, NeuroSim V1.5 advances the design and validation of next-generation ACIM accelerators. All NeuroSim versions are available open-source at this https URL.
Submission history
From: James Read [view email][v1] Mon, 5 May 2025 02:07:04 UTC (5,066 KB)
[v2] Tue, 17 Mar 2026 15:17:58 UTC (6,528 KB)
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
