---
title: "UniFluids: Unified Neural Operator Learning with Conditional Flow-matching"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22309"
published: "2026-03-25"
fetched: "2026-03-26T07:09:36.886111"
---

Computer Science > Machine Learning
[Submitted on 19 Mar 2026]
Title:UniFluids: Unified Neural Operator Learning with Conditional Flow-matching
View PDF HTML (experimental)Abstract:Partial differential equation (PDE) simulation holds extensive significance in scientific research. Currently, the integration of deep neural networks to learn solution operators of PDEs has introduced great potential. In this paper, we present UniFluids, a conditional flow-matching framework that harnesses the scalability of diffusion Transformer to unify learning of solution operators across diverse PDEs with varying dimensionality and physical variables. Unlike the autoregressive PDE foundation models, UniFluids adopts flow-matching to achieve parallel sequence generation, making it the first such approach for unified operator learning. Specifically, the introduction of a unified four-dimensional spatiotemporal representation for the heterogeneous PDE datasets enables joint training and conditional encoding. Furthermore, we find the effective dimension of the PDE dataset is much lower than its patch dimension. We thus employ $x$-prediction in the flow-matching operator learning, which is verified to significantly improve prediction accuracy. We conduct a large-scale evaluation of UniFluids on several PDE datasets covering spatial dimensions 1D, 2D and 3D. Experimental results show that UniFluids achieves strong prediction accuracy and demonstrates good scalability and cross-scenario generalization capability. The code will be released later.
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
