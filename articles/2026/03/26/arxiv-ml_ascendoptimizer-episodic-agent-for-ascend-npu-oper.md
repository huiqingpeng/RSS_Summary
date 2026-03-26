---
title: "AscendOptimizer: Episodic Agent for Ascend NPU Operator Optimization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23566"
published: "2026-03-26"
fetched: "2026-03-27T07:14:36.146905"
---

Computer Science > Machine Learning
[Submitted on 24 Mar 2026]
Title:AscendOptimizer: Episodic Agent for Ascend NPU Operator Optimization
View PDF HTML (experimental)Abstract:AscendC (Ascend C) operator optimization on Huawei Ascend neural processing units (NPUs) faces a two-fold knowledge bottleneck: unlike the CUDA ecosystem, there are few public reference implementations to learn from, and performance hinges on a coupled two-part artifact - a host-side tiling program that orchestrates data movement and a kernel program that schedules and pipelines instructions. We present AscendOptimizer, an episodic agent that bootstraps this missing expertise by turning execution into experience. On the host side, AscendOptimizer performs profiling-in-the-loop evolutionary search to discover valid and high-performing tiling and data-movement configurations directly from hardware feedback. On the kernel side, it mines transferable optimization motifs by rewinding optimized kernels - systematically de-optimizing them to synthesize instructive "bad-to-good" trajectories - and distills these motifs into a retrievable experience bank for guided rewriting. By alternating host tuning and kernel rewriting in a closed loop, AscendOptimizer steadily expands feasibility and pushes latency down. On a benchmark of 127 real AscendC operators, AscendOptimizer achieves a 1.19x geometric-mean speedup over the open-source baseline, with 49.61% of operators outperforming their references, outperforming strong agent and search baselines.
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
