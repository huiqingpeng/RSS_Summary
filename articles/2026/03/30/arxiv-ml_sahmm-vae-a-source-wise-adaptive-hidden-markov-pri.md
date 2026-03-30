---
title: "SAHMM-VAE: A Source-Wise Adaptive Hidden Markov Prior Variational Autoencoder for Unsupervised Blind Source Separation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.25776"
published: "2026-03-30"
fetched: "2026-03-31T07:27:00.210165"
---

Statistics > Machine Learning
[Submitted on 26 Mar 2026]
Title:SAHMM-VAE: A Source-Wise Adaptive Hidden Markov Prior Variational Autoencoder for Unsupervised Blind Source Separation
View PDF HTML (experimental)Abstract:We propose SAHMM-VAE, a source-wise adaptive Hidden Markov prior variational autoencoder for unsupervised blind source separation. Instead of treating the latent prior as a single generic regularizer, the proposed framework assigns each latent dimension its own adaptive regime-switching prior, so that different latent dimensions are pulled toward different source-specific temporal organizations during training. Under this formulation, source separation is not implemented as an external post-processing step; it is embedded directly into variational learning itself. The encoder, decoder, posterior parameters, and source-wise prior parameters are optimized jointly, where the encoder progressively learns an inference map that behaves like an approximate inverse of the mixing transformation, while the decoder plays the role of the generative mixing model. Through this coupled optimization, the gradual alignment between posterior source trajectories and heterogeneous HMM priors becomes the mechanism through which different latent dimensions separate into different source components. To instantiate this idea, we develop three branches within one common framework: a Gaussian-emission HMM prior, a Markov-switching autoregressive HMM prior, and an HMM state-flow prior with state-wise autoregressive flow transformations. Experiments show that the proposed framework achieves unsupervised source recovery while also learning meaningful source-wise switching structures. More broadly, the method extends our structured-prior VAE line from smooth, mixture-based, and flow-based latent priors to adaptive switching priors, and provides a useful basis for future work on interpretable and potentially identifiable latent source modeling.
Submission history
From: Yuan-Hao Wei Dr. [view email][v1] Thu, 26 Mar 2026 13:08:16 UTC (2,395 KB)
Current browse context:
stat.ML
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
