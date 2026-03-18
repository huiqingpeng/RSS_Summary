---
title: "FEAT: A Linear-Complexity Foundation Model for Extremely Large Structured Data"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16513"
published: "2026-03-18"
fetched: "2026-03-18T15:44:41.818540"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:FEAT: A Linear-Complexity Foundation Model for Extremely Large Structured Data
View PDF HTML (experimental)Abstract:Structured data is foundational to healthcare, finance, e-commerce, and scientific data management. Large structured-data models (LDMs) extend the foundation model paradigm to unify heterogeneous datasets for tasks such as classification, regression, and decision support. However, existing LDMs face major limitations. First, most rely on sample-wise self-attention, whose O(N^2) complexity limits the sample count. Second, linear sequence models often degrade representations due to hidden-state compression and artificial causal bias. Third, synthetic-only pre-training often fails to match real-world distributions. We propose FEAT, a linear-complexity foundation model for extremely large structured data. FEAT introduces a multi-layer dual-axis architecture that replaces quadratic attention with hybrid linear encoding. The architecture combines adaptive-fusion bi-Mamba-2 (AFBM) for local sample dependencies and convolutional gated linear attention (Conv-GLA) for global memory. This design enables linear-complexity cross-sample modeling while preserving expressive representations. To improve robustness, FEAT adopts a hybrid structural causal model pipeline and a stable reconstruction objective. Experiments on 11 real-world datasets show that FEAT consistently outperforms baselines in zero-shot performance, while scaling linearly and achieving up to 40x faster inference.
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
