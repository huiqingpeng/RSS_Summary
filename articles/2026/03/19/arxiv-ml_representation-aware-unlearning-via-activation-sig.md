---
title: "Representation-Aware Unlearning via Activation Signatures: From Suppression to Knowledge-Signature Erasure"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2601.10566"
published: "2026-03-19"
fetched: "2026-03-19T14:17:50.123908"
---

Computer Science > Computation and Language
[Submitted on 15 Jan 2026 (v1), last revised 17 Mar 2026 (this version, v4)]
Title:Representation-Aware Unlearning via Activation Signatures: From Suppression to Knowledge-Signature Erasure
View PDF HTML (experimental)Abstract:Selective knowledge erasure from LLMs is critical for GDPR compliance and model safety, yet current unlearning methods conflate behavioral suppression with true knowledge removal, allowing latent capabilities to persist beneath surface-level refusals. In this work, we address this challenge by introducing Knowledge Immunization Framework (KIF), a representation-aware architecture that distinguishes genuine erasure from obfuscation by targeting internal activation signatures rather than surface outputs. Our approach combines dynamic suppression of subject-specific representations with parameter-efficient adaptation, enabling durable unlearning without full model retraining. KIF achieves near-oracle erasure (FQ approx 0.99 vs. 1.00) while preserving utility at oracle levels (MU = 0.62), effectively breaking the stability-erasure tradeoff that has constrained all prior work. We evaluate both standard foundation models (Llama and Mistral) and reasoning-prior models (Qwen and DeepSeek) across 3B to 14B parameters. Our observation shows that standard models exhibit scale-independent true erasure (<3% utility drift), while reasoning-prior models reveal fundamental architectural divergence. Our comprehensive dual-metric evaluation protocol, combining surface-level leakage with latent trace persistence, operationalizes the obfuscation - erasure distinction and enables the first systematic diagnosis of mechanism-level forgetting behavior across model families and scales.
Submission history
From: Syed Naveed Mahmood [view email][v1] Thu, 15 Jan 2026 16:28:14 UTC (1,743 KB)
[v2] Wed, 21 Jan 2026 06:55:54 UTC (1,743 KB)
[v3] Wed, 4 Feb 2026 15:22:32 UTC (1,743 KB)
[v4] Tue, 17 Mar 2026 19:23:39 UTC (686 KB)
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
