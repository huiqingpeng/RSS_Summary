---
title: "Is One Token All It Takes? Graph Pooling Tokens for LLM-based GraphQA"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00342"
published: "2026-04-02"
fetched: "2026-04-03T07:20:35.686183"
---

Computer Science > Machine Learning
[Submitted on 1 Apr 2026]
Title:Is One Token All It Takes? Graph Pooling Tokens for LLM-based GraphQA
View PDF HTML (experimental)Abstract:The integration of Graph Neural Networks (GNNs) with Large Language Models (LLMs) has emerged as a promising paradigm for Graph Question Answering (GraphQA). However, effective methods for encoding complex structural information into the LLM's latent space remain an open challenge. Current state-of-the-art architectures, such as G-Retriever, typically rely on standard GNNs and aggressive mean pooling to compress entire graph substructures into a single token, creating a severe information bottleneck. This work mitigates this bottleneck by investigating two orthogonal strategies: (1) increasing the bandwidth of the graph-to-LLM interface via multi-token pooling, and (2) enhancing the semantic quality of the graph encoder via global attention mechanisms. We evaluate a suite of hierarchical pruning and clustering-based pooling operators including Top-k, SAGPool, DiffPool, MinCutPool, and Virtual Node Pooling (VNPool) to project graph data into multiple learnable tokens. Empirically, we demonstrate that while pooling introduces significant instability during soft prompt tuning, the application of Low-Rank Adaptation (LoRA) effectively stabilizes specific hierarchical projections (notably VNPool and pruning methods), though dense clustering operators remain challenging. This stabilization allows compressed representations to rival full-graph baselines (achieving ~73% Hit@1 on WebQSP). Conceptually, we demonstrate that a Graph Transformer with VNPool implementation functions structurally as a single-layer Perceiver IO encoder. Finally, we adapt the FandE (Features and Edges) Score to the generative GraphQA domain. Our analysis reveals that the GraphQA benchmark suffers from representational saturation, where target answers are often highly correlated with isolated node features. The implementation is available at this https URL
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
