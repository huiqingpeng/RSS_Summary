---
title: "TRINE: A Token-Aware, Runtime-Adaptive FPGA Inference Engine for Multimodal AI"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.22867"
published: "2026-03-25"
fetched: "2026-03-26T07:06:57.708610"
---

Computer Science > Hardware Architecture
[Submitted on 24 Mar 2026]
Title:TRINE: A Token-Aware, Runtime-Adaptive FPGA Inference Engine for Multimodal AI
View PDF HTML (experimental)Abstract:Multimodal stacks that mix ViTs, CNNs, GNNs, and transformer NLP strain embedded platforms because their compute/memory patterns diverge and hard real-time targets leave little slack. TRINE is a single-bitstream FPGA accelerator and compiler that executes end-to-end multimodal inference without reconfiguration. Layers are unified as DDMM/SDDMM/SpMM and mapped to a mode-switchable engine that toggles at runtime among weight/output-stationary systolic, 1xCS SIMD, and a routable adder tree (RADT) on a shared PE array. A width-matched, two-stage top-k unit enables in-stream token pruning, while dependency-aware layer offloading (DALO) overlaps independent kernels across reconfigurable processing units to sustain utilization. Evaluated on Alveo U50 and ZCU104, TRINE reduces latency by up to 22.57x vs. RTX 4090 and 6.86x vs. Jetson Orin Nano at 20-21 W; token pruning alone yields up to 7.8x on ViT-heavy pipelines, and DALO contributes up to 79% throughput improvement. With int8 quantization, accuracy drops remain <2.5% across representative tasks, delivering state-of-the-art latency and energy efficiency for unified vision, language, and graph workloads-in one bitstream.
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
