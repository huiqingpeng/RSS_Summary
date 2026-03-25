---
title: "MIOFlow 2.0: A unified framework for inferring cellular stochastic dynamics from single cell and spatial transcriptomics data"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22564"
published: "2026-03-25"
fetched: "2026-03-26T07:15:18.056727"
---

Computer Science > Machine Learning
[Submitted on 23 Mar 2026]
Title:MIOFlow 2.0: A unified framework for inferring cellular stochastic dynamics from single cell and spatial transcriptomics data
View PDF HTML (experimental)Abstract:Understanding cellular trajectories via time-resolved single-cell transcriptomics is vital for studying development, regeneration, and disease. A key challenge is inferring continuous trajectories from discrete snapshots. Biological complexity stems from stochastic cell fate decisions, temporal proliferation changes, and spatial environmental influences. Current methods often use deterministic interpolations treating cells in isolation, failing to capture the probabilistic branching, population shifts, and niche-dependent signaling driving real biological processes.
We introduce Manifold Interpolating Optimal-Transport Flow (MIOFlow) 2.0. This framework learns biologically informed cellular trajectories by integrating manifold learning, optimal transport, and neural differential equations. It models three core processes: (1) stochasticity and branching via Neural Stochastic Differential Equations; (2) non-conservative population changes using a learned growth-rate model initialized with unbalanced optimal transport; and (3) environmental influence through a joint latent space unifying gene expression with spatial features like local cell type composition and signaling.
By operating in a PHATE-distance matching autoencoder latent space, MIOFlow 2.0 ensures trajectories respect the data's intrinsic geometry. Empirical comparisons show expressive trajectory learning via neural differential equations outperforms existing generative models, including simulation-free flow matching. Validated on synthetic datasets, embryoid body differentiation, and spatially resolved axolotl brain regeneration, MIOFlow 2.0 improves trajectory accuracy and reveals hidden drivers of cellular transitions, like specific signaling niches. MIOFlow 2.0 thus bridges single-cell and spatial transcriptomics to uncover tissue-scale trajectories.
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
