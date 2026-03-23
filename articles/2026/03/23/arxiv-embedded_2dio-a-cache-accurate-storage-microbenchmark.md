---
title: "2DIO: A Cache-Accurate Storage Microbenchmark"
source: "arXiv Embedded Systems"
url: "https://arxiv.org/abs/2603.19971"
published: "2026-03-23"
fetched: "2026-03-24T07:13:42.277250"
---

Computer Science > Operating Systems
[Submitted on 20 Mar 2026]
Title:2DIO: A Cache-Accurate Storage Microbenchmark
View PDF HTML (experimental)Abstract:We introduce 2DIO, a microbenchmark creating cache-accurate, stressful I/O traces. While existing tools are limited to generating traces with well-behaved, concave hit ratio curves, 2DIO produces ones with tunable complex cache behaviors, particularly performance cliffs and plateaus.
Our framework encodes a workload as a compact parameter triplet, capturing both short-term recency and long-term frequency. This parsimonious parameterization allows researchers to easily translate individual adjustments into predictable cache effects across various eviction policies, and enables the parameter space to be "swept" for exhaustive exploration of desired cache behavior, or to mimic real traces by calibrating parameters to match observed behaviors.
The tuned parameters are portable, meaning if the scale of the system under evaluation changes, so too will the footprint and length of the trace, while the relative cache behaviors are preserved.
Evaluations demonstrate 2DIO's ability to generate traces across a continuum of "what-if" cache behaviors and to reproduce real-world ones with high accuracy.
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
