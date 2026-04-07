---
title: "GEMM-GS: Accelerating 3D Gaussian Splatting on Tensor Cores with GEMM-Compatible Blending"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2604.02120"
published: "2026-04-07"
fetched: "2026-04-08T07:02:28.024569"
---

Computer Science > Hardware Architecture
[Submitted on 2 Apr 2026 (v1), last revised 6 Apr 2026 (this version, v2)]
Title:GEMM-GS: Accelerating 3D Gaussian Splatting on Tensor Cores with GEMM-Compatible Blending
View PDF HTML (experimental)Abstract:Neural Radiance Fields (NeRF) enables 3D scene reconstruction from several 2D images but incurs high rendering latency via its point-sampling design. 3D Gaussian Splatting (3DGS) improves on NeRF with explicit scene representation and an optimized pipeline yet still fails to meet practical real-time demands. Existing acceleration works overlook the evolving Tensor Cores of modern GPUs because 3DGS pipeline lacks General Matrix Multiplication (GEMM) operations. This paper proposes GEMM-GS, an acceleration approach utilizing tensor cores on GPUs via GEMM-friendly blending transformation. It equivalently reformulates the 3DGS blending process into a GEMM-compatible form to utilize Tensor Cores. A high-performance CUDA kernel is designed, integrating a three-stage double-buffered pipeline that overlaps computation and memory access. Extensive experiments show that GEMM-GS achieves $1.42\times$ speedup over vanilla 3DGS and provides an additional $1.47\times$ speedup on average when combining with existing acceleration approaches. Code is released at this https URL.
Submission history
From: Haomin Li [view email][v1] Thu, 2 Apr 2026 14:56:06 UTC (3,986 KB)
[v2] Mon, 6 Apr 2026 06:53:41 UTC (3,986 KB)
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
