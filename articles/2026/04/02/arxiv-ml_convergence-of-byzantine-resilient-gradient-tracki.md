---
title: "Convergence of Byzantine-Resilient Gradient Tracking via Probabilistic Edge Dropout"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00449"
published: "2026-04-02"
fetched: "2026-04-03T07:21:26.742609"
---

Computer Science > Machine Learning
[Submitted on 1 Apr 2026]
Title:Convergence of Byzantine-Resilient Gradient Tracking via Probabilistic Edge Dropout
View PDF HTML (experimental)Abstract:We study distributed optimization over networks with Byzantine agents that may send arbitrary adversarial messages. We propose \emph{Gradient Tracking with Probabilistic Edge Dropout} (GT-PD), a stochastic gradient tracking method that preserves the convergence properties of gradient tracking under adversarial communication. GT-PD combines two complementary defense layers: a universal self-centered projection that clips each incoming message to a ball of radius $\tau$ around the receiving agent, and a fully decentralized probabilistic dropout rule driven by a dual-metric trust score in the decision and tracking channels. This design bounds adversarial perturbations while preserving the doubly stochastic mixing structure, a property often lost under robust aggregation in decentralized settings. Under complete Byzantine isolation ($p_b=0$), GT-PD converges linearly to a neighborhood determined solely by stochastic gradient variance. For partial isolation ($p_b>0$), we introduce \emph{Gradient Tracking with Probabilistic Edge Dropout and Leaky Integration} (GT-PD-L), which uses a leaky integrator to control the accumulation of tracking errors caused by persistent perturbations and achieves linear convergence to a bounded neighborhood determined by the stochastic variance and the clipping-to-leak ratio. We further show that under two-tier dropout with $p_h=1$, isolating Byzantine agents introduces no additional variance into the honest consensus dynamics. Experiments on MNIST under Sign Flip, ALIE, and Inner Product Manipulation attacks show that GT-PD-L outperforms coordinate-wise trimmed mean by up to 4.3 percentage points under stealth attacks.
Submission history
From: Amirhossein Dezhboro [view email][v1] Wed, 1 Apr 2026 03:55:42 UTC (2,639 KB)
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
