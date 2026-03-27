---
title: "DepthCharge: A Domain-Agnostic Framework for Measuring Depth-Dependent Knowledge in Large Language Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23514"
published: "2026-03-27"
fetched: "2026-03-28T07:12:35.360737"
---

Computer Science > Computation and Language
[Submitted on 5 Mar 2026]
Title:DepthCharge: A Domain-Agnostic Framework for Measuring Depth-Dependent Knowledge in Large Language Models
View PDF HTML (experimental)Abstract:Large Language Models appear competent when answering general questions but often fail when pushed into domain-specific details. No existing methodology provides an out-of-the-box solution for measuring how deeply LLMs can sustain accurate responses under adaptive follow-up questioning across arbitrary domains.
We present DepthCharge, a domain-agnostic framework that measures knowledge depth through three innovations: adaptive probing that generates follow-up questions based on concepts the model actually mentions, on-demand fact verification from authoritative sources, and survival statistics with constant sample sizes at every depth level. The framework can be deployed on any knowledge domain with publicly verifiable facts, without requiring pre-constructed test sets or domain-specific expertise. DepthCharge results are relative to the evaluator model used for answer checking, making the framework a tool for comparative evaluation rather than absolute accuracy certification.
Empirical validation across four diverse domains (Medicine, Constitutional Law, Ancient Rome, and Quantum Computing) with five frontier models demonstrates that DepthCharge reveals depth-dependent performance variation hidden by standard benchmarks. Expected Valid Depth (EVD) ranges from 3.45 to 7.55 across model-domain combinations, and model rankings vary substantially by domain, with no single model dominating all areas. Cost-performance analysis further reveals that expensive models do not always achieve deeper knowledge, suggesting that domain-specific evaluation is more informative than aggregate benchmarks for model selection in professional applications.
Submission history
From: Alexander Sheppert [view email][v1] Thu, 5 Mar 2026 20:49:11 UTC (1,206 KB)
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
