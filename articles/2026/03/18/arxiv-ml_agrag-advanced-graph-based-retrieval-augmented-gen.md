---
title: "AGRAG: Advanced Graph-based Retrieval-Augmented Generation for LLMs"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2511.05549"
published: "2026-03-18"
fetched: "2026-03-18T16:20:20.539654"
---

Computer Science > Machine Learning
[Submitted on 2 Nov 2025 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:AGRAG: Advanced Graph-based Retrieval-Augmented Generation for LLMs
View PDF HTML (experimental)Abstract:Graph-based retrieval-augmented generation (Graph-based RAG) has demonstrated significant potential in enhancing Large Language Models (LLMs) with structured knowledge. However, existing methods face three critical challenges: Inaccurate Graph Construction, caused by LLM hallucination; Poor Reasoning Ability, caused by failing to generate explicit reasons telling LLM why certain chunks were selected; and Inadequate Answering, which only partially answers the query due to the inadequate LLM reasoning, making their performance lag behind NaiveRAG on certain tasks. To address these issues, we propose AGRAG, an advanced graph-based retrieval-augmented generation framework. When constructing the graph, AGRAG substitutes the widely used LLM entity extraction method with a statistics-based method, avoiding hallucination and error propagation. During retrieval, AGRAG formulates the graph reasoning procedure as the Minimum Cost Maximum Influence (MCMI) subgraph generation problem, where we try to include more nodes with high influence score, but with less involving edge cost, to make the generated reasoning paths more comprehensive. We prove this problem to be NP-hard, and propose a greedy algorithm to solve it. The MCMI subgraph generated can serve as explicit reasoning paths to tell LLM why certain chunks were retrieved, thereby making the LLM better focus on the query-related part contents of the chunks, reducing the impact of noise, and improving AGRAG's reasoning ability. Furthermore, compared with the simple tree-structured reasoning paths, our MCMI subgraph can allow more complex graph structures, such as cycles, and improve the comprehensiveness of the generated reasoning paths. The code and prompt of AGRAG are released at: this https URL.
Submission history
From: Yubo Wang [view email][v1] Sun, 2 Nov 2025 06:13:06 UTC (624 KB)
[v2] Tue, 17 Mar 2026 07:22:27 UTC (628 KB)
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
