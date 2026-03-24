---
title: "From Data to Laws: Neural Discovery of Conservation Laws Without False Positives"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20474"
published: "2026-03-24"
fetched: "2026-03-25T07:10:09.733736"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:From Data to Laws: Neural Discovery of Conservation Laws Without False Positives
View PDF HTML (experimental)Abstract:Conservation laws are fundamental to understanding dynamical systems, but discovering them from data remains challenging due to parameter variation, non-polynomial invariants, local minima, and false positives on chaotic systems. We introduce NGCG, a neural-symbolic pipeline that decouples dynamics learning from invariant discovery and systematically addresses these challenges. A multi-restart variance minimiser learns a near-constant latent representation; system-specific symbolic extraction (polynomial Lasso, log-basis Lasso, explicit PDE candidates, and PySR) yields closed-form expressions; a strict constancy gate and diversity filter eliminate spurious laws. On a benchmark of nine diverse systems including Hamiltonian and dissipative ODEs, chaos, and PDEs, NGCG achieves consistent discovery (DR=1.0, FDR=0.0, F1=1.0) on all four systems with true conservation laws, with constancy two to three orders of magnitude lower than the best baseline. It is the only method that succeeds on the Lotka--Volterra system, and it correctly outputs no law on all five systems without invariants. Extensive experiments demonstrate robustness to noise ($\sigma = 0.1$), sample efficiency (50--100 trajectories), insensitivity to hyperparameters, and runtime under one minute per system. A Pareto analysis shows that the method provides a range of candidate expressions, allowing users to trade complexity for constancy. NGCG achieves strong performance relative to prior methods for data-driven conservation-law discovery, combining high accuracy with interpretability.
Current browse context:
cs.LG
Change to browse by:
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
