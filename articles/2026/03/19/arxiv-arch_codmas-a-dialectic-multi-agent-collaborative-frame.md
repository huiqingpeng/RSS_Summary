---
title: "CODMAS: A Dialectic Multi-Agent Collaborative Framework for Structured RTL Optimization"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.17204"
published: "2026-03-19"
fetched: "2026-03-19T12:03:46.237096"
---

Computer Science > Computation and Language
[Submitted on 17 Mar 2026]
Title:CODMAS: A Dialectic Multi-Agent Collaborative Framework for Structured RTL Optimization
View PDF HTML (experimental)Abstract:Optimizing Register Transfer Level (RTL) code is a critical step in Electronic Design Automation (EDA) for improving power, performance, and area (PPA). We present CODMAS (Collaborative Optimization via a Dialectic Multi-Agent System), a framework that combines structured dialectic reasoning with domain-aware code generation and deterministic evaluation to automate RTL optimization. At the core of CODMAS are two dialectic agents: the Articulator, inspired by rubber-duck debugging, which articulates stepwise transformation plans and exposes latent assumptions; and the Hypothesis Partner, which predicts outcomes and reconciles deviations between expected and actual behavior to guide targeted refinements. These agents direct a Domain-Specific Coding Agent (DCA) to generate architecture-aware Verilog edits and a Code Evaluation Agent (CEA) to verify syntax, functionality, and PPA metrics. We introduce RTLOPT, a benchmark of 120 Verilog triples (unoptimized, optimized, testbench) for pipelining and clock-gating transformations. Across proprietary and open LLMs, CODMAS achieves ~25% reduction in critical path delay for pipelining and ~22% power reduction for clock gating, while reducing functional and compilation failures compared to strong prompting and agentic baselines. These results demonstrate that structured multi-agent reasoning can significantly enhance automated RTL optimization and scale to more complex designs and broader optimization tasks.
Submission history
From: Prashanth Vijayaraghavan [view email][v1] Tue, 17 Mar 2026 23:10:07 UTC (914 KB)
Current browse context:
cs.CL
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
