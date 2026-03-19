---
title: "Vectorization of Verilog Designs and its Effects on Verification and Synthesis"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.17099"
published: "2026-03-19"
fetched: "2026-03-19T12:03:37.294487"
---

Computer Science > Programming Languages
[Submitted on 17 Mar 2026]
Title:Vectorization of Verilog Designs and its Effects on Verification and Synthesis
View PDF HTML (experimental)Abstract:Vectorization is a compiler optimization that replaces multiple operations on scalar values with a single operation on vector values. Although common in traditional compilers such as rustc, clang, and gcc, vectorization is not common in the Verilog ecosystem. This happens because, even though Verilog supports vector notation, the language provides no semantic guarantee that a vectorized signal behaves as a word-level entity: synthesis tools still resolve multiple individual assignments and a single vector assignment into the same set of parallel wire connections. However, vectorization brings important benefits in other domains. In particular, it reduces symbolic complexity even when the underlying hardware remains unchanged. Formal verification tools such as Cadence Jasper operates at the symbolic level: they reason about Boolean functions, state transitions, and equivalence classes, rather than about individual wires or gates. When these tools can treat a bus as a single symbolic entity, they scale more efficiently. This paper supports this observation by introducing a Verilog vectorizer. The vectorizer, built on top of the CIRCT compilation infrastructure, recognizes several vectorization patterns, including inverted assignments, assignments involving complex expressions, and inter-module assignments. It has been experimented with some Electronic design automation (EDA) tools, and for Jasper tool, it improves elaboration time by 28.12% and reduces memory consumption by 51.30% on 1,157 designs from the ChiBench collection.
Submission history
From: Fernando Quintao Pereira [view email][v1] Tue, 17 Mar 2026 19:39:56 UTC (1,067 KB)
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
