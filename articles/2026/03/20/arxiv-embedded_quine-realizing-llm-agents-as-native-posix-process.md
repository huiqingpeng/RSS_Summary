---
title: "Quine: Realizing LLM Agents as Native POSIX Processes"
source: "arXiv Embedded Systems"
url: "https://arxiv.org/abs/2603.18030"
published: "2026-03-20"
fetched: "2026-03-20T12:03:17.635627"
---

Computer Science > Operating Systems
[Submitted on 8 Mar 2026]
Title:Quine: Realizing LLM Agents as Native POSIX Processes
View PDF HTML (experimental)Abstract:Current LLM agent frameworks often implement isolation, scheduling, and communication at the application layer, even though these mechanisms are already provided by mature operating systems. Instead of introducing another application-layer orchestrator, this paper presents Quine, a runtime architecture and reference implementation that realizes LLM agents as native POSIX processes. The mapping is explicit: identity is PID, interface is standard streams and exit status, state is memory, environment variables, and filesystem, and lifecycle is fork/exec/exit. A single executable implements this model by recursively spawning fresh instances of itself. By grounding the agent abstraction in the OS process model, Quine inherits isolation, composition, and resource control directly from the kernel, while naturally supporting recursive delegation, context renewal via exec, and shell-native composition. The design also exposes where the POSIX process model stops: processes provide a robust substrate for execution, but not a complete runtime model for cognition. In particular, the analysis points toward two immediate extensions beyond process semantics: task-relative worlds and revisable time. A reference implementation of Quine is publicly available on GitHub.
Current browse context:
cs.OS
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
