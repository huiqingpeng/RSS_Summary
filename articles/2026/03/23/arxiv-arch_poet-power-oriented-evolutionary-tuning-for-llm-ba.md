---
title: "POET: Power-Oriented Evolutionary Tuning for LLM-Based RTL PPA Optimization"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.19333"
published: "2026-03-23"
fetched: "2026-03-24T07:13:55.254076"
---

Computer Science > Hardware Architecture
[Submitted on 19 Mar 2026]
Title:POET: Power-Oriented Evolutionary Tuning for LLM-Based RTL PPA Optimization
View PDF HTML (experimental)Abstract:Applying large language models (LLMs) to RTL code optimization for improved power, performance, and area (PPA) faces two key challenges: ensuring functional correctness of optimized designs despite LLM hallucination, and systematically prioritizing power reduction within the multi-objective PPA trade-off space. We propose POET (Power-Oriented Evolutionary Tuning), a framework that addresses both challenges. For functional correctness, POET introduces a differential-testing-based testbench generation pipeline that treats the original design as a functional oracle, using deterministic simulation to produce golden references and eliminating LLM hallucination from the verification process. For PPA optimization, POET employs an LLM-driven evolutionary mechanism with non-dominated sorting, power-first intra-level ranking, and proportional survivor selection to steer the search toward the low-power region of the Pareto front without manual weight tuning. Evaluated on the RTL-OPT benchmark across 40 diverse RTL designs, POET achieves 100% functional correctness, the best power on all 40 designs, and competitive area and delay improvements.
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
