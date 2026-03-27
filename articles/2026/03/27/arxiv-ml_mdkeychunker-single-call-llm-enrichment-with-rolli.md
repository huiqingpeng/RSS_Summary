---
title: "MDKeyChunker: Single-Call LLM Enrichment with Rolling Keys and Key-Based Restructuring for High-Accuracy RAG"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23533"
published: "2026-03-27"
fetched: "2026-03-28T07:12:53.584438"
---

Computer Science > Computation and Language
[Submitted on 8 Mar 2026]
Title:MDKeyChunker: Single-Call LLM Enrichment with Rolling Keys and Key-Based Restructuring for High-Accuracy RAG
View PDF HTML (experimental)Abstract:RAG pipelines typically rely on fixed-size chunking, which ignores document structure, fragments semantic units across boundaries, and requires multiple LLM calls per chunk for metadata extraction. We present MDKeyChunker, a three-stage pipeline for Markdown documents that (1) performs structure-aware chunking treating headers, code blocks, tables, and lists as atomic units; (2) enriches each chunk via a single LLM call extracting title, summary, keywords, typed entities, hypothetical questions, and a semantic key, while propagating a rolling key dictionary to maintain document-level context; and (3) restructures chunks by merging those sharing the same semantic key via bin-packing, co-locating related content for retrieval. The single-call design extracts all seven metadata fields in one LLM invocation, eliminating the need for separate per-field extraction passes. Rolling key propagation replaces hand-tuned scoring with LLM-native semantic matching. An empirical evaluation on 30 queries over an 18-document Markdown corpus shows Config D (BM25 over structural chunks) achieves Recall@5=1.000 and MRR=0.911, while dense retrieval over the full pipeline (Config C) reaches Recall@5=0.867. MDKeyChunker is implemented in Python with four dependencies and supports any OpenAI-compatible endpoint.
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
