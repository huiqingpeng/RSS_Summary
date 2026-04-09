---
title: "Instance-Adaptive Parametrization for Amortized Variational Inference"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.06796"
published: "2026-04-09"
fetched: "2026-04-10T07:05:07.435507"
---

Computer Science > Machine Learning
[Submitted on 8 Apr 2026]
Title:Instance-Adaptive Parametrization for Amortized Variational Inference
View PDF HTML (experimental)Abstract:Latent variable models, including variational autoencoders (VAE), remain a central tool in modern deep generative modeling due to their scalability and a well-founded probabilistic formulation. These models rely on amortized variational inference to enable efficient posterior approximation, but this efficiency comes at the cost of a shared parametrization, giving rise to the amortization gap. We propose the instance-adaptive variational autoencoder (IA-VAE), an amortized variational inference framework in which a hypernetwork generates input-dependent modulations of a shared encoder. This enables input-specific adaptation of the inference model while preserving the efficiency of a single forward pass. By leveraging instance-specific parameter modulations, the proposed approach can achieve performance comparable to standard encoders with substantially fewer parameters, indicating a more efficient use of model capacity. Experiments on synthetic data, where the true posterior is known, show that IA-VAE yields more accurate posterior approximations and reduces the amortization gap. Similarly, on standard image benchmarks, IA-VAE consistently improves held-out ELBO over baseline VAEs, with statistically significant gains across multiple runs. These results suggest that increasing the flexibility of the inference parametrization through instance-adaptive modulation is a key factor in mitigating amortization-induced suboptimality in deep generative models.
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
