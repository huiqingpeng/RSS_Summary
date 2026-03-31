---
title: "MemGuard-Alpha: Detecting and Filtering Memorization-Contaminated Signals in LLM-Based Financial Forecasting via Membership Inference and Cross-Model Disagreement"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26797"
published: "2026-03-31"
fetched: "2026-04-01T07:18:15.968448"
---

Computer Science > Machine Learning
[Submitted on 26 Mar 2026]
Title:MemGuard-Alpha: Detecting and Filtering Memorization-Contaminated Signals in LLM-Based Financial Forecasting via Membership Inference and Cross-Model Disagreement
View PDFAbstract:Large language models (LLMs) are increasingly used to generate financial alpha signals, yet growing evidence shows that LLMs memorize historical financial data from their training corpora, producing spurious predictive accuracy that collapses out-of-sample. This memorization-induced look-ahead bias threatens the validity of LLM-based quantitative strategies. Prior remedies -- model retraining and input anonymization -- are either prohibitively expensive or introduce significant information loss. No existing method offers practical, zero-cost signal-level filtering for real-time trading. We introduce MemGuard-Alpha, a post-generation framework comprising two algorithms: (i) the MemGuard Composite Score (MCS), which combines five membership inference attack (MIA) methods with temporal proximity features via logistic regression, achieving Cohen's d = 18.57 for contamination separation (d = 0.39-1.37 using MIA features alone); and (ii) Cross-Model Memorization Disagreement (CMMD), which exploits variation in training cutoff dates across LLMs to separate memorized signals from genuine reasoning. Evaluated across seven LLMs (124M-7B parameters), 50 S&P 100 stocks, 42,800 prompts, and five MIA methods over 5.5 years (2019-2024), CMMD achieves a Sharpe ratio of 4.11 versus 2.76 for unfiltered signals (49% improvement). Clean signals produce 14.48 bps average daily return versus 2.13 bps for tainted signals (7x difference). A striking crossover pattern emerges: in-sample accuracy rises with contamination (40.8% to 52.5%) while out-of-sample accuracy falls (47% to 42%), providing direct evidence that memorization inflates apparent accuracy at the cost of generalization.
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
