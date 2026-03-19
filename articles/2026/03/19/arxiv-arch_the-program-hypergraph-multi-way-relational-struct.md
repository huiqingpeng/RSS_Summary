---
title: "The Program Hypergraph: Multi-Way Relational Structure for Geometric Algebra, Spatial Compute, and Physics-Aware Compilation"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.17627"
published: "2026-03-19"
fetched: "2026-03-19T12:03:59.836378"
---

Computer Science > Programming Languages
[Submitted on 18 Mar 2026]
Title:The Program Hypergraph: Multi-Way Relational Structure for Geometric Algebra, Spatial Compute, and Physics-Aware Compilation
View PDF HTML (experimental)Abstract:The Program Semantic Graph (PSG) introduced in prior work on Dimensional Type Systems and Deterministic Memory Management encodes compilation-relevant properties as binary edge relations between computation nodes. This representation is adequate for scalar and tensor computations, but becomes structurally insufficient for two classes of problems central to heterogeneous compute: tile co-location and routing constraints in spatial dataflow architectures, which are inherently multi-way; and geometric algebra computation, where graded multi-way products cannot be faithfully represented as sequences of binary operations without loss of algebraic identity. This paper introduces the Program Hypergraph (PHG) as a principled generalization of the PSG that promotes binary edges to hyperedges of arbitrary arity. We demonstrate that grade in Clifford algebra is a natural dimension axis within the existing DTS abelian group framework, that grade inference derives geometric product sparsity eliminating the primary performance objection to Clifford algebra neural networks without manual specialization, and that the k-simplex structure of mesh topology is a direct instance of the hyperedge formalism. We assess the existing geometric algebra library ecosystem, identify the consistent type-theoretic gap that no current system addresses, and show that the PHG closes it within the Fidelity compilation framework. The result is a compilation framework where geometric correctness, memory placement, numerical precision selection, and hardware partitioning are jointly derivable from a single graph structure exposed as interactive design-time feedback.
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
