---
title: "Temporal Memory for Resource-Constrained Agents: Continual Learning via Stochastic Compress-Add-Smooth"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00067"
published: "2026-04-02"
fetched: "2026-04-03T07:16:36.336924"
---

Computer Science > Machine Learning
[Submitted on 31 Mar 2026]
Title:Temporal Memory for Resource-Constrained Agents: Continual Learning via Stochastic Compress-Add-Smooth
View PDF HTML (experimental)Abstract:An agent that operates sequentially must incorporate new experience without forgetting old experience, under a fixed memory budget. We propose a framework in which memory is not a parameter vector but a stochastic process: a Bridge Diffusion on a replay interval $[0,1]$, whose terminal marginal encodes the present and whose intermediate marginals encode the past. New experience is incorporated via a three-step \emph{Compress--Add--Smooth} (CAS) recursion. We test the framework on the class of models with marginal probability densities modeled via Gaussian mixtures of fixed number of components~$K$ in $d$ dimensions; temporal complexity is controlled by a fixed number~$L$ of piecewise-linear protocol segments whose nodes store Gaussian-mixture states. The entire recursion costs $O(LKd^2)$ flops per day -- no backpropagation, no stored data, no neural networks -- making it viable for controller-light hardware.
Forgetting in this framework arises not from parameter interference but from lossy temporal compression: the re-approximation of a finer protocol by a coarser one under a fixed segment budget. We find that the retention half-life scales linearly as $a_{1/2}\approx c\,L$ with a constant $c>1$ that depends on the dynamics but not on the mixture complexity~$K$, the dimension~$d$, or the geometry of the target family. The constant~$c$ admits an information-theoretic interpretation analogous to the Shannon channel capacity. The stochastic process underlying the bridge provides temporally coherent ``movie'' replay -- compressed narratives of the agent's history, demonstrated visually on an MNIST latent-space illustration. The framework provides a fully analytical ``Ising model'' of continual learning in which the mechanism, rate, and form of forgetting can be studied with mathematical precision.
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
