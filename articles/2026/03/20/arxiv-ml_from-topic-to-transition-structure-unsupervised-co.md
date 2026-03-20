---
title: "From Topic to Transition Structure: Unsupervised Concept Discovery at Corpus Scale via Predictive Associative Memory"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18420"
published: "2026-03-20"
fetched: "2026-03-20T13:12:51.167148"
---

Computer Science > Artificial Intelligence
[Submitted on 19 Mar 2026]
Title:From Topic to Transition Structure: Unsupervised Concept Discovery at Corpus Scale via Predictive Associative Memory
View PDF HTML (experimental)Abstract:Embedding models group text by semantic content, what text is about. We show that temporal co-occurrence within texts discovers a different kind of structure: recurrent transition-structure concepts or what text does. We train a 29.4M-parameter contrastive model on 373 million co-occurrence pairs from 9,766 Project Gutenberg texts (24.96 million passages), mapping pre-trained embeddings into an association space where passages with similar transition structure cluster together. Under capacity constraint (42.75% accuracy), the model must compress across recurring patterns rather than memorise individual co-occurrences. Clustering at six granularities (k=50 to k=2,000) produces a multi-resolution concept map; from broad modes like "direct confrontation" and "lyrical meditation" to precise registers and scene templates like "sailor dialect" and "courtroom cross-examination." At k=100, clusters average 4,508 books each (of 9,766), confirming corpus-wide patterns. Direct comparison with embedding-similarity clustering shows that raw embeddings group by topic while association-space clusters group by function, register, and literary tradition. Unseen novels are assigned to existing clusters without retraining; the association model concentrates each novel into a selective subset of coherent clusters, while raw embedding assignment saturates nearly all clusters. Validation controls address positional, length, and book-concentration confounds. The method extends Predictive Associative Memory (PAM, arXiv:2602.11322) from episodic recall to concept formation: where PAM recalls specific associations, multi-epoch contrastive training under compression extracts structural patterns that transfer to unseen texts, the same framework producing qualitatively different behaviour in a different regime.
Current browse context:
cs.AI
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
