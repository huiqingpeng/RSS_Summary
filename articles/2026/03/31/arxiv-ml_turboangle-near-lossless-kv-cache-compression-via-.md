---
title: "TurboAngle: Near-Lossless KV Cache Compression via Uniform Angle Quantization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.27467"
published: "2026-03-31"
fetched: "2026-04-01T07:24:30.197698"
---

Computer Science > Machine Learning
[Submitted on 29 Mar 2026]
Title:TurboAngle: Near-Lossless KV Cache Compression via Uniform Angle Quantization
View PDF HTML (experimental)Abstract:We compress KV cache entries by quantizing angles in the Fast Walsh-Hadamard domain, where a random diagonal rotation makes consecutive element pairs approximately uniformly distributed on the unit circle. We extend this angular quantizer with per-layer early-boost, which independently configures K and V codebook sizes at each layer, allocating higher precision to a model-specific subset of critical layers. Across seven models (1B to 7B parameters), per-layer early-boost achieves lossless compression on four models and near-lossless quality on six of seven, at 3.28 to 3.67 angle bits per element. Asymmetric norm quantization (8-bit for keys, 4-bit log-space for values) yields 6.56 total bits per element on Mistral-7B with perplexity degradation of +0.0014 and no calibration data. A layer-group sensitivity analysis reveals model-specific bottleneck patterns, including K-dominated versus V-dominated layers and negative-transfer layers where increased precision degrades quality.
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
