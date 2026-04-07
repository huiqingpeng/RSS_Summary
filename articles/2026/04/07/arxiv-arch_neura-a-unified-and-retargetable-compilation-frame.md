---
title: "NEURA: A Unified and Retargetable Compilation Framework for Coarse-Grained Reconfigurable Architectures"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2604.04236"
published: "2026-04-07"
fetched: "2026-04-08T07:02:24.542381"
---

Computer Science > Programming Languages
[Submitted on 5 Apr 2026]
Title:NEURA: A Unified and Retargetable Compilation Framework for Coarse-Grained Reconfigurable Architectures
View PDF HTML (experimental)Abstract:Coarse-Grained Reconfigurable Architectures (CGRAs) are a promising and versatile accelerator platform, offering a balance between the performance and efficiency of specialized accelerators and the software programmability. However, their full potential is severely hindered by control flow in accelerated kernels, as the control flow (e.g., loops, branches) is fundamentally incompatible with the parallel, data-driven CGRA fabric. Prior strategies to resolve this mismatch in CGRA kernel acceleration are either inefficient, sacrificing performance for generality, or lack generality due to the difficulty of adapting them across different execution models. Thus, a general and unified solution for efficient CGRA kernel acceleration remains elusive.
This paper introduces NEURA, a unified and retargetable compilation framework that systematically resolves the control-dataflow mismatch in CGRAs. NEURA's core innovation is a novel, pure dataflow intermediate representation (IR) built on a predicated type system. In this IR, control contexts are embedded as a predicate within each data, making control an intrinsic property of data. This mechanism enables NEURA to systematically flatten complex control flow into a single unified dataflow graph. This unified representation decouples kernel representation from hardware, empowering NEURA to retarget diverse CGRAs with different execution models and microarchitectural features. When targeted to a high-performance spatio-temporal CGRA, NEURA delivers a 2.20x speedup on kernel benchmarks and up to 2.71x geometric mean speedup on real-world applications over state-of-the-art (SOTA) high-performance baselines. It also provides a competitive solution against the SOTA low-power CGRA when retargeted to a spatial-only CGRA. NEURA is open-source and available at this https URL.
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
