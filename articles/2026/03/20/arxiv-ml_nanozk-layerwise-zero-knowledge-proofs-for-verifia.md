---
title: "NANOZK: Layerwise Zero-Knowledge Proofs for Verifiable Large Language Model Inference"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18046"
published: "2026-03-20"
fetched: "2026-03-20T12:06:24.980842"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:NANOZK: Layerwise Zero-Knowledge Proofs for Verifiable Large Language Model Inference
View PDF HTML (experimental)Abstract:When users query proprietary LLM APIs, they receive outputs with no cryptographic assurance that the claimed model was actually used. Service providers could substitute cheaper models, apply aggressive quantization, or return cached responses - all undetectable by users paying premium prices for frontier capabilities. We present METHOD, a zero-knowledge proof system that makes LLM inference verifiable: users can cryptographically confirm that outputs correspond to the computation of a specific model.
Our approach exploits the fact that transformer inference naturally decomposes into independent layer computations, enabling a layerwise proof framework where each layer generates a constant-size proof regardless of model width. This decomposition sidesteps the scalability barrier facing monolithic approaches and enables parallel proving. We develop lookup table approximations for non-arithmetic operations (softmax, GELU, LayerNorm) that introduce zero measurable accuracy loss, and introduce Fisher information-guided verification for scenarios where proving all layers is impractical.
On transformer models up to d=128, METHOD generates constant-size layer proofs of 5.5KB (2.1KB attention + 3.5KB MLP) with 24 ms verification time. Compared to EZKL, METHOD achieves 70x smaller proofs and 5.7x faster proving time at d=128, while maintaining formal soundness guarantees (epsilon < 1e-37). Lookup approximations preserve model perplexity exactly, enabling verification without quality compromise.
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
