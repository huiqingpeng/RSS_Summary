---
title: "Benchmarking PDF Parsers on Table Extraction with LLM-based Semantic Evaluation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18652"
published: "2026-03-20"
fetched: "2026-03-20T15:14:16.234742"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 19 Mar 2026]
Title:Benchmarking PDF Parsers on Table Extraction with LLM-based Semantic Evaluation
View PDF HTML (experimental)Abstract:Reliably extracting tables from PDFs is essential for large-scale scientific data mining and knowledge base construction, yet existing evaluation approaches rely on rule-based metrics that fail to capture semantic equivalence of table content. We present a benchmarking framework based on synthetically generated PDFs with precise LaTeX ground truth, using tables sourced from arXiv to ensure realistic complexity and diversity. As our central methodological contribution, we apply LLM-as-a-judge for semantic table evaluation, integrated into a matching pipeline that accommodates inconsistencies in parser outputs. Through a human validation study comprising over 1,500 quality judgments on extracted table pairs, we show that LLM-based evaluation achieves substantially higher correlation with human judgment (Pearson r=0.93) compared to Tree Edit Distance-based Similarity (TEDS, r=0.68) and Grid Table Similarity (GriTS, r=0.70). Evaluating 21 contemporary PDF parsers across 100 synthetic documents containing 451 tables reveals significant performance disparities. Our results offer practical guidance for selecting parsers for tabular data extraction and establish a reproducible, scalable evaluation methodology for this critical task.
Code and data: this https URL Metric study and human evaluation: this https URL
Current browse context:
cs.CV
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
