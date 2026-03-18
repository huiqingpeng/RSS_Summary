---
title: "AutothinkRAG: Complexity-Aware Control of Retrieval-Augmented Reasoning for Image-Text Interaction"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.05551"
published: "2026-03-18"
fetched: "2026-03-18T19:07:10.315709"
---

Computer Science > Information Retrieval
[Submitted on 5 Mar 2026 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:AutothinkRAG: Complexity-Aware Control of Retrieval-Augmented Reasoning for Image-Text Interaction
View PDF HTML (experimental)Abstract:Multimodal document question answering requires retrieving dispersed evidence from visually rich long documents and performing reliable reasoning over heterogeneous information. Existing multimodal RAG systems remain limited by two bottlenecks: static retrieval that ignores query complexity, and end-to-end Vision-Language Models (VLMs) that couple visual perception with logical reasoning, leading to inefficient computation and unstable answer generation. We propose AutoThinkRAG, a complexity-aware inference architecture for multimodal document QA. It has two components: (1) a Query Complexity Router that analyzes query difficulty and structure to adaptively select retrieval and reasoning paths; and (2) a Perception--Reasoning Decoupling architecture that uses a lightweight VLM as a high-fidelity visual interpreter to convert query-relevant visual cues into textual representations, which are then passed to an LLM for logical reasoning and answer synthesis. This design improves both efficiency and robustness, especially on long-document and unanswerable queries. Experiments on DocBench and MMLongBench show that AutoThinkRAG achieves 82.13\% and 51.29\% overall accuracy, respectively, while reducing per-query token consumption by 18.9\% and monetary cost by 18.2\%. Further analyses show that the gains are most pronounced on complex queries requiring adaptive retrieval and multi-step reasoning.
Submission history
From: Jiashu Yang [view email][v1] Thu, 5 Mar 2026 02:29:33 UTC (697 KB)
[v2] Tue, 17 Mar 2026 15:59:36 UTC (1,256 KB)
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
