---
title: "SymCircuit: Bayesian Structure Inference for Tractable Probabilistic Circuits via Entropy-Regularized Reinforcement Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20392"
published: "2026-03-24"
fetched: "2026-03-25T07:08:34.109661"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:SymCircuit: Bayesian Structure Inference for Tractable Probabilistic Circuits via Entropy-Regularized Reinforcement Learning
View PDFAbstract:Probabilistic circuit (PC) structure learning is hampered by greedy algorithms that make irreversible, locally optimal decisions. We propose SymCircuit, which replaces greedy search with a learned generative policy trained via entropy-regularized reinforcement learning. Instantiating the RL-as-inference framework in the PC domain, we show the optimal policy is a tempered Bayesian posterior, recovering the exact posterior when the regularization temperature is set inversely proportional to the dataset size. The policy is implemented as SymFormer, a grammar-constrained autoregressive Transformer with tree-relative self-attention that guarantees valid circuits at every generation step. We introduce option-level REINFORCE, restricting gradient updates to structural decisions rather than all tokens, yielding an SNR (signal to noise ratio) improvement and >10 times sample efficiency gain on the NLTCS dataset. A three-layer uncertainty decomposition (structural via model averaging, parametric via the delta method, leaf via conjugate Dirichlet-Categorical propagation) is grounded in the multilinear polynomial structure of PC outputs. On NLTCS, SymCircuit closes 93% of the gap to LearnSPN; preliminary results on Plants (69 variables) suggest scalability.
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
