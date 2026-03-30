---
title: "Who Checks the Checker? Enhancing Component-level Architectural SEU Fault Tolerance for End-to-End SoC Protection"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.26637"
published: "2026-03-30"
fetched: "2026-03-31T07:16:58.190018"
---

Computer Science > Hardware Architecture
[Submitted on 27 Mar 2026]
Title:Who Checks the Checker? Enhancing Component-level Architectural SEU Fault Tolerance for End-to-End SoC Protection
View PDF HTML (experimental)Abstract:Single-event upset (SEU) fault tolerance for systems-on-chip (SoCs) in radiation-heavy environments is often addressed by architectural fault-tolerance approaches protecting individual SoC components (e.g., cores, memories) in isolation. However, the protection of voting logic and interconnections among components is also critical, as these become single points of failure in the design. We investigate combining multiple fault-tolerance approaches targeting individual SoC components, including interconnect and voting logic to ensure end-to-end SoC-level architectural SEU fault tolerance, while minimizing implementation area overheads. Enforcing an overlap between the protection methods ensures hardening of the whole design without gaps, while curtailing overheads. We demonstrate our approach on a RISC-V microcontroller SoC. SEU fault-tolerance is assessed with simulation-based fault injection. Overheads are assessed with full physical implementation. Tolerance to over 99.9% of faults in both RTL and implemented netlist is demonstrated. Furthermore, the design exhibits 22% lower implementation overhead compared to a single global fault-tolerance method, such as fine-grained triplication.
Submission history
From: Michael Rogenmoser [view email][v1] Fri, 27 Mar 2026 17:42:16 UTC (5,801 KB)
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
