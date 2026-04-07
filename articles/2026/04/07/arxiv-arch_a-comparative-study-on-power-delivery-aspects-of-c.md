---
title: "A comparative study on power delivery aspects of compute-in/near-memory approaches using DRAM"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2604.04773"
published: "2026-04-07"
fetched: "2026-04-08T07:02:22.464647"
---

Computer Science > Hardware Architecture
[Submitted on 6 Apr 2026]
Title:A comparative study on power delivery aspects of compute-in/near-memory approaches using DRAM
View PDFAbstract:Compute-in-memory (PIM) mitigates the memory wall by performing computation within memory, reducing data movement and improving energy efficiency. DRAM-based PIM is particularly attractive due to its high density, mature manufacturing ecosystem, and compatibility with existing systems. Recent works exploit multiple levels of the DRAM hierarchy - including subarrays, banks, and 3D-stacked organizations - to enable in-memory computation using mechanisms such as multi-row activation, row-buffer operations, and near-bank compute units. However, these approaches introduce non-traditional current demand patterns that challenge the power delivery network (PDN).
This paper surveys PDN challenges in DRAM-based PIM systems and proposes a unified taxonomy that characterizes PIM-induced current behavior along temporal (burst vs. sustained) and spatial (localized vs. distributed) dimensions. Using this framework, we analyze how representative PIM techniques stress the PDN through bursty activations, multi-row concurrency, and large-scale parallel execution, leading to voltage droop, IR drop, and thermal hotspots.
We further discuss DRAM-specific mitigation strategies leveraging existing architectural and circuit-level mechanisms, including timing constraints, memory controller scheduling, data placement, and bank- and vault-level power management. This survey highlights the importance of PDN-aware design for scalable and reliable DRAM-based PIM systems and outlines key future research directions.
Submission history
From: Siddhartha Raman Sundara Raman [view email][v1] Mon, 6 Apr 2026 15:44:40 UTC (98 KB)
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
