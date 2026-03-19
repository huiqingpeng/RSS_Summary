---
title: "Cohomological Obstructions to Global Counterfactuals: A Sheaf-Theoretic Foundation for Generative Causal Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17384"
published: "2026-03-19"
fetched: "2026-03-19T12:10:58.132172"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:Cohomological Obstructions to Global Counterfactuals: A Sheaf-Theoretic Foundation for Generative Causal Models
View PDF HTML (experimental)Abstract:Current continuous generative models (e.g., Diffusion Models, Flow Matching) implicitly assume that locally consistent causal mechanisms naturally yield globally coherent counterfactuals. In this paper, we prove that this assumption fails fundamentally when the causal graph exhibits non-trivial homology (e.g., structural conflicts or hidden confounders). We formalize structural causal models as cellular sheaves over Wasserstein spaces, providing a strict algebraic topological definition of cohomological obstructions in measure spaces. To ensure computational tractability and avoid deterministic singularities (which we define as manifold tearing), we introduce entropic regularization and derive the Entropic Wasserstein Causal Sheaf Laplacian, a novel system of coupled non-linear Fokker-Planck equations. Crucially, we prove an entropic pullback lemma for the first variation of pushforward measures. By integrating this with the Implicit Function Theorem (IFT) on Sinkhorn optimality conditions, we establish a direct algorithmic bridge to automatic differentiation (VJP), achieving O(1)-memory reverse-mode gradients strictly independent of the iteration horizon. Empirically, our framework successfully leverages thermodynamic noise to navigate topological barriers ("entropic tunneling") in high-dimensional scRNA-seq counterfactuals. Finally, we invert this theoretical framework to introduce the Topological Causal Score, demonstrating that our Sheaf Laplacian acts as a highly sensitive algebraic detector for topology-aware causal discovery.
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
