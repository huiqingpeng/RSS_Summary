---
title: "I Know What I Don't Know: Latent Posterior Factor Models for Multi-Evidence Probabilistic Reasoning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15670"
published: "2026-03-18"
fetched: "2026-03-18T16:05:59.146475"
---

Computer Science > Artificial Intelligence
[Submitted on 13 Mar 2026]
Title:I Know What I Don't Know: Latent Posterior Factor Models for Multi-Evidence Probabilistic Reasoning
View PDF HTML (experimental)Abstract:Real-world decision-making, from tax compliance assessment to medical diagnosis, requires aggregating multiple noisy and potentially contradictory evidence sources. Existing approaches either lack explicit uncertainty quantification (neural aggregation methods) or rely on manually engineered discrete predicates (probabilistic logic frameworks), limiting scalability to unstructured data.
We introduce Latent Posterior Factors (LPF), a framework that transforms Variational Autoencoder (VAE) latent posteriors into soft likelihood factors for Sum-Product Network (SPN) inference, enabling tractable probabilistic reasoning over unstructured evidence while preserving calibrated uncertainty estimates. We instantiate LPF as LPF-SPN (structured factor-based inference) and LPF-Learned (end-to-end learned aggregation), enabling a principled comparison between explicit probabilistic reasoning and learned aggregation under a shared uncertainty representation.
Across eight domains (seven synthetic and the FEVER benchmark), LPF-SPN achieves high accuracy (up to 97.8%), low calibration error (ECE 1.4%), and strong probabilistic fit, substantially outperforming evidential deep learning, LLMs and graph-based baselines over 15 random seeds.
Contributions: (1) A framework bridging latent uncertainty representations with structured probabilistic reasoning. (2) Dual architectures enabling controlled comparison of reasoning paradigms. (3) Reproducible training methodology with seed selection. (4) Evaluation against EDL, BERT, R-GCN, and large language model baselines. (5) Cross-domain validation. (6) Formal guarantees in a companion paper.
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
