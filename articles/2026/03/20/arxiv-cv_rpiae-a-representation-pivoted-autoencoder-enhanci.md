---
title: "RPiAE: A Representation-Pivoted Autoencoder Enhancing Both Image Generation and Editing"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.19206"
published: "2026-03-20"
fetched: "2026-03-20T16:05:38.737868"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 19 Mar 2026]
Title:RPiAE: A Representation-Pivoted Autoencoder Enhancing Both Image Generation and Editing
View PDF HTML (experimental)Abstract:Diffusion models have become the dominant paradigm for image generation and editing, with latent diffusion models shifting denoising to a compact latent space for efficiency and scalability. Recent attempts to leverage pretrained visual representation models as tokenizer priors either align diffusion features to representation features or directly reuse representation encoders as frozen tokenizers. Although such approaches can improve generation metrics, they often suffer from limited reconstruction fidelity due to frozen encoders, which in turn degrades editing quality, as well as overly high-dimensional latents that make diffusion modeling difficult. To address these limitations, We propose Representation-Pivoted AutoEncoder, a representation-based tokenizer that improves both generation and editing. We introduce Representation-Pivot Regularization, a training strategy that enables a representation-initialized encoder to be fine-tuned for reconstruction while preserving the semantic structure of the pretrained representation space, followed by a variational bridge which compress latent space into a compact one for better diffusion modeling. We adopt an objective-decoupled stage-wise training strategy that sequentially optimizes generative tractability and reconstruction-fidelity objectives. Together, these components yield a tokenizer that preserves strong semantics, reconstructs faithfully, and produces latents with reduced diffusion modeling complexity. Experiments demonstrate that RPiAE outperforms other visual tokenizers on text-to-image generation and image editing, while delivering the best reconstruction fidelity among representation-based tokenizers.
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
