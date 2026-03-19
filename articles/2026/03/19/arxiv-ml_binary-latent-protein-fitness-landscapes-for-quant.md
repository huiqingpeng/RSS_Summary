---
title: "Binary Latent Protein Fitness Landscapes for Quantum Annealing Optimization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17247"
published: "2026-03-19"
fetched: "2026-03-19T12:09:16.299782"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:Binary Latent Protein Fitness Landscapes for Quantum Annealing Optimization
View PDF HTML (experimental)Abstract:We propose Q-BIOLAT, a framework for modeling and optimizing protein fitness landscapes in binary latent spaces. Starting from protein sequences, we leverage pretrained protein language models to obtain continuous embeddings, which are then transformed into compact binary latent representations. In this space, protein fitness is approximated using a quadratic unconstrained binary optimization (QUBO) model, enabling efficient combinatorial search via classical heuristics such as simulated annealing and genetic algorithms.
On the ProteinGym benchmark, we demonstrate that Q-BIOLAT captures meaningful structure in protein fitness landscapes and enables the identification of high-fitness variants. Despite using a simple binarization scheme, our method consistently retrieves sequences whose nearest neighbors lie within the top fraction of the training fitness distribution, particularly under the strongest configurations. We further show that different optimization strategies exhibit distinct behaviors, with evolutionary search performing better in higher-dimensional latent spaces and local search remaining competitive in preserving realistic sequences.
Beyond its empirical performance, Q-BIOLAT provides a natural bridge between protein representation learning and combinatorial optimization. By formulating protein fitness as a QUBO problem, our framework is directly compatible with emerging quantum annealing hardware, opening new directions for quantum-assisted protein engineering.
Our implementation is publicly available at: this https URL
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
