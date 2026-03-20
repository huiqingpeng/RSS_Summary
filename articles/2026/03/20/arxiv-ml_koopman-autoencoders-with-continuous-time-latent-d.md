---
title: "Koopman Autoencoders with Continuous-Time Latent Dynamics for Fluid Dynamics Forecasting"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2602.02832"
published: "2026-03-20"
fetched: "2026-03-20T14:10:29.289069"
---

Computer Science > Machine Learning
[Submitted on 2 Feb 2026 (v1), last revised 19 Mar 2026 (this version, v2)]
Title:Koopman Autoencoders with Continuous-Time Latent Dynamics for Fluid Dynamics Forecasting
View PDF HTML (experimental)Abstract:Learning surrogate models for time-dependent PDEs requires balancing expressivity, stability, and computational efficiency. While highly expressive generative models achieve strong short-term accuracy, they rely on autoregressive sampling procedures that are computationally expensive and prone to error accumulation over long horizons. We propose a continuous-time Koopman autoencoder in which latent dynamics are governed by a parameter-conditioned linear generator. This formulation enables exact latent evolution via matrix exponentiation, allowing predictions at arbitrary temporal resolutions without autoregressive rollouts. We evaluate our method on challenging fluid dynamics benchmarks and compare against autoregressive neural operators and diffusion-based models. We evaluate our method on challenging fluid dynamics benchmarks against autoregressive neural operators and diffusion-based models. Our results demonstrate that imposing a continuous-time linear structure in the latent space yields a highly favorable trade-off: it achieves massive computational efficiency and extreme long-horizon stability while remaining competitive in short-term generative accuracy.
Submission history
From: Rares Grozavescu [view email][v1] Mon, 2 Feb 2026 21:33:07 UTC (1,608 KB)
[v2] Thu, 19 Mar 2026 10:03:18 UTC (2,340 KB)
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
