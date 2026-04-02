---
title: "RePart: Efficient Hypergraph Partitioning with Logic Replication Optimization for Multi-FPGA System"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2604.00780"
published: "2026-04-02"
fetched: "2026-04-03T07:14:45.301477"
---

Computer Science > Hardware Architecture
[Submitted on 1 Apr 2026]
Title:RePart: Efficient Hypergraph Partitioning with Logic Replication Optimization for Multi-FPGA System
View PDF HTML (experimental)Abstract:Multi-FPGA systems (MFS) are widely adopted for VLSI emulation and rapid prototyping. In an MFS, FPGAs connect only to a limited number of neighbors through bandwidth-constrained links, so inter-FPGA communication cost depends on network topology. This setting exposes two fundamental limitations of existing MFS-aware partitioning methods: conventional hypergraph partitioners focus solely on cut size and ignore topological structure, and they leave substantial FPGA resources unused due to conservative balance margins. We present RePart, a fully customized multilevel hypergraph partitioning framework for MFS that integrates logic replication with topology-aware optimization. RePart introduces three coordinated innovations across the multilevel pipeline: FPGA-aware dynamic coarsening, heat-value guided assignment, and replication-deletion supported refinement. Extensive experiments on the Titan23 and EDA Elite Challenge Contest benchmarks show that RePart reduces total hop distance by 52.3% on average over state-of-the-art hypergraph partitioners with an 11.1x speedup, and outperforms the EDA Elite Challenge winners. Code is available at: this https URL.
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
