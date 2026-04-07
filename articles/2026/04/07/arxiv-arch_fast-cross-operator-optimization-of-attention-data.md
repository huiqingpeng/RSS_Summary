---
title: "Fast Cross-Operator Optimization of Attention Dataflow"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2604.03446"
published: "2026-04-07"
fetched: "2026-04-08T07:02:17.663656"
---

Computer Science > Hardware Architecture
[Submitted on 3 Apr 2026]
Title:Fast Cross-Operator Optimization of Attention Dataflow
View PDF HTML (experimental)Abstract:Attention is a fundamental computational kernel that accounts for the majority of the workload in transformer and LLM computing. Optimizing dataflow is crucial for enhancing both performance and energy efficiency in attention computation. This optimization involves a range of decisions, such as tiling, computation ordering and buffer management, and can be applied at both intra-operator and inter-operator levels, resulting in a highly complex decision space. We propose a new approach to cross-operator dataflow optimization. Its centerpiece is an analytical performance model that spans a large decision space and enables matrix-based encoding of multiple candidate solutions. Built on this foundation, a vast number of solutions can be evaluated rapidly, and with the aid of an effective pruning technique, the optimal solution can be identified through exhaustive enumeration. We refer to our method as MMEE (Matrix Multiplication Encoded Enumeration). The ability to efficiently enumerate a large design space allows MMEE to deliver higher-quality solutions at a substantially faster speed compared to prior approaches. The MMEE approach is evaluated across various test cases for different accelerator configurations. For energy-driven optimization, MMEE reduces energy consumption by 48%-50% and latency by 31%-69%, compared to state-of-the-art methods. For latency-driven optimization, MMEE achieves simultaneous reductions of 40%-50% in energy consumption and 40%-69% in latency, respectively. Additionally, MMEE is $64\times$ to $343\times$ faster than previous works.
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
