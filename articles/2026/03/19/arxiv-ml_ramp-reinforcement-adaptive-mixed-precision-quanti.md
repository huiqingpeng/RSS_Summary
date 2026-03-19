---
title: "RAMP: Reinforcement Adaptive Mixed Precision Quantization for Efficient On Device LLM Inference"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17891"
published: "2026-03-19"
fetched: "2026-03-19T12:17:50.809809"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:RAMP: Reinforcement Adaptive Mixed Precision Quantization for Efficient On Device LLM Inference
View PDF HTML (experimental)Abstract:Post training quantization is essential for deploying large language models (LLMs) on resource constrained hardware, yet state of the art methods enforce uniform bit widths across layers, yielding suboptimal accuracy efficiency trade offs. We present RAMP (Reinforcement Adaptive Mixed Precision), an off policy Soft Actor Critic framework that learns per layer bit width assignments to minimize perplexity under a global bit budget. The policy conditions on an 11 dimensional embedding of activation statistics, weight properties, and structural descriptors, enabling zero shot transfer across model families and scales. To enable stable sub 4 bit quantization, we introduce Scale Folding, a preconditioning technique that migrates activation outliers into weights via per channel scaling and normalization layer compensation. A quality prioritized reward with asymmetric penalties and budget cliffs drives rapid convergence. On Llama 2 7B, RAMP achieves 5.54 perplexity at 3.68GB (3.65 effective bits), outperforming uniform 4 bit AWQ (5.60 at 3.90 GB) and GPTQ by 6% in size and 1% to3% in quality. Critically, a policy trained only on Llama 2 7B generalizes zero shot to Llama 2 13B and Mistral 7B, often surpassing target specific training, supporting the hypothesis that quantization sensitivity is primarily architectural. The HALO pipeline exports allocations to GGUF format for kernel free inference on CPUs, GPUs, and edge devices, retaining 99.5% of FP16 commonsense reasoning performance.
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
