---
title: "Entropy trajectory shape predicts LLM reasoning reliability: A diagnostic study of uncertainty dynamics in chain-of-thought"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18940"
published: "2026-03-20"
fetched: "2026-03-20T13:17:56.431746"
---

Computer Science > Computation and Language
[Submitted on 19 Mar 2026]
Title:Entropy trajectory shape predicts LLM reasoning reliability: A diagnostic study of uncertainty dynamics in chain-of-thought
View PDF HTML (experimental)Abstract:Chain-of-thought (CoT) reasoning improves LLM accuracy, yet detecting failures cheaply remains elusive. We study whether the shape of uncertainty dynamics across reasoning steps--captured by sampling a few answer completions per step--predicts correctness.
We introduce entropy-trajectory monotonicity: a chain is monotone if its per-step answer-distribution entropy decreases at every step. On GSM8K (n=300) with Qwen2.5-7B-Instruct, monotone chains achieve 68.8% accuracy vs. 46.8% for non-monotone chains (+21.9 pp; Fisher's p=0.0005; OR=2.50). Critically, total entropy reduction is not predictive ($\rho$=-0.06, p=0.31), revealing a shape-over-magnitude dissociation: whether entropy decreases at every step matters, not how much. Violation count 0/1/2 gives 68.8%/50.8%/28.6% accuracy.
Token log-probability confidence worsens in calibration with step depth (ECE: 0.186->0.312), and monotonicity achieves +5.8 pp at 73.7% coverage, outperforming scalar baselines at approx 1,500 tokens/question--1/8 the cost of 40-chain self-consistency. Results replicate on Mistral-7B (n=300): monotone chains reach 72.3% vs. 37.6% (+34.7 pp; OR=4.33). Structural properties of uncertainty trajectories are thus more informative than aggregate measures.
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
