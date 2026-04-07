---
title: "A reconfigurable smart camera implementation for jet flames characterization based on an optimized segmentation model"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2604.03267"
published: "2026-04-07"
fetched: "2026-04-08T07:02:39.908257"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 19 Mar 2026]
Title:A reconfigurable smart camera implementation for jet flames characterization based on an optimized segmentation model
View PDF HTML (experimental)Abstract:In this work we present a novel framework for fire safety management in industrial settings through the implementation of a smart camera platform for jet flames characterization. The approach seeks to alleviate the lack of real-time solutions for industrial early fire segmentation and characterization. As a case study, we demonstrate how a SoC FPGA, running optimized Artificial Intelligence (AI) models can be leveraged to implement a full edge processing pipeline for jet flames analysis. In this paper we extend previous work on computer-vision jet fire segmentation by creating a novel experimental set-up and system implementation for addressing this issue, which can be replicated to other fire safety applications. The proposed platform is designed to carry out image processing tasks in real-time and on device, reducing video processing overheads, and thus the overall latency. This is achieved by optimizing a UNet segmentation model to make it amenable for an SoC FPGAs implementation; the optimized model can then be efficiently mapped onto the SoC reconfigurable logic for massively parallel execution. For our experiments, we have chosen the Ultra96 platform, as it also provides the means for implementing full-fledged intelligent systems using the SoC peripherals, as well as other Operating System (OS) capabilities (i.e., multi-threading) for systems management. For optimizing the model we made use of the Vitis (Xilinx) framework, which enabled us to optimize the full precision model from 7.5 million parameters to 59,095 parameters (125x less), which translated into a reduction of the processing latency of 2.9x. Further optimization (multi-threading and batch normalization) led to an improvement of 7.5x in terms of latency, yielding a performance of 30 Frames Per Second (FPS) without sacrificing accuracy in terms of the evaluated metrics (Dice Score).
Submission history
From: Gilberto Ochoa-Ruiz [view email][v1] Thu, 19 Mar 2026 22:17:55 UTC (5,359 KB)
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
