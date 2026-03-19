---
title: "The Phasor Transformer: Resolving Attention Bottlenecks on the Unit Circle"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17433"
published: "2026-03-19"
fetched: "2026-03-19T12:11:40.070462"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:The Phasor Transformer: Resolving Attention Bottlenecks on the Unit Circle
View PDF HTML (experimental)Abstract:Transformer models have redefined sequence learning, yet dot-product self-attention introduces a quadratic token-mixing bottleneck for long-context time-series. We introduce the \textbf{Phasor Transformer} block, a phase-native alternative representing sequence states on the unit-circle manifold $S^1$. Each block combines lightweight trainable phase-shifts with parameter-free Discrete Fourier Transform (DFT) token coupling, achieving global $\mathcal{O}(N\log N)$ mixing without explicit attention maps. Stacking these blocks defines the \textbf{Large Phasor Model (LPM)}. We validate LPM on autoregressive time-series prediction over synthetic multi-frequency benchmarks. Operating with a highly compact parameter budget, LPM learns stable global dynamics and achieves competitive forecasting behavior compared to conventional self-attention baselines. Our results establish an explicit efficiency-performance frontier, demonstrating that large-model scaling for time-series can emerge from geometry-constrained phase computation with deterministic global coupling, offering a practical path toward scalable temporal modeling in oscillatory domains.
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
