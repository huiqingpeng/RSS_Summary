---
title: "YANA: Bridging the Neuromorphic Simulation-to-Hardware Gap"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2604.03432"
published: "2026-04-07"
fetched: "2026-04-08T07:02:23.501789"
---

Computer Science > Neural and Evolutionary Computing
[Submitted on 3 Apr 2026]
Title:YANA: Bridging the Neuromorphic Simulation-to-Hardware Gap
View PDF HTML (experimental)Abstract:Spiking Neural Networks (SNNs) promise significant advantages over conventional Artificial Neural Networks (ANNs) for applications requiring real-time processing of temporally sparse data streams under strict power constraints -- a concept known as the Neuromorphic Advantage. However, the limited availability of neuromorphic hardware creates a substantial simulation-to-hardware gap that impedes algorithmic innovation, hardware-software co-design, and the development of mature open-source ecosystems. To address this challenge, we introduce Yet Another Neuromorphic Accelerator (YANA), an FPGA-based digital SNN accelerator designed to bridge this gap by providing an accessible hardware and software framework for neuromorphic computing. YANA implements a five-stage, event-driven processing pipeline that fully exploits temporal and spatial sparsity while supporting arbitrary SNN topologies through point-to-point neuron connections. The architecture features an input preprocessing scheme that maintains steady event processing at one event per cycle without buffer overflow risks, and implements hardware-efficient event-driven neuron updates using lookup tables for leak calculations. We demonstrate YANA's sparsity exploitation capabilities through experiments on the Spiking Heidelberg Digits dataset, showing near-linear scaling of inference time with both spatial and temporal sparsity levels. Deployed on the accessible AMD Kria KR260 platform, a single YANA core utilizes 740 LUTs, 918 registers, 7 BRAMS and 24 URAMs, supporting up to $2^{17}$ synapses and $2^{10}$ neurons. We release the YANA framework as an open-source project, providing an end-to-end solution for training, optimizing, and deploying SNNs that integrates with existing neuromorphic computing tools through the Neuromorphic Intermediate Representation (NIR).
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
