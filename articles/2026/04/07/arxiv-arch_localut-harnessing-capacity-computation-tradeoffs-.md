---
title: "LOCALUT: Harnessing Capacity-Computation Tradeoffs for LUT-Based Inference in DRAM-PIM"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2604.04523"
published: "2026-04-07"
fetched: "2026-04-08T07:02:20.569733"
---

Computer Science > Hardware Architecture
[Submitted on 6 Apr 2026]
Title:LOCALUT: Harnessing Capacity-Computation Tradeoffs for LUT-Based Inference in DRAM-PIM
View PDF HTML (experimental)Abstract:Lookup tables (LUTs) have recently gained attention as an alternative compute mechanism that maps input operands to precomputed results, eliminating the need for arithmetic logic. LUTs not only reduce logic complexity, but also naturally support diverse numerical precisions without requiring separate circuits for each bitwidth-an increasingly important feature in quantized DNNs. This creates a favorable tradeoff in PIM: memory capacity can be used in place of logic to increase computational throughput, aligning well with DRAM-PIM architectures that offer high bandwidth and easily available memory but limited logic density. In this work, we explore this capacity-computation tradeoff in LUT-based PIM designs, where memory capacity is traded for performance by packing multiple MAC operations into a single LUT lookup. Building on this insight, we propose LOCALUT, a PIM-based design for efficient low-bit quantized DNN inference using operation-packed LUTs. First, we observe that these LUTs contain extensive redundancy and introduce LUT canonicalization, which eliminates duplicate entries to reduce LUT size. Second, we propose reordering LUT, a lightweight auxiliary LUT that remaps weight vectors to their canonical form required by LUT canonicalization with a simple LUT lookup. Third, we propose LUT slice streaming, a novel execution strategy that exploits the DRAM-buffer hierarchy by streaming only relevant LUT columns into the buffer and reusing them across multiple weight vectors. Evaluated on a real system based on UPMEM devices, we demonstrate a geometric mean speedup of 1.82x across various numeric precisions and DNN models. We believe LOCALUT opens a path toward scalable, low-logic PIM designs tailored for LUT-based DNN inference. Our implementation of LOCALUT is available at this https URL.
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
