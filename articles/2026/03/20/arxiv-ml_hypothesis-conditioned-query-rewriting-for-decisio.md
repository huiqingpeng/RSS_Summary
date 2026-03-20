---
title: "Hypothesis-Conditioned Query Rewriting for Decision-Useful Retrieval"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19008"
published: "2026-03-20"
fetched: "2026-03-20T13:18:58.956478"
---

Computer Science > Computation and Language
[Submitted on 19 Mar 2026]
Title:Hypothesis-Conditioned Query Rewriting for Decision-Useful Retrieval
View PDF HTML (experimental)Abstract:Retrieval-Augmented Generation (RAG) improves Large Language Models (LLMs) by grounding generation in external, non-parametric knowledge. However, when a task requires choosing among competing options, simply grounding generation in broadly relevant context is often insufficient to drive the final decision. Existing RAG methods typically rely on a single initial query, which often favors topical relevance over decision-relevant evidence, and therefore retrieves background information that can fail to discriminate among answer options. To address this issue, here we propose Hypothesis-Conditioned Query Rewriting (HCQR), a training-free pre-retrieval framework that reorients RAG from topic-oriented retrieval to evidence-oriented retrieval. HCQR first derives a lightweight working hypothesis from the input question and candidate options, and then rewrites retrieval into three targeted queries that seek evidence to: (1) support the hypothesis, (2) distinguish it from competing alternatives, and (3) verify salient clues in the question. This approach enables context retrieval that is more directly aligned with answer selection, allowing the generator to confirm or overturn the initial hypothesis based on the retrieved evidence. Experiments on MedQA and MMLU-Med show that HCQR consistently outperforms single-query RAG and re-rank/filter baselines, improving average accuracy over Simple RAG by 5.9 and 3.6 points, respectively. Code is available at this https URL.
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
