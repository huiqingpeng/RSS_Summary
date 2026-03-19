---
title: "GTS: Inference-Time Scaling of Latent Reasoning with a Learnable Gaussian Thought Sampler"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2602.14077"
published: "2026-03-19"
fetched: "2026-03-19T14:18:51.826352"
---

Computer Science > Computation and Language
[Submitted on 15 Feb 2026 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:GTS: Inference-Time Scaling of Latent Reasoning with a Learnable Gaussian Thought Sampler
View PDF HTML (experimental)Abstract:Inference-time scaling (ITS) in latent reasoning models typically relies on heuristic perturbations, such as dropout or fixed Gaussian noise, to generate diverse candidate trajectories. However, we show that stronger perturbations do not necessarily yield better sampling quality: they often induce larger distribution shifts without producing more useful reasoning paths or better final decisions. A key limitation is that these perturbations inject stochasticity without defining an explicit conditional sampling distribution, making latent exploration difficult to control or optimize. To address this, we propose the Gaussian Thought Sampler (GTS), a lightweight module that reformulates latent exploration as sampling from a learned conditional distribution over continuous reasoning states. GTS predicts context-dependent perturbation distributions and is trained with GRPO-style policy optimization while keeping the backbone frozen, turning heuristic perturbation into an explicit probabilistic sampling policy. Experiments across multiple benchmarks and two latent reasoning architectures show that GTS yields more reliable inference-time scaling than heuristic baselines, suggesting that effective latent ITS requires better-controlled and optimizable sampling rather than simply amplifying stochasticity.
Submission history
From: Minghan Wang [view email][v1] Sun, 15 Feb 2026 09:57:47 UTC (165 KB)
[v2] Wed, 18 Mar 2026 07:35:39 UTC (211 KB)
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
