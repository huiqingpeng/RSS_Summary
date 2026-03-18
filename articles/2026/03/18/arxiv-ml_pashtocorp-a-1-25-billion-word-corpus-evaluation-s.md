---
title: "PashtoCorp: A 1.25-Billion-Word Corpus, Evaluation Suite, and Reproducible Pipeline for Low-Resource Language Development"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16354"
published: "2026-03-18"
fetched: "2026-03-18T16:12:28.030957"
---

Computer Science > Computation and Language
[Submitted on 17 Mar 2026]
Title:PashtoCorp: A 1.25-Billion-Word Corpus, Evaluation Suite, and Reproducible Pipeline for Low-Resource Language Development
View PDF HTML (experimental)Abstract:We present PashtoCorp, a 1.25-billion-word corpus for Pashto, a language spoken by 60 million people that remains severely underrepresented in NLP. The corpus is assembled from 39 sources spanning seven HuggingFace
datasets and 32 purpose-built web scrapers, processed through a reproducible pipeline with Arabic-script tokenization, SHA-256 deduplication, and quality filtering. At 1.25B words across 2.81 million documents,
PashtoCorp is 40x larger than the OSCAR Pashto subset and 83x larger than the previously largest dedicated Pashto corpus. Continued MLM pretraining of XLM-R-base on PashtoCorp reduces held-out perplexity by 25.1%
(8.08->6.06). On WikiANN Pashto NER, the pretrained model improves entity F1 by 10% relative (19.0%->21.0%) and reduces training variance nearly 7x; the largest gain appears at 50 training sentences (+27%), with
PashtoCorp covering 97.9% of WikiANN entity vocabulary. On Belebele Pashto reading comprehension, Gemma-3n achieves 64.6% accuracy, the first published LLM baseline for Pashto on this benchmark. A leave-one-out source
ablation shows that Wikipedia (0.7% of documents) is the most critical source for NER: removing it alone reduces entity F1 by 47%. Corpus data, trained model, and code are available at
this https URL, this https URL, and this https URL.
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
