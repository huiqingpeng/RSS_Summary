---
title: "The Alignment Tax: Response Homogenization in Aligned LLMs and Its Implications for Uncertainty Estimation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24124"
published: "2026-03-26"
fetched: "2026-03-27T07:20:42.409378"
---

Computer Science > Machine Learning
[Submitted on 25 Mar 2026]
Title:The Alignment Tax: Response Homogenization in Aligned LLMs and Its Implications for Uncertainty Estimation
View PDF HTML (experimental)Abstract:RLHF-aligned language models exhibit response homogenization: on TruthfulQA (n=790), 40-79% of questions produce a single semantic cluster across 10 i.i.d. samples. On affected questions, sampling-based uncertainty methods have zero discriminative power (AUROC=0.500), while free token entropy retains signal (0.603). This alignment tax is task-dependent: on GSM8K (n=500), token entropy achieves 0.724 (Cohen's d=0.81).
A base-vs-instruct ablation confirms the causal role of alignment: the base model shows 1.0% single-cluster rate vs. 28.5% for the instruct model (p < 10^{-6}). A training stage ablation (Base 0.0% -> SFT 1.5% -> DPO 4.0% SCR) localizes the cause to DPO, not SFT. Cross-family replication on four model families reveals alignment tax severity varies by family and scale. We validate across 22 experiments, 5 benchmarks, 4 model families, and 3 model scales (3B-14B), with Jaccard, embedding, and NLI-based baselines at three DeBERTa scales (all ~0.51 AUROC). Cross-embedder validation with two independent embedding families rules out coupling bias. Cross-dataset validation on WebQuestions (58.0% SCR) confirms generalization beyond TruthfulQA. The central finding -- response homogenization -- is implementation-independent and label-free. Motivated by this diagnosis, we explore a cheapest-first cascade (UCBD) over orthogonal uncertainty signals. Selective prediction raises GSM8K accuracy from 84.4% to 93.2% at 50% coverage; weakly dependent boundaries (|r| <= 0.12) enable 57% cost savings.
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
