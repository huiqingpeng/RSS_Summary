---
title: "UCAgent: An End-to-End Agent for Block-Level Functional Verification"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.25768"
published: "2026-03-30"
fetched: "2026-03-31T07:17:04.858432"
---

Computer Science > Software Engineering
[Submitted on 26 Mar 2026]
Title:UCAgent: An End-to-End Agent for Block-Level Functional Verification
View PDF HTML (experimental)Abstract:Functional verification remains a critical bottleneck in modern IC development cycles, accounting for approximately 70% of total development time in many projects. However, traditional methods, including constrained-random and formal verification, struggle to keep pace with the growing complexity of modern semiconductor designs.
While recent advances in Large Language Models (LLMs) have shown promise in code generation and task automation, significant challenges hinder the realization of end-to-end functional verification automation. These challenges include (i) limited accuracy in generating Verilog/SystemVerilog verification code, (ii) the fragility of LLMs when executing complex, multi-step verification workflows, and (iii) the difficulty of maintaining verification consistency across specifications, coverage models, and test cases throughout the workflow.
To address these challenges, we propose UCAgent, an end-to-end agent that automates hardware block-level functional verification based on three core mechanisms. First, we establish a pure Python verification environment using Picker and Toffee to avoid relying on LLM-generated SystemVerilog verification code. Second, we introduce a configurable 31-stage fine-grained verification workflow to guide the LLM, where each stage is verified by an automated checker. Furthermore, we propose a Verification Consistency Labeling Mechanism (VCLM) that assigns hierarchical labels to LLM-generated artifacts, improving the reliability and traceability of verification.
Experimental results show that UCAgent can complete end-to-end automated verification on multiple modules, including the UART, FPU, and integer divider modules, achieving up to 98.5% code coverage and up to 100% functional coverage. UCAgent also discovers previously unidentified design defects in realistic designs, demonstrating its practical potential.
Current browse context:
cs.SE
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
