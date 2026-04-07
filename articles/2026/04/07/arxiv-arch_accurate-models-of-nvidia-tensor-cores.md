---
title: "Accurate Models of NVIDIA Tensor Cores"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2512.07004"
published: "2026-04-07"
fetched: "2026-04-08T07:02:28.540038"
---

Computer Science > Mathematical Software
[Submitted on 7 Dec 2025 (v1), last revised 4 Apr 2026 (this version, v3)]
Title:Accurate Models of NVIDIA Tensor Cores
View PDF HTML (experimental)Abstract:Matrix multiplication is a fundamental operation in both training of neural networks and inference. To accelerate matrix multiplication, Graphical Processing Units (GPUs) provide it implemented in hardware. Due to the increased throughput over the software-based matrix multiplication, the multipliers are increasingly used outside of AI, to accelerate various applications in scientific computing. However, matrix multipliers targeted at AI are at present not compliant with IEEE 754 floating-point arithmetic behaviour, with different vendors offering different numerical features. This leads to non-reproducible results across different generations of GPU architectures, at the matrix multiply-accumulate instruction level. To study numerical characteristics of matrix multipliers -- such as rounding behaviour, accumulator width, normalization points, extra carry bits, and others -- test vectors are typically constructed. Yet, these vectors may or may not distinguish between different hardware models, and due to limited hardware availability, their reliability across many different platforms remains largely untested. We present software models for emulating the inner product behaviour of low- and mixed-precision matrix multipliers in the V100, A100, H100 and B200 data center GPUs in most supported input formats of interest to mixed-precision algorithm developers: 8-, 16-, and 19-bit floating point.
Submission history
From: Mantas Mikaitis [view email][v1] Sun, 7 Dec 2025 21:13:18 UTC (162 KB)
[v2] Mon, 22 Dec 2025 10:08:25 UTC (167 KB)
[v3] Sat, 4 Apr 2026 12:44:59 UTC (243 KB)
Current browse context:
cs.MS
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
