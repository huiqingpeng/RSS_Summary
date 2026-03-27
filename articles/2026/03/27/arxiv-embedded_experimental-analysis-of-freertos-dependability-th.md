---
title: "Experimental Analysis of FreeRTOS Dependability through Targeted Fault Injection Campaigns"
source: "arXiv Embedded Systems"
url: "https://arxiv.org/abs/2603.25666"
published: "2026-03-27"
fetched: "2026-03-28T07:05:41.055997"
---

Computer Science > Operating Systems
[Submitted on 26 Mar 2026]
Title:Experimental Analysis of FreeRTOS Dependability through Targeted Fault Injection Campaigns
View PDF HTML (experimental)Abstract:Real-Time Operating Systems (RTOSes) play a crucial role in safety-critical domains, where deterministic and predictable task execution is essential. Yet they are increasingly exposed to ionizing radiation, which can compromise system dependability.
To assess FreeRTOS under such conditions, we introduce KRONOS, a software-based, non-intrusive post-propagation Fault Injection (FI) framework that injects transient and permanent faults into Operating System-visible kernel data structures without specialized hardware or debug interfaces. Using KRONOS, we conduct an extensive FI campaign on core FreeRTOS kernel components, including scheduler-related variables and Task Control Blocks (TCBs), characterizing the impact of kernel-level corruptions on functional correctness, timing behavior, and availability.
The results show that corruption of pointer and key scheduler-related variables frequently leads to crashes, whereas many TCB fields have only a limited impact on system availability.
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
