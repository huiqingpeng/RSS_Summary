---
title: "Loop Control Management in Tightly Coupled Processor Arrays (TCPAs)"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.28645"
published: "2026-03-31"
fetched: "2026-04-01T07:16:36.513910"
---

Computer Science > Hardware Architecture
[Submitted on 30 Mar 2026]
Title:Loop Control Management in Tightly Coupled Processor Arrays (TCPAs)
View PDF HTML (experimental)Abstract:Multidimensional loop kernels often suffer from control overhead that can dominate execution time on parallel loop accelerators. Tightly Coupled Processor Arrays (TCPAs) offload loop control to a global controller (GC), but existing approaches still require hundreds of control signals. We propose a method to derive and aggressively reduce these control conditions from a polyhedral representation of the iteration space, achieving reductions of 15x to 45x in control signals across several benchmarks. We introduce a lightweight GC architecture that evaluates conditions as unions of polyhedra using bounded evaluation units, requiring hardware comparable to a single processing element. Control signals are distributed throughout the array with a minimal number of delay elements resulting in zero-overhead loop control. Our evaluation on PolyBench kernels shows that the entire control flow requires < 10 % of the total array resources.
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
