---
title: "Improving Efficiency of GPU Kernel Optimization Agents using a Domain-Specific Language and Speed-of-Light Guidance"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.29010"
published: "2026-04-01"
fetched: "2026-04-02T07:14:23.385529"
---

Computer Science > Machine Learning
[Submitted on 30 Mar 2026]
Title:Improving Efficiency of GPU Kernel Optimization Agents using a Domain-Specific Language and Speed-of-Light Guidance
View PDF HTML (experimental)Abstract:Optimizing GPU kernels with LLM agents is an iterative process over a large design space. Every candidate must be generated, compiled, validated, and profiled, so fewer trials will save both runtime and cost. We make two key observations. First, the abstraction level that agents operate at is important. If it is too low, the LLM wastes reasoning on low-impact details. If it is too high, it may miss important optimization choices. Second, agents cannot easily tell when they reach the point of diminishing returns, wasting resources as they continue searching.
These observations motivate two design principles to improve efficiency: (1) a compact domain-specific language (DSL) that can be learned in context and lets the model reason at a higher level while preserving important optimization levers, and (2) Speed-of-Light (SOL) guidance that uses first-principles performance bounds to steer and budget search. We implement these principles in $\mu$CUTLASS, a DSL with a compiler for CUTLASS-backed GPU kernels that covers kernel configuration, epilogue fusion, and multi-stage pipelines. We use SOL guidance to estimate headroom and guide optimization trials, deprioritize problems that are near SOL, and flag kernels that game the benchmark.
On 59 KernelBench problems with the same iteration budgets, switching from generating low-level code to DSL code using GPT-5-mini turns a 0.40x geomean regression into a 1.27x speedup over PyTorch. Adding SOL-guided steering raises this to 1.56x. Across model tiers, $\mu$CUTLASS + SOL-guidance lets weaker models outperform stronger baseline agents at lower token cost. SOL-guided budgeting saves 19-43% of tokens while retaining at least 95% of geomean speedup, with the best policy reaching a 1.68x efficiency gain. Lastly, SOL analysis helps detect benchmark-gaming cases, where kernels may appear fast while failing to perform the intended computation.
Submission history
From: Siva Kumar Sastry Hari [view email][v1] Mon, 30 Mar 2026 21:16:39 UTC (6,047 KB)
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
