---
title: "Highly-Parallel Atom-Detection Accelerator for Tweezer-Based Neutral Atom Quantum Computers"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2604.00816"
published: "2026-04-02"
fetched: "2026-04-03T07:15:13.137322"
---

Quantum Physics
[Submitted on 1 Apr 2026]
Title:Highly-Parallel Atom-Detection Accelerator for Tweezer-Based Neutral Atom Quantum Computers
View PDF HTML (experimental)Abstract:Neutral atom quantum computers (NAQCs) are among the most promising computational platforms for quantum computing. Controlling and measuring individual atoms and their states, which often requires multiple imaging and image-analysis procedures, is typically the most time-consuming task during computation and contributes significantly to overall cycle times. To resolve this challenge, we propose a highly-parallel atom-detection accelerator for tweezer-based NAQCs. Our design builds on an existing state-reconstruction method and combines an algorithm-level optimization with a Field Programmable Gate Array (FPGA) implementation to maximize parallelism and reduce the run time of the image-analysis process. We identify and overcome several challenges for an FPGA implementation, such as introducing a prefetching mechanism to improve scalability and customizing bus transfers to support large bandwidths. Tested on a Xilinx UltraScale+ FPGA, our design can analyze a 256x256-pixel fluorescence image in just 115mus, achieving 34.9x and 6.3x speedups over the original and optimized CPU baseline, respectively. Moreover, our accelerator can maintain consistent resource utilization across various atom array sizes, contributing to the ongoing efforts toward scalable and fully integrated FPGA-based control systems for NAQCs.
Current browse context:
quant-ph
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
