---
title: "Decomposing Discrimination: Causal Mediation Analysis for AI-Driven Credit Decisions"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.27510"
published: "2026-03-31"
fetched: "2026-04-01T07:25:03.883819"
---

Computer Science > Machine Learning
[Submitted on 29 Mar 2026]
Title:Decomposing Discrimination: Causal Mediation Analysis for AI-Driven Credit Decisions
View PDF HTML (experimental)Abstract:Statistical fairness metrics in AI-driven credit decisions conflate two causally distinct mechanisms: discrimination operating directly from a protected attribute to a credit outcome, and structural inequality propagating through legitimate financial features. We formalise this distinction using Pearl's framework of natural direct and indirect effects applied to the credit decision setting. Our primary theoretical contribution is an identification strategy for natural direct and indirect effects under treatment-induced confounding -- the prevalent setting in which protected attributes causally affect both financial mediators and the final decision, violating standard sequential ignorability. We show that interventional direct and indirect effects (IDE/IIE) are identified under the weaker Modified Sequential Ignorability assumption, and prove that IDE/IIE provide conservative bounds on the unidentified natural effects under monotone indirect treatment response. We propose a doubly-robust augmented inverse probability weighted (AIPW) estimator for IDE/IIE with semiparametric efficiency properties, implemented via cross-fitting. An E-value sensitivity analysis addresses residual confounding on the direct pathway. Empirical evaluation on 89,465 real HMDA conventional purchase mortgage applications from New York State (2022) demonstrates that approximately 77% of the observed 7.9 percentage-point racial denial disparity operates through financial mediators shaped by structural inequality, while the remaining 23% constitutes a conservative lower bound on direct discrimination. The open-source CausalFair Python package implements the full pipeline for deployment at resource-constrained financial institutions.
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
