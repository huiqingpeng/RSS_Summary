---
title: "Differentiable Symbolic Planning: A Neural Architecture for Constraint Reasoning with Learned Feasibility"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.02350"
published: "2026-04-07"
fetched: "2026-04-08T07:02:35.762494"
---

Computer Science > Machine Learning
[Submitted on 19 Feb 2026]
Title:Differentiable Symbolic Planning: A Neural Architecture for Constraint Reasoning with Learned Feasibility
View PDF HTML (experimental)Abstract:Neural networks excel at pattern recognition but struggle with constraint reasoning -- determining whether configurations satisfy logical or physical constraints. We introduce Differentiable Symbolic Planning (DSP), a neural architecture that performs discrete symbolic reasoning while remaining fully differentiable. DSP maintains a feasibility channel (phi) that tracks constraint satisfaction evidence at each node, aggregates this into a global feasibility signal (Phi) through learned rule-weighted combination, and uses sparsemax attention to achieve exact-zero discrete rule selection. We integrate DSP into a Universal Cognitive Kernel (UCK) that combines graph attention with iterative constraint propagation. Evaluated on three constraint reasoning benchmarks -- graph reachability, Boolean satisfiability, and planning feasibility -- UCK+DSP achieves 97.4% accuracy on planning under 4x size generalization (vs. 59.7% for ablated baselines), 96.4% on SAT under 2x generalization, and maintains balanced performance on both positive and negative classes where standard neural approaches collapse. Ablation studies reveal that global phi aggregation is critical: removing it causes accuracy to drop from 98% to 64%. The learned phi signal exhibits interpretable semantics, with values of +18 for feasible cases and -13 for infeasible cases emerging without supervision.
Submission history
From: Venkatakrishna Reddy Oruganti [view email][v1] Thu, 19 Feb 2026 03:38:03 UTC (198 KB)
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
