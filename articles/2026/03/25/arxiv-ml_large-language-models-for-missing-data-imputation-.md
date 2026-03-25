---
title: "Large Language Models for Missing Data Imputation: Understanding Behavior, Hallucination Effects, and Control Mechanisms"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22332"
published: "2026-03-25"
fetched: "2026-03-26T07:12:15.807302"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:Large Language Models for Missing Data Imputation: Understanding Behavior, Hallucination Effects, and Control Mechanisms
View PDF HTML (experimental)Abstract:Data imputation is a cornerstone technique for handling missing values in real-world datasets, which are often plagued by missingness. Despite recent progress, prior studies on Large Language Models-based imputation remain limited by scalability challenges, restricted cross-model comparisons, and evaluations conducted on small or domain-specific datasets. Furthermore, heterogeneous experimental protocols and inconsistent treatment of missingness mechanisms (MCAR, MAR, and MNAR) hinder systematic benchmarking across methods. This work investigates the robustness of Large Language Models for missing data imputation in tabular datasets using a zero-shot prompt engineering approach. To this end, we present a comprehensive benchmarking study comparing five widely used LLMs against six state-of-the-art imputation baselines. The experimental design evaluates these methods across 29 datasets (including nine synthetic datasets) under MCAR, MAR, and MNAR mechanisms, with missing rates of up to 20\%. The results demonstrate that leading LLMs, particularly Gemini 3.0 Flash and Claude 4.5 Sonnet, consistently achieve superior performance on real-world open-source datasets compared to traditional methods. However, this advantage appears to be closely tied to the models' prior exposure to domain-specific patterns learned during pre-training on internet-scale corpora. In contrast, on synthetic datasets, traditional methods such as MICE outperform LLMs, suggesting that LLM effectiveness is driven by semantic context rather than purely statistical reconstruction. Furthermore, we identify a clear trade-off: while LLMs excel in imputation quality, they incur significantly higher computational time and monetary costs. Overall, this study provides a large-scale comparative analysis, positioning LLMs as promising semantics-driven imputers for complex tabular data.
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
