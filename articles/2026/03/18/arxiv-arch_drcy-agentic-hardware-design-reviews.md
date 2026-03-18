---
title: "DRCY: Agentic Hardware Design Reviews"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.15672"
published: "2026-03-18"
fetched: "2026-03-18T14:52:11.198272"
---

Computer Science > Hardware Architecture
[Submitted on 13 Mar 2026]
Title:DRCY: Agentic Hardware Design Reviews
View PDF HTML (experimental)Abstract:Hardware design errors discovered after fabrication require costly physical respins that can delay products by months. Existing electronic design automation (EDA) tools enforce structural connectivity rules. However, they cannot verify that connections are \emph{semantically} correct with respect to component datasheets. For example, that a symbol's pinout matches the manufacturer's specification, or that a voltage regulator's feedback resistors produce the intended output. We present DRCY, the first production-ready multi-agent LLM system that automates first-pass schematic connection review by autonomously fetching component datasheets, performing pin-by-pin analysis against extracted specifications, and posting findings as inline comments on design reviews. DRCY is deployed in production on AllSpice Hub, a collaborative hardware design platform, where it runs as a CI/CD action triggered on design review submissions. DRCY is used regularly by major hardware companies for use-cases ranging from multi-agent vehicle design to space exploration. We describe DRCY's five-agent pipeline architecture, its agentic datasheet retrieval system with self-evaluation, and its multi-run consensus mechanism for improving reliability on safety-critical analyses
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
