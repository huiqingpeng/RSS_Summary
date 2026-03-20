---
title: "Transfer Learning for Contextual Joint Assortment-Pricing under Cross-Market Heterogeneity"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18114"
published: "2026-03-20"
fetched: "2026-03-20T13:09:13.182539"
---

Statistics > Methodology
[Submitted on 18 Mar 2026]
Title:Transfer Learning for Contextual Joint Assortment-Pricing under Cross-Market Heterogeneity
View PDF HTML (experimental)Abstract:We study transfer learning for contextual joint assortment-pricing under a multinomial logit choice model with bandit feedback. A seller operates across multiple related markets and observes only posted prices and realized purchases. While data from source markets can accelerate learning in a target market, cross-market differences in customer preferences may introduce systematic bias if pooled indiscriminately.
We model heterogeneity through a structured utility shift, where markets share a common contextual utility structure but differ along a sparse set of latent preference coordinates. Building on this, we develop Transfer Joint Assortment-Pricing (TJAP), a bias-aware framework that combines aggregate-then-debias estimation with a UCB-style policy. TJAP constructs two-radius confidence bounds that separately capture statistical uncertainty and transfer-induced bias, uniformly over continuous prices.
We establish matching minimax regret bounds of order $\tilde{O}\!\left(d\sqrt{\frac{T}{1+H}} + s_0\sqrt{T}\right),$revealing a transparent variance-bias tradeoff: transfer accelerates learning along shared preference directions, while heterogeneous components impose an irreducible adaptation cost. Numerical experiments corroborate the theory, showing that TJAP outperforms both target-only learning and naive pooling while remaining robust to cross-market differences.
Current browse context:
stat.ME
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
