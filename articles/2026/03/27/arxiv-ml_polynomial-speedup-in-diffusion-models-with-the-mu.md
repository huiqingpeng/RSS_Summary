---
title: "Polynomial Speedup in Diffusion Models with the Multilevel Euler-Maruyama Method"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24594"
published: "2026-03-27"
fetched: "2026-03-28T07:12:01.231009"
---

Computer Science > Machine Learning
[Submitted on 25 Mar 2026]
Title:Polynomial Speedup in Diffusion Models with the Multilevel Euler-Maruyama Method
View PDF HTML (experimental)Abstract:We introduce the Multilevel Euler-Maruyama (ML-EM) method compute solutions of SDEs and ODEs using a range of approximators $f^1,\dots,f^k$ to the drift $f$ with increasing accuracy and computational cost, only requiring a few evaluations of the most accurate $f^k$ and many evaluations of the less costly $f^1,\dots,f^{k-1}$. If the drift lies in the so-called Harder than Monte Carlo (HTMC) regime, i.e. it requires $\epsilon^{-\gamma}$ compute to be $\epsilon$-approximated for some $\gamma>2$, then ML-EM $\epsilon$-approximates the solution of the SDE with $\epsilon^{-\gamma}$ compute, improving over the traditional EM rate of $\epsilon^{-\gamma-1}$. In other terms it allows us to solve the SDE at the same cost as a single evaluation of the drift. In the context of diffusion models, the different levels $f^{1},\dots,f^{k}$ are obtained by training UNets of increasing sizes, and ML-EM allows us to perform sampling with the equivalent of a single evaluation of the largest UNet. Our numerical experiments confirm our theory: we obtain up to fourfold speedups for image generation on the CelebA dataset downscaled to 64x64, where we measure a $\gamma\approx2.5$. Given that this is a polynomial speedup, we expect even stronger speedups in practical applications which involve orders of magnitude larger networks.
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
