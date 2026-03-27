---
title: "Agent Factories for High Level Synthesis: How Far Can General-Purpose Coding Agents Go in Hardware Optimization?"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.25719"
published: "2026-03-27"
fetched: "2026-03-28T07:08:06.512011"
---

Computer Science > Artificial Intelligence
[Submitted on 26 Mar 2026]
Title:Agent Factories for High Level Synthesis: How Far Can General-Purpose Coding Agents Go in Hardware Optimization?
View PDF HTML (experimental)Abstract:We present an empirical study of how far general-purpose coding agents -- without hardware-specific training -- can optimize hardware designs from high-level algorithmic specifications. We introduce an agent factory, a two-stage pipeline that constructs and coordinates multiple autonomous optimization agents.
In Stage~1, the pipeline decomposes a design into sub-kernels, independently optimizes each using pragma and code-level transformations, and formulates an Integer Linear Program (ILP) to assemble globally promising configurations under an area constraint. In Stage~2, it launches $N$ expert agents over the top ILP solutions, each exploring cross-function optimizations such as pragma recombination, loop fusion, and memory restructuring that are not captured by sub-kernel decomposition.
We evaluate the approach on 12 kernels from HLS-Eval and Rodinia-HLS using Claude Code (Opus~4.5/4.6) with AMD Vitis HLS. Scaling from 1 to 10 agents yields a mean $8.27\times$ speedup over baseline, with larger gains on harder benchmarks: streamcluster exceeds $20\times$ and kmeans reaches approximately $10\times$. Across benchmarks, agents consistently rediscover known hardware optimization patterns without domain-specific training, and the best designs often do not originate from top-ranked ILP candidates, indicating that global optimization exposes improvements missed by sub-kernel search. These results establish agent scaling as a practical and effective axis for HLS optimization.
Submission history
From: Abhishek Bhandwaldar [view email][v1] Thu, 26 Mar 2026 17:57:50 UTC (786 KB)
Current browse context:
cs.AI
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
