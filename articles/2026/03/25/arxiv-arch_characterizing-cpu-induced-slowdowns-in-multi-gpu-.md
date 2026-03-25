---
title: "Characterizing CPU-Induced Slowdowns in Multi-GPU LLM Inference"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.22774"
published: "2026-03-25"
fetched: "2026-03-26T07:06:08.711496"
---

Computer Science > Hardware Architecture
[Submitted on 24 Mar 2026]
Title:Characterizing CPU-Induced Slowdowns in Multi-GPU LLM Inference
View PDF HTML (experimental)Abstract:Large-scale machine learning workloads increasingly rely on multi-GPU systems, yet their performance is often limited by an overlooked component: the CPU. Through a detailed study of modern large language model (LLM) inference and serving workloads, we find that multi-GPU performance frequently degrades not because GPUs are saturated, but because CPUs fail to keep the GPUs busy. Under limited CPU allocations, systems exhibit symptoms such as delayed kernel launch, stalled communication, and increased tokenization latency, leading to severe GPU underutilization even when ample GPU resources are available. This work presents a systematic analysis of CPU-induced slowdowns in multi-GPU LLM inference. We show that these bottlenecks persist even in serving stacks that employ process-level separation and modern GPU-side optimizations such as CUDA Graphs. Since the marginal cost of additional CPU cores is small relative to GPU instance pricing, our evaluation indicates that increasing the number of CPU cores can substantially improve performance and stability at minimal additional cost. Under moderate serving load, we observe that CPU-starved configurations frequently time out, while providing adequate CPU resources restores responsiveness and reduces time-to-first-token (TTFT) latency by 1.36-5.40x across configurations, all without requiring additional GPUs. This work shows that CPU provisioning is a crucial factor in multi-GPU LLM inference configuration, helping prevent control-side bottlenecks.
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
