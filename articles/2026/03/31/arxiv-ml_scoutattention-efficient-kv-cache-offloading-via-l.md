---
title: "ScoutAttention: Efficient KV Cache Offloading via Layer-Ahead CPU Pre-computation for LLM Inference"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.27138"
published: "2026-03-31"
fetched: "2026-04-01T07:22:00.048700"
---

Computer Science > Machine Learning
[Submitted on 28 Mar 2026]
Title:ScoutAttention: Efficient KV Cache Offloading via Layer-Ahead CPU Pre-computation for LLM Inference
View PDF HTML (experimental)Abstract:Large language models encounter critical GPU memory capacity constraints during long-context inference, where KV cache memory consumption severely limits decode batch sizes. While existing research has explored offloading KV cache to DRAM, these approaches either demand frequent GPU-CPU data transfers or impose extensive CPU computation requirements, resulting in poor GPU utilization as the system waits for I/O operations or CPU processing to complete.
We propose ScoutAttention, a novel KV cache offloading framework that accelerates LLM inference through collaborative GPU-CPU attention computation. To prevent CPU computation from bottlenecking the system, ScoutAttention introduces GPU-CPU collaborative block-wise sparse attention that significantly reduces CPU load. Unlike conventional parallel computing approaches, our framework features a novel layer-ahead CPU pre-computation algorithm, enabling the CPU to initiate attention computation one layer in advance, complemented by asynchronous periodic recall mechanisms to maintain minimal CPU compute load. Experimental results demonstrate that ScoutAttention maintains accuracy within 2.4% of baseline while achieving 2.1x speedup compared to existing offloading methods.
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
IArxiv Recommender
(What is IArxiv?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
