---
title: "From Imperative to Declarative: Towards LLM-friendly OS Interfaces for Boosted Computer-Use Agents"
source: "arXiv Embedded Systems"
url: "https://arxiv.org/abs/2510.04607"
published: "2026-03-26"
fetched: "2026-03-27T07:12:22.378618"
---

Computer Science > Operating Systems
[Submitted on 6 Oct 2025 (v1), last revised 25 Mar 2026 (this version, v2)]
Title:From Imperative to Declarative: Towards LLM-friendly OS Interfaces for Boosted Computer-Use Agents
View PDF HTML (experimental)Abstract:Computer-use agents (CUAs) powered by large language models (LLMs) have emerged as a promising approach to automating computer tasks, yet they struggle with the existing human-oriented OS interfaces - graphical user interfaces (GUIs). GUIs force LLMs to decompose high-level goals into lengthy, error-prone sequences of fine-grained actions, resulting in low success rates and an excessive number of LLM calls.
We propose Declarative Model Interface (DMI), an abstraction that transforms existing GUIs into three declarative primitives: access, state, and observation, thereby providing novel OS interfaces tailored for LLM agents. Our key idea is policy-mechanism separation: LLMs focus on high-level semantic planning (policy) while DMI handles low-level navigation and interaction (mechanism). DMI does not require modifying the application source code or relying on application programming interfaces (APIs).
We evaluate DMI with Microsoft Office Suite (Word, PowerPoint, Excel) on Windows. Integrating DMI into a leading GUI-based agent baseline improves task success rates by 67% and reduces interaction steps by 43.5%. Notably, DMI completes over 61% of successful tasks with a single LLM call.
Submission history
From: Yuan Wang [view email][v1] Mon, 6 Oct 2025 09:14:58 UTC (496 KB)
[v2] Wed, 25 Mar 2026 11:29:08 UTC (511 KB)
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
