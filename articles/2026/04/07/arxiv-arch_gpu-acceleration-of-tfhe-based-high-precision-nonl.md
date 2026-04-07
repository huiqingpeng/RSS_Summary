---
title: "GPU Acceleration of TFHE-Based High-Precision Nonlinear Layers for Encrypted LLM Inference"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2604.04783"
published: "2026-04-07"
fetched: "2026-04-08T07:02:25.448241"
---

Computer Science > Cryptography and Security
[Submitted on 6 Apr 2026]
Title:GPU Acceleration of TFHE-Based High-Precision Nonlinear Layers for Encrypted LLM Inference
View PDF HTML (experimental)Abstract:Deploying large language models (LLMs) as cloud services raises privacy concerns as inference may leak sensitive data. Fully Homomorphic Encryption (FHE) allows computation on encrypted data, but current FHE methods struggle with efficient and precise nonlinear function evaluation. Specifically, CKKS-based approaches require high-degree polynomial approximations, which are costly when target precision increases. Alternatively, TFHE's Programmable Bootstrapping (PBS) outperforms CKKS by offering exact lookup-table evaluation. But it lacks high-precision implementations of LLM nonlinear layers and underutilizes GPU resources.
We propose \emph{TIGER}, the first GPU-accelerated framework for high-precision TFHE-based nonlinear LLM layer evaluation. TIGER offers: (1) GPU-optimized WoP-PBS method combined with numerical algorithms to surpass native lookup-table precision limits on nonlinear functions; (2) high-precision and efficient implementations of key nonlinear layers, enabling practical encrypted inference; (3) batch-driven design exploiting inter-input parallelism to boost GPU efficiency. TIGER achieves 7.17$\times$, 16.68$\times$, and 17.05$\times$ speedups over a CPU baseline for GELU, Softmax, and LayerNorm, respectively.
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
