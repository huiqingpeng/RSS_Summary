---
title: "Characterizing WebGPU Dispatch Overhead for LLM Inference Across Four GPU Vendors, Three Backends, and Three Browsers"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.02344"
published: "2026-04-07"
fetched: "2026-04-08T07:02:32.935942"
---

Computer Science > Machine Learning
[Submitted on 9 Feb 2026]
Title:Characterizing WebGPU Dispatch Overhead for LLM Inference Across Four GPU Vendors, Three Backends, and Three Browsers
View PDF HTML (experimental)Abstract:WebGPU's security-focused design imposes per-operation validation that compounds across the many small dispatches in neural network inference, yet the true cost of this overhead is poorly characterized. We present a systematic characterization of WebGPU dispatch overhead for LLM inference at batch size 1, spanning four GPU vendors (NVIDIA, AMD, Apple, Intel), two native implementations (Dawn, wgpu-native) and three browsers (Chrome, Safari, Firefox), and two model sizes (Qwen2.5-0.5B and 1.5B). Our primary contribution is a sequential-dispatch methodology that reveals naive single-operation benchmarks overestimate dispatch cost by ${\sim}20\times$. The true per-dispatch cost of WebGPU API overhead alone is 24-36 $\mu$s on Vulkan and 32-71 $\mu$s on Metal, while the total per-operation overhead including Python cost is ${\sim}95$~$\mu$s, which turns out to be a distinction critical for optimization. On Vulkan, kernel fusion improves throughput by 53%, while CUDA fusion provides no benefit, confirming that per-operation overhead is a primary differentiator. LLM inference was tested across three major operating systems (Linux, Windows, macOS). We built $\texttt{torch-webgpu}$, a PrivateUse1-based out-of-tree PyTorch backend and an FX-to-WebGPU compiler, which on our reference platform achieves 11--12% of CUDA performance. At dtype-matched float32, RTX PRO 2000 achieves 1.4$\times$ WebGPU's throughput despite ${\sim}6\times$ less compute than RTX 5090. For dispatch overhead, backend choice is the dominant factor, although implementation choice also matters substantially within a backend (2.2$\times$ for Metal). In terms of dispatch vs kernel compute efficiency, we conclude that at batch=1 with the current dispatch-heavy pipeline, per-operation overhead dominates regardless of kernel quality. All code, benchmarks, and raw data are open source.
Current browse context:
cs.LG
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
IArxiv Recommender
(What is IArxiv?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
