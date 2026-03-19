---
title: "Enabling RISC-V Vector Code Generation in MLIR through Custom xDSL Lowerings"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.17800"
published: "2026-03-19"
fetched: "2026-03-19T12:03:24.512226"
---

Computer Science > Hardware Architecture
[Submitted on 18 Mar 2026]
Title:Enabling RISC-V Vector Code Generation in MLIR through Custom xDSL Lowerings
View PDF HTML (experimental)Abstract:The growing adoption of RISC-V in high-performance and scientific computing has increased the need for performance-portable code targeting the RISC-V Vector (RVV) extension. However, current compiler infrastructures provide limited end-to-end support for generating optimized RVV code from high-level representations to low-level implementations. In particular, existing MLIR distributions lack practical lowering paths that map high-level abstractions to RVV intrinsics, limiting their applicability for production-ready RISC-V kernels. This paper presents a compilation approach that combines MLIR with xDSL to bridge the missing lowering stages required for RVV code generation. Using custom intermediate representations and transformation passes implemented in xDSL, we systematically translate high-level operations into specialized, hardware-aware C code invoking RVV intrinsics. The resulting kernels are emitted as portable C functions that can be directly integrated into existing applications, enabling incremental adoption without modifying surrounding software stacks. We demonstrate the approach on the General Matrix Multiplication (GEMM) kernel and evaluate the generated micro-kernels on two real RISC-V platforms, the K230 and the BananaPi F3, comparing against OpenBLAS for both square-matrix benchmarks and transformer-based workloads derived from the BERT-Large model. When integrated into a matrix multiplication kernel, the proposed approach consistently outperforms OpenBLAS, reaching up to 12.2 GFLOPS compared to the baseline's 5.1 GFLOPS and providing performance improvements between 10--35\% across the evaluated workloads. These results demonstrate that combining MLIR with xDSL provides a practical pathway to portable, optimized code generation for RISC-V platforms.
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
