---
title: "Neural Uncertainty Principle: A Unified View of Adversarial Fragility and LLM Hallucination"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19562"
published: "2026-03-23"
fetched: "2026-03-24T07:19:32.895682"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:Neural Uncertainty Principle: A Unified View of Adversarial Fragility and LLM Hallucination
View PDF HTML (experimental)Abstract:Adversarial vulnerability in vision and hallucination in large language models are conventionally viewed as separate problems, each addressed with modality-specific patches. This study first reveals that they share a common geometric origin: the input and its loss gradient are conjugate observables subject to an irreducible uncertainty bound. Formalizing a Neural Uncertainty Principle (NUP) under a loss-induced state, we find that in near-bound regimes, further compression must be accompanied by increased sensitivity dispersion (adversarial fragility), while weak prompt-gradient coupling leaves generation under-constrained (hallucination). Crucially, this bound is modulated by an input-gradient correlation channel, captured by a specifically designed single-backward probe. In vision, masking highly coupled components improves robustness without costly adversarial training; in language, the same prefill-stage probe detects hallucination risk before generating any answer tokens. NUP thus turns two seemingly separate failure taxonomies into a shared uncertainty-budget view and provides a principled lens for reliability analysis. Guided by this NUP theory, we propose ConjMask (masking high-contribution input components) and LogitReg (logit-side regularization) to improve robustness without adversarial training, and use the probe as a decoding-free risk signal for LLMs, enabling hallucination detection and prompt selection. NUP thus provides a unified, practical framework for diagnosing and mitigating boundary anomalies across perception and generation tasks.
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
