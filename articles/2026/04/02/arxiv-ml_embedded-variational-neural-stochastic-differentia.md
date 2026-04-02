---
title: "Embedded Variational Neural Stochastic Differential Equations for Learning Heterogeneous Dynamics"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00669"
published: "2026-04-02"
fetched: "2026-04-03T07:23:24.226033"
---

Computer Science > Machine Learning
[Submitted on 1 Apr 2026]
Title:Embedded Variational Neural Stochastic Differential Equations for Learning Heterogeneous Dynamics
View PDF HTML (experimental)Abstract:This study examines the challenges of modeling complex and noisy data related to socioeconomic factors over time, with a focus on data from various districts in Odisha, India. Traditional time-series models struggle to capture both trends and variations together in this type of data. To tackle this, a Variational Neural Stochastic Differential Equation (V-NSDE) model is designed that combines the expressive dynamics of Neural SDEs with the generative capabilities of Variational Autoencoders (VAEs). This model uses an encoder and a decoder. The encoder takes the initial observations and district embeddings and translates them into a Gaussian distribution, which determines the mean and log-variance of the first latent state. Then the obtained latent state initiates the Neural SDE, which utilize neural networks to determine the drift and diffusion functions that govern continuous-time latent dynamics. These governing functions depend on the time index, latent state, and district embedding, which help the model learn the unique characteristics specific to each district. After that, using a probabilistic decoder, the observations are reconstructed from the latent trajectory. The decoder outputs a mean and log-variance for each time step, which follows the Gaussian likelihood. The Evidence Lower Bound (ELBO) training loss improves by adding a KL-divergence regularization term to the negative log-likelihood (nll). The obtained results demonstrate the effective learning of V-NSDE in recognizing complex patterns over time, yielding realistic outcomes that include clear trends and random fluctuations across different areas.
Submission history
From: Snehashish Chakraverty [view email][v1] Wed, 1 Apr 2026 09:15:04 UTC (2,672 KB)
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
