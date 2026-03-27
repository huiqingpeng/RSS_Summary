---
title: "TAMI-MPC:Trusted Acceleration of Minimal-Interaction MPC for Efficient Nonlinear Inference"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.24861"
published: "2026-03-27"
fetched: "2026-03-28T07:06:37.957468"
---

Computer Science > Hardware Architecture
[Submitted on 25 Mar 2026]
Title:TAMI-MPC:Trusted Acceleration of Minimal-Interaction MPC for Efficient Nonlinear Inference
View PDF HTML (experimental)Abstract:Secure multi-party computation (MPC) offers a practical foundation for privacy-preserving machine learning at the edge. However, current MPC systems rely heavily on communication and computation-intensive primitives-such as secure comparison for nonlinear inference, which are often impractical on resource-constrained platforms. To enable real-time inference under a resource-constrained platform, we introduce a Trusted Acceleration of Minimal-Interaction MPC framework, TAMI-MPC, for nonlinear evaluation. Specifically, we reduce communication cost by redesigning the core primitives, leaf comparison, and tree merge, reducing the interactive round from log(n) to just 1 per operation. Furthermore, unlike prior work that heavily relies on oblivious transfer (OT), a well-known computational bottleneck, we leverage synchronized seeds inside the TEE to eliminate OT for the vast majority of our designs, along with a correlated-randomness reuse technique that keeps new designs computationally lightweight. To fully realize the potential, we design a specialized accelerator that restructures the dataflow across stages to enable continuous, fine-grained streaming and high parallelism, reducing memory overhead. Our design achieves up to 4.86x speedup on ResNet-50 inference, compared with state-of-the-art CNN frameworks, and achieves up to 7.44x speedup on BERT-base inference, compared with state-of-the-art LLM frameworks.
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
