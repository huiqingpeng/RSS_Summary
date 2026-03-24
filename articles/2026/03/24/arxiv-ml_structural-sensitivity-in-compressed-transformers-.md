---
title: "Structural Sensitivity in Compressed Transformers: Error Propagation, Lyapunov Stability, and Formally Verified Bounds"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20991"
published: "2026-03-24"
fetched: "2026-03-25T07:17:15.940951"
---

Computer Science > Machine Learning
[Submitted on 22 Mar 2026]
Title:Structural Sensitivity in Compressed Transformers: Error Propagation, Lyapunov Stability, and Formally Verified Bounds
View PDF HTML (experimental)Abstract:A single matrix out of 468 in GPT-2 Small can increase perplexity by 20,000x when compressed, revealing that transformer compression sensitivity spans five orders of magnitude. We map this sensitivity landscape across five architectures (117M-8B parameters), finding a consistent hierarchy: early-layer MLP up-projections are catastrophically sensitive while value projections compress nearly for free. This hierarchy is stable across compression levels, evaluation scales (2K-51K tokens), and datasets (WikiText-103, C4). Using Lyapunov stability theory, we show that residual connections contract compression errors by growing the hidden state faster than the error. Error contraction is necessary but not sufficient for compression tolerance: architecture-specific redundancy plays an equally important role, as demonstrated by the hybrid LFM2-2.6B degrading only 7x despite higher amplification than the fully-contracting GPT-2 Small (120x). Ten machine-checked Lean 4 theorems formalize per-matrix error bounds with no sorry markers; all bounds produce zero violations across 14,040+ configurations. We validate with downstream task evaluation (HellaSwag, ARC-Easy, Winogrande), activation-aware pruning on two architectures, and a Compression Fragility Index that rank-orders model robustness.
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
