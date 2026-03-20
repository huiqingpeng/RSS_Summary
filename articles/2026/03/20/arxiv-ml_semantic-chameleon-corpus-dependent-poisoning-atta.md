---
title: "Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18034"
published: "2026-03-20"
fetched: "2026-03-20T13:07:38.476603"
---

Computer Science > Cryptography and Security
[Submitted on 10 Mar 2026]
Title:Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems
View PDF HTML (experimental)Abstract:Retrieval-Augmented Generation (RAG) systems extend large language models (LLMs) with external knowledge sources but introduce new attack surfaces through the retrieval pipeline. In particular, adversaries can poison retrieval corpora so that malicious documents are preferentially retrieved at inference time, enabling targeted manipulation of model outputs. We study gradient-guided corpus poisoning attacks against modern RAG pipelines and evaluate retrieval-layer defenses that require no modification to the underlying LLM.
We implement dual-document poisoning attacks consisting of a sleeper document and a trigger document optimized using Greedy Coordinate Gradient (GCG). In a large-scale evaluation on the Security Stack Exchange corpus (67,941 documents) with 50 attack attempts, gradient-guided poisoning achieves a 38.0 percent co-retrieval rate under pure vector retrieval.
We show that a simple architectural modification, hybrid retrieval combining BM25 and vector similarity, substantially mitigates this attack. Across all 50 attacks, hybrid retrieval reduces gradient-guided attack success from 38 percent to 0 percent without modifying the model or retraining the retriever. When attackers jointly optimize payloads for both sparse and dense retrieval signals, hybrid retrieval can be partially circumvented, achieving 20-44 percent success, but still significantly raises attack difficulty relative to vector-only retrieval.
Evaluation across five LLM families (GPT-5.3, GPT-4o, Claude Sonnet 4.6, Llama 4, and GPT-4o-mini) shows attack success ranging from 46.7 percent to 93.3 percent. Cross-corpus evaluation on the FEVER Wikipedia dataset (25 attacks) yields 0 percent attack success across all retrieval configurations.
Current browse context:
cs.CR
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
