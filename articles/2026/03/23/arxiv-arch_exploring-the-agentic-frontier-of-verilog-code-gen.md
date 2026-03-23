---
title: "Exploring the Agentic Frontier of Verilog Code Generation"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.19347"
published: "2026-03-23"
fetched: "2026-03-24T07:14:03.637069"
---

Computer Science > Hardware Architecture
[Submitted on 19 Mar 2026]
Title:Exploring the Agentic Frontier of Verilog Code Generation
View PDF HTML (experimental)Abstract:Large language models (LLMs) have made rapid advancements in code generation for popular languages such as Python and C++. Many of these recent gains can be attributed to the use of ``agents'' that wrap domain-relevant tools alongside LLMs. Hardware design languages such as Verilog have also seen improved code generation in recent years, but the impact of agentic frameworks on Verilog code generation tasks remains unclear. In this work, we present the first systematic evaluation of agentic LLMs for Verilog generation, using the recently introduced CVDP benchmark. We also introduce several open-source hardware design agent harnesses, providing a model-agnostic baseline for future work. Through controlled experiments across frontier models, we study how structured prompting and tool design affect performance, analyze agent failure modes and tool usage patterns, compare open-source and closed-source models, and provide qualitative examples of successful and failed agent runs. Our results show that naive agentic wrapping around frontier models can degrade performance (relative to standard forward passes with optimized prompts), but that structured harnesses meaningfully match and in some cases exceed non-agentic baselines. We find that the performance gap between open and closed source models is driven by both higher crash rates and weaker tool output interpretation. Our exploration illuminates the path towards designing special-purpose agents for verilog generation in the future.
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
