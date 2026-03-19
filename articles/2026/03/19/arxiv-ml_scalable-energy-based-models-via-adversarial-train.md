---
title: "Scalable Energy-Based Models via Adversarial Training: Unifying Discrimination and Generation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2510.13872"
published: "2026-03-19"
fetched: "2026-03-19T14:07:37.716950"
---

Computer Science > Machine Learning
[Submitted on 13 Oct 2025 (v1), last revised 18 Mar 2026 (this version, v4)]
Title:Scalable Energy-Based Models via Adversarial Training: Unifying Discrimination and Generation
View PDF HTML (experimental)Abstract:Simultaneously achieving robust classification and high-fidelity generative modeling within a single framework presents a significant challenge. Hybrid approaches, such as Joint Energy-Based Models (JEM), interpret classifiers as EBMs but are often limited by the instability and poor sample quality inherent in training based on Stochastic Gradient Langevin Dynamics (SGLD). We address these limitations by proposing a novel training framework that integrates adversarial training (AT) principles for both discriminative robustness and stable generative learning. The proposed method introduces three key innovations: (1) the replacement of SGLD-based JEM learning with a stable, AT-based approach that optimizes the energy function through a Binary Cross-Entropy (BCE) loss that discriminates between real data and contrastive samples generated via Projected Gradient Descent (PGD); (2) adversarial training for the discriminative component that enhances classification robustness while implicitly providing the gradient regularization needed for stable EBM training; and (3) a two-stage training strategy that addresses normalization-related instabilities and enables leveraging pretrained robust classifiers, generalizing effectively across architectures. Experiments on CIFAR-10/100 and ImageNet demonstrate that our approach: (1) is the first EBM-based hybrid to scale to high-resolution datasets with high training stability, simultaneously achieving state-of-the-art discriminative and generative performance on ImageNet 256x256; (2) uniquely combines generative quality with adversarial robustness, enabling faithful counterfactual explanations; and (3) functions as a competitive standalone generative model, matching autoregressive models and surpassing diffusion models while offering additional versatility.
Submission history
From: Xuwang Yin [view email][v1] Mon, 13 Oct 2025 13:07:22 UTC (6,709 KB)
[v2] Thu, 4 Dec 2025 13:35:02 UTC (7,998 KB)
[v3] Tue, 20 Jan 2026 15:22:16 UTC (7,992 KB)
[v4] Wed, 18 Mar 2026 06:30:59 UTC (8,221 KB)
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
