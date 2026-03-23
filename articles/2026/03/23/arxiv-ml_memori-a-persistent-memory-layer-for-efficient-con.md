---
title: "Memori: A Persistent Memory Layer for Efficient, Context-Aware LLM Agents"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19935"
published: "2026-03-23"
fetched: "2026-03-24T07:23:26.120579"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:Memori: A Persistent Memory Layer for Efficient, Context-Aware LLM Agents
View PDF HTML (experimental)Abstract:As large language models (LLMs) evolve into autonomous agents, persistent memory at the API layer is essential for enabling context-aware behavior across LLMs and multi-session interactions. Existing approaches force vendor lock-in and rely on injecting large volumes of raw conversation into prompts, leading to high token costs and degraded performance.
We introduce Memori, an LLM-agnostic persistent memory layer that treats memory as a data structuring problem. Its Advanced Augmentation pipeline converts unstructured dialogue into compact semantic triples and conversation summaries, enabling precise retrieval and coherent reasoning.
Evaluated on the LoCoMo benchmark, Memori achieves 81.95% accuracy, outperforming existing memory systems while using only 1,294 tokens per query (~5% of full context). This results in substantial cost reductions, including 67% fewer tokens than competing approaches and over 20x savings compared to full-context methods.
These results show that effective memory in LLM agents depends on structured representations instead of larger context windows, enabling scalable and cost-efficient deployment.
Submission history
From: Luiz Antonio Buschetto Macarini [view email][v1] Fri, 20 Mar 2026 13:26:38 UTC (311 KB)
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
