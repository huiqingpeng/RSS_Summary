---
title: "Robust Batch-Level Query Routing for Large Language Models under Cost and Capacity Constraints"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26796"
published: "2026-03-31"
fetched: "2026-04-01T07:18:11.558322"
---

Computer Science > Machine Learning
[Submitted on 25 Mar 2026]
Title:Robust Batch-Level Query Routing for Large Language Models under Cost and Capacity Constraints
View PDF HTML (experimental)Abstract:We study the problem of routing queries to large language models (LLMs) under cost, GPU resources, and concurrency constraints. Prior per-query routing methods often fail to control batch-level cost, especially under non-uniform or adversarial batching. To address this, we propose a batch-level, resource-aware routing framework that jointly optimizes model assignment for each batch while respecting cost and model capacity limits. We further introduce a robust variant that accounts for uncertainty in predicted LLM performance, along with an offline instance allocation procedure that balances quality and throughput across multiple models. Experiments on two multi-task LLM benchmarks show that robustness improves accuracy by 1-14% over non-robust counterparts (depending on the performance estimator), batch-level routing outperforms per-query methods by up to 24% under adversarial batching, and optimized instance allocation yields additional gains of up to 3% compared to a non-optimized allocation, all while strictly controlling cost and GPU resource constraints.
Submission history
From: Jelena Markovic-Voronov [view email][v1] Wed, 25 Mar 2026 22:24:11 UTC (975 KB)
Current browse context:
cs.LG
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
