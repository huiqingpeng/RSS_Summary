---
title: "AgenticRS-EnsNAS: Ensemble-Decoupled Self-Evolving Architecture Search"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20014"
published: "2026-03-23"
fetched: "2026-03-24T07:23:59.894427"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:AgenticRS-EnsNAS: Ensemble-Decoupled Self-Evolving Architecture Search
View PDF HTML (experimental)Abstract:Neural Architecture Search (NAS) deployment in industrial production systems faces a fundamental validation bottleneck: verifying a single candidate architecture pi requires evaluating the deployed ensemble of M models, incurring prohibitive O(M) computational cost per candidate. This cost barrier severely limits architecture iteration frequency in real-world applications where ensembles (M=50-200) are standard for robustness. This work introduces Ensemble-Decoupled Architecture Search, a framework that leverages ensemble theory to predict system-level performance from single-learner evaluation. We establish the Ensemble-Decoupled Theory with a sufficient condition for monotonic ensemble improvement under homogeneity assumptions: a candidate architecture pi yields lower ensemble error than the current baseline if rho(pi) < rho(pi_old) - (M / (M - 1)) * (Delta E(pi) / sigma^2(pi)), where Delta E, rho, and sigma^2 are estimable from lightweight dual-learner training. This decouples architecture search from full ensemble training, reducing per-candidate search cost from O(M) to O(1) while maintaining O(M) deployment cost only for validated winners. We unify solution strategies across pipeline continuity: (1) closed-form optimization for tractable continuous pi (exemplified by feature bagging in CTR prediction), (2) constrained differentiable optimization for intractable continuous pi, and (3) LLM-driven search with iterative monotonic acceptance for discrete pi. The framework reveals two orthogonal improvement mechanisms -- base diversity gain and accuracy gain -- providing actionable design principles for industrial-scale NAS. All theoretical derivations are rigorous with detailed proofs deferred to the appendix. Comprehensive empirical validation will be included in the journal extension of this work.
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
