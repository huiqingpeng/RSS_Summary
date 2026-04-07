---
title: "Direct Integer Division in RNS and its Hardware Solutions"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2604.04796"
published: "2026-04-07"
fetched: "2026-04-08T07:02:22.982900"
---

Computer Science > Hardware Architecture
[Submitted on 6 Apr 2026]
Title:Direct Integer Division in RNS and its Hardware Solutions
View PDFAbstract:Residue Number Systems (RNS) offer efficient modular arithmetic and natural parallelism, but direct integer division in RNS remains a difficult and comparatively underdeveloped operation. This paper builds on the type-II division algorithm of Szabo and Tanaka and reformulates it for more efficient hardware implementation. A principal contribution is the introduction of a power-based RNS, in which moduli are selected as powers of natural primes, increasing dynamic range, improving bit efficiency, and providing greater flexibility for scaling during division. The paper further formalizes three decomposition methods required by the division process: multi-factor scaling for modulus-based division, mixed-radix conversion for base extension and comparison, and a new divisor decomposition method introduced in this work. Each method is supported by mathematical development, including analysis of modulus invalidation during computation. These results simplify the hardware structure of the algorithm and improve its scalability. Supported by hardware diagrams and performance tables, the work advances both the theory and practical implementation of direct RNS division.
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
