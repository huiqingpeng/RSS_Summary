---
title: "AP-DRL: A Synergistic Algorithm-Hardware Framework for Automatic Task Partitioning of Deep Reinforcement Learning on Versal ACAP"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.29369"
published: "2026-04-01"
fetched: "2026-04-02T07:10:47.721022"
---

Computer Science > Hardware Architecture
[Submitted on 31 Mar 2026]
Title:AP-DRL: A Synergistic Algorithm-Hardware Framework for Automatic Task Partitioning of Deep Reinforcement Learning on Versal ACAP
View PDF HTML (experimental)Abstract:Deep reinforcement learning has demonstrated remarkable success across various domains. However, the tight coupling between training and inference processes makes accelerating DRL training an essential challenge for DRL optimization. Two key issues hinder efficient DRL training: (1) the significant variation in computational intensity across different DRL algorithms and even among operations within the same algorithm complicates hardware platform selection, while (2) DRL's wide dynamic range could lead to substantial reward errors with conventional FP16+FP32 mixed-precision quantization. While existing work has primarily focused on accelerating DRL for specific computing units or optimizing inference-stage quantization, we propose AP-DRL to address the above challenges.
AP-DRL is an automatic task partitioning framework that harnesses the heterogeneous architecture of AMD Versal ACAP (integrating CPUs, FPGAs, and AI Engines) to accelerate DRL training through intelligent hardware-aware optimization. Our approach begins with bottleneck analysis of CPU, FPGA, and AIE performance across diverse DRL workloads, informing the design principles for AP-DRL's inter-component task partitioning and quantization optimization. The framework then addresses the challenge of platform selection through design space exploration-based profiling and ILP-based partitioning models that match operations to optimal computing units based on their computational characteristics. For the quantization challenge, AP-DRL employs a hardware-aware algorithm coordinating FP32 (CPU), FP16 (FPGA/DSP), and BF16 (AI Engine) operations by leveraging Versal ACAP's native support for these precision formats. Comprehensive experiments indicate that AP-DRL can achieve speedup of up to 4.17$\times$ over programmable logic and up to 3.82$\times$ over AI Engine baselines while maintaining training convergence.
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
