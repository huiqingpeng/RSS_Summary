---
title: "Spectral Edge Dynamics of Training Trajectories: Signal--Noise Geometry Across Scales"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15678"
published: "2026-03-18"
fetched: "2026-03-18T15:33:35.470994"
---

Computer Science > Machine Learning
[Submitted on 14 Mar 2026]
Title:Spectral Edge Dynamics of Training Trajectories: Signal--Noise Geometry Across Scales
View PDF HTML (experimental)Abstract:Despite hundreds of millions of parameters, transformer training trajectories evolve within only a few coherent directions. We introduce \emph{Spectral Edge Dynamics} (SED) to measure this structure: rolling-window SVD of parameter updates reveals a sharp boundary -- the \emph{spectral edge} -- between coherent optimization directions and stochastic noise, identified by the maximum consecutive singular value ratio $\sigma_k/\sigma_{k+1}$. Across a 51M-parameter TinyStories model (4~seeds) and GPT-2 124M under a distribution shift, the spectral edge exhibits a universal three-phase pattern (rise, plateau, collapse), signal rank adjusts with task complexity ($k^* = 2$ at 51M, $k^* = 3$ at 124M), and the directional coupling between spectral geometry and validation loss reverses with window size -- a \emph{lag flip} reflecting the timescale of trajectory integration. Johnson--Lindenstrauss projection to $d = 10W$ dimensions (e.g., $d = 100$ for $W = 10$) preserves the spectral gap within 5.7\%, making the framework applicable to models of arbitrary size. In companion work, the same spectral geometry provides early-warning signals of grokking -- predicting generalization 600--1{,}700 steps before it occurs across modular arithmetic, Dyck languages, and the SCAN benchmark.
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
