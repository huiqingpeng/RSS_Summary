---
title: "The Truncation Blind Spot: How Decoding Strategies Systematically Exclude Human-Like Token Choices"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18482"
published: "2026-03-20"
fetched: "2026-03-20T13:13:23.598887"
---

Computer Science > Computation and Language
[Submitted on 19 Mar 2026]
Title:The Truncation Blind Spot: How Decoding Strategies Systematically Exclude Human-Like Token Choices
View PDF HTML (experimental)Abstract:Standard decoding strategies for text generation, including top-k, nucleus sampling, and contrastive search, select tokens based on likelihood, restricting selection to high-probability regions. Human language production operates differently: tokens are chosen for communicative appropriateness rather than statistical frequency. This mismatch creates a truncation blind spot: contextually appropriate but statistically rare tokens remain accessible to humans yet unreachable by likelihood-based decoding. We hypothesize this contributes to the detectability of machine-generated text. Analyzing over 1.8 million texts across eight language models, five decoding strategies, and 53 hyperparameter configurations, we find that 8-18% of human-selected tokens fall outside typical truncation boundaries. Simple classifiers trained on predictability and lexical diversity achieve remarkable detection rates. Crucially, neither model scale nor architecture correlates strongly with detectability; truncation parameters account for most variance. Configurations achieving low detectability often produce incoherent text, indicating that evading detection and producing natural text are distinct objectives. These findings suggest detectability is enhanced by likelihood-based token selection, not merely a matter of model capability.
Submission history
From: Esteban Garces Arias [view email][v1] Thu, 19 Mar 2026 04:36:22 UTC (2,065 KB)
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
