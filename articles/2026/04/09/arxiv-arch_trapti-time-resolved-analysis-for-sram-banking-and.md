---
title: "TRAPTI: Time-Resolved Analysis for SRAM Banking and Power Gating Optimization in Embedded Transformer Inference"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2604.06955"
published: "2026-04-09"
fetched: "2026-04-10T07:04:51.568230"
---

Computer Science > Hardware Architecture
[Submitted on 8 Apr 2026]
Title:TRAPTI: Time-Resolved Analysis for SRAM Banking and Power Gating Optimization in Embedded Transformer Inference
View PDF HTML (experimental)Abstract:Transformer neural networks achieve state-of-the-art accuracy across language and vision tasks, but their deployment on embedded hardware is hindered by stringent area, latency, and energy constraints. During inference, performance and efficiency are increasingly dominated by the Key--Value (KV) cache, whose memory footprint grows with sequence length, straining on-chip memory utilization. Although existing mechanisms such as Grouped-Query Attention (GQA) reduce KV cache requirements compared to Multi-Head Attention (MHA), effectively exploiting this reduction requires understanding how on-chip memory demand evolves over time. This work presents TRAPTI, a two-stage methodology that combines cycle-level inference simulation with time-resolved analysis of on-chip memory occupancy to guide design decisions. In the first stage, the framework obtains memory occupancy traces and memory access statistics from simulation. In the second stage, the framework leverages the traces to explore banked memory organizations and power-gating configurations in an offline optimization flow. We apply this methodology to GPT-2 XL and DeepSeek-R1-Distill-Qwen-1.5B under the same accelerator configuration, enabling a direct comparison of MHA and GQA memory profiles. The analysis shows that DeepSeek-R1-Distill-Qwen-1.5B exhibits a 2.72x reduction in peak on-chip memory utilization in this setting compared to GPT-2 XL, unlocking further opportunities for power-gating optimization.
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
