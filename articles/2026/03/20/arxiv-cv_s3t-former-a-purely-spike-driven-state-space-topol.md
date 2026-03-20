---
title: "S3T-Former: A Purely Spike-Driven State-Space Topology Transformer for Skeleton Action Recognition"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18062"
published: "2026-03-20"
fetched: "2026-03-20T15:05:28.312171"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:S3T-Former: A Purely Spike-Driven State-Space Topology Transformer for Skeleton Action Recognition
View PDF HTML (experimental)Abstract:Skeleton-based action recognition is crucial for multimedia applications but heavily relies on power-hungry Artificial Neural Networks (ANNs), limiting their deployment on resource-constrained edge devices. Spiking Neural Networks (SNNs) provide an energy-efficient alternative; however, existing spiking models for skeleton data often compromise the intrinsic sparsity of SNNs by resorting to dense matrix aggregations, heavy multimodal fusion modules, or non-sparse frequency domain transformations. Furthermore, they severely suffer from the short-term amnesia of spiking neurons. In this paper, we propose the Spiking State-Space Topology Transformer (S3T-Former), which, to the best of our knowledge, is the first purely spike-driven Transformer architecture specifically designed for energy-efficient skeleton action recognition. Rather than relying on heavy fusion overhead, we formulate a Multi-Stream Anatomical Spiking Embedding (M-ASE) that acts as a generalized kinematic differential operator, elegantly transforming multimodal skeleton features into heterogeneous, highly sparse event streams. To achieve true topological and temporal sparsity, we introduce Lateral Spiking Topology Routing (LSTR) for on-demand conditional spike propagation, and a Spiking State-Space (S3) Engine to systematically capture long-range temporal dynamics without non-sparse spectral workarounds. Extensive experiments on multiple large-scale datasets demonstrate that S3T-Former achieves highly competitive accuracy while theoretically reducing energy consumption compared to classic ANNs, establishing a new state-of-the-art for energy-efficient neuromorphic action recognition.
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
