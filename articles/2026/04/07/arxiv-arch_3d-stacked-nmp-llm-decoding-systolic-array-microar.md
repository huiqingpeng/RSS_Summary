---
title: "3D-Stacked NMP, LLM Decoding, Systolic Array Microarchitecture, Multi-Core Scheduling"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2604.04253"
published: "2026-04-07"
fetched: "2026-04-08T07:02:19.599570"
---

Computer Science > Hardware Architecture
[Submitted on 5 Apr 2026]
Title:3D-Stacked NMP, LLM Decoding, Systolic Array Microarchitecture, Multi-Core Scheduling
View PDF HTML (experimental)Abstract:Large language model (LLM) decoding is a major inference bottleneck because its low arithmetic intensity makes performance highly sensitive to memory bandwidth. 3D-stacked near-memory processing (NMP) provides substantially higher local memory bandwidth than conventional off-chip interfaces, making it a promising substrate for decode acceleration. However, our analysis shows that this bandwidth advantage also shifts many decode operators on 3D-stacked NMP back into the compute-bound regime. Under the tight area budget of the logic die, the design of the compute substrate itself therefore becomes a first-order challenge.
Therefore, we rethink the compute microarchitecture of prior 3D-stacked NMP designs. First, we replace prior MAC tree-based compute units with a more area-efficient systolic array, and we further observe that decode operators exhibit substantial shape diversity, making reconfigurability in both systolic array shape and dataflow essential for sustaining high utilization. Building on this insight, we continue to exploit two key opportunities: the high local memory bandwidth reduces the need for large on-chip buffers, and the existing vector core, originally designed to handle auxiliary tensor computations, already provides much of the control logic and multi-ported buffering required for fine-grained flexibility for systolic array, allowing us to unify the two structures in a highly area-efficient manner. Based on these insights, we present the first compute microarchitecture tailored to 3D-stacked NMP LLM decoding, explicitly designed to satisfy the joint requirements of low area cost, high-bandwidth operation, and fine-grained reconfigurability.
We further propose an multi-core scheduling framework. Compared with Stratum, our design achieves an average 2.91x speedup and 2.40x higher energy efficiency across both dense and MoE models.
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
