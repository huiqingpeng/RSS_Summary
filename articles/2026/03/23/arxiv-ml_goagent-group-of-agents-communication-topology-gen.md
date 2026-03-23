---
title: "GoAgent: Group-of-Agents Communication Topology Generation for LLM-based Multi-Agent Systems"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19677"
published: "2026-03-23"
fetched: "2026-03-24T07:21:12.313494"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:GoAgent: Group-of-Agents Communication Topology Generation for LLM-based Multi-Agent Systems
View PDF HTML (experimental)Abstract:Large language model (LLM)-based multi-agent systems (MAS) have demonstrated exceptional capabilities in solving complex tasks, yet their effectiveness depends heavily on the underlying communication topology that coordinates agent interactions. Within these systems, successful problem-solving often necessitates task-specific group structures to divide and conquer subtasks. However, most existing approaches generate communication topologies in a node-centric manner, leaving group structures to emerge implicitly from local connectivity decisions rather than modeling them explicitly, often leading to suboptimal coordination and unnecessary communication overhead. To address this limitation, we propose GoAgent (Group-of-Agents), a communication topology generation method that explicitly treats collaborative groups as the atomic units of MAS construction. Specifically, GoAgent first enumerates task-relevant candidate groups through an LLM and then autoregressively selects and connects these groups as atomic units to construct the final communication graph, jointly capturing intra-group cohesion and inter-group coordination. To mitigate communication redundancy and noise propagation inherent in expanding topologies, we further introduce a conditional information bottleneck (CIB) objective that compresses inter-group communication, preserving task-relevant signals while filtering out redundant historical noise. Extensive experiments on six benchmarks demonstrate the state-of-the-art performance of GoAgent with 93.84% average accuracy while reducing token consumption by about 17%.
Current browse context:
cs.LG
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
IArxiv Recommender
(What is IArxiv?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
