---
title: "Sparse-by-Design Cross-Modality Prediction: L0-Gated Representations for Reliable and Efficient Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26801"
published: "2026-03-31"
fetched: "2026-04-01T07:18:42.794972"
---

Computer Science > Machine Learning
[Submitted on 26 Mar 2026]
Title:Sparse-by-Design Cross-Modality Prediction: L0-Gated Representations for Reliable and Efficient Learning
View PDF HTML (experimental)Abstract:Predictive systems increasingly span heterogeneous modalities such as graphs, language, and tabular records, but sparsity and efficiency remain modality-specific (graph edge or neighborhood sparsification, Transformer head or layer pruning, and separate tabular feature-selection pipelines). This fragmentation makes results hard to compare, complicates deployment, and weakens reliability analysis across end-to-end KDD pipelines. A unified sparsification primitive would make accuracy-efficiency trade-offs comparable across modalities and enable controlled reliability analysis under representation compression. We ask whether a single representation-level mechanism can yield comparable accuracy-efficiency trade-offs across modalities while preserving or improving probability calibration. We propose L0-Gated Cross-Modality Learning (L0GM), a modality-agnostic, feature-wise hard-concrete gating framework that enforces L0-style sparsity directly on learned representations. L0GM attaches hard-concrete stochastic gates to each modality's classifier-facing interface: node embeddings (GNNs), pooled sequence embeddings such as CLS (Transformers), and learned tabular embedding vectors (tabular models). This yields end-to-end trainable sparsification with an explicit control knob for the active feature fraction. To stabilize optimization and make trade-offs interpretable, we introduce an L0-annealing schedule that induces clear accuracy-sparsity Pareto frontiers. Across three public benchmarks (ogbn-products, Adult, IMDB), L0GM achieves competitive predictive performance while activating fewer representation dimensions, and it reduces Expected Calibration Error (ECE) in our evaluation. Overall, L0GM establishes a modality-agnostic, reproducible sparsification primitive that supports comparable accuracy, efficiency, and calibration trade-off analysis across heterogeneous modalities.
Submission history
From: Filippo Cenacchi [view email][v1] Thu, 26 Mar 2026 03:33:42 UTC (8,565 KB)
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
