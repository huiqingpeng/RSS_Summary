---
title: "SISA: A Scale-In Systolic Array for GEMM Acceleration"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.29913"
published: "2026-04-01"
fetched: "2026-04-02T07:11:16.557568"
---

Computer Science > Hardware Architecture
[Submitted on 31 Mar 2026]
Title:SISA: A Scale-In Systolic Array for GEMM Acceleration
View PDF HTML (experimental)Abstract:The currently dominant AI/ML workloads, such as Large Language Models (LLMs), rely on the efficient execution of General Matrix-Matrix Multiplication (GEMM) operations. Thus, most systems are equipped with dedicated matrix hardware accelerators based on square Systolic Arrays (SAs) of Processing Elements (PEs). While this organization was effective for traditional Deep Neural Networks (DNNs), LLMs introduce input-dependent and highly skewed matrices, leading to underutilized SA resources. To address this challenge, we propose SISA (Scale-In Systolic Array), a novel SA architecture that partitions the traditional square array into horizontal rectangular slabs. With minimal overhead, SISA exposes parallelism through independently scheduled slabs for efficient execution of small or skewed matrix shapes, while retaining full-array operation for large GEMMs. SISA achieves up to 8.52x speedup and 93% energy-delay-product (EDP) reduction for representative LLMs compared to a state-of-the-art monolithic SA with the same number of PEs.
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
