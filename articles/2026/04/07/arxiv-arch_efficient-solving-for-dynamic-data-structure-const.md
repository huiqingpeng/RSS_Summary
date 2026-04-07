---
title: "Efficient Solving for Dynamic Data Structure Constraint Satisfaction Problem"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2604.03624"
published: "2026-04-07"
fetched: "2026-04-08T07:02:18.184960"
---

Computer Science > Hardware Architecture
[Submitted on 4 Apr 2026]
Title:Efficient Solving for Dynamic Data Structure Constraint Satisfaction Problem
View PDF HTML (experimental)Abstract:Functional verification plays a central role in ensuring the correctness of modern integrated circuit designs, where constrained-random verification is widely adopted to generate diverse stimuli under high-level constraints. In industrial verification environments, constraint solving increasingly involves dynamic data structures whose shape and content are determined at runtime, causing the sets of variables and constraint instances to evolve across solver invocations, which in turn leads to substantial overhead when nested and high-dimensional structures repeatedly expand across solves. We formalize this class of problems as the Dynamic Data Structure Constraint Satisfaction Problem (D2SCSP),which captures the interaction between dynamic data structure expansion and constraint evaluation. We propose a dependency-guided problem partitioning framework combined with an incremental encoding and constraint activation mechanism, enabling reuse of solver state and encodings across multiple solves. The framework is integrated into an industrial SystemVerilog verification flow and implemented in the commercial simulator VeriSim. Experimental results on industrial benchmarks demonstrate significant performance improvements, achieving an average speedup of 24.80x over a baseline and 1.72x over a state-of-the-art commercial simulator, highlighting the practicality of the approach for real-world verification workflows.
Current browse context:
cs.AR
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
