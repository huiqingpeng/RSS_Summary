---
title: "Stable Forgetting: Bounded Parameter-Efficient Unlearning in Foundation Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2509.24166"
published: "2026-03-19"
fetched: "2026-03-19T14:07:10.728624"
---

Computer Science > Machine Learning
[Submitted on 29 Sep 2025 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:Stable Forgetting: Bounded Parameter-Efficient Unlearning in Foundation Models
View PDF HTML (experimental)Abstract:Machine unlearning in foundation models (e.g., language and vision transformers) is essential for privacy and safety; however, existing approaches are unstable and unreliable. A widely used strategy, the gradient difference method, applies gradient descent to retained data while performing gradient ascent on forgotten data. When combined with cross-entropy, this procedure can trigger the unbounded growth of weights and gradients, degrading both forgetting and retention. We provide a theoretical framework that explains this failure by showing how ascent destabilizes optimization in transformer feedforward MLP layers. Guided by this insight, we propose *Bounded Parameter-Efficient Unlearning*, which stabilizes LoRA-based fine-tuning by applying bounded functions to MLP adapters. This controls the weight dynamics during ascent and enables reliable convergence. We validate the approach on Vision Transformer class deletion on CIFAR-100, where GD+Sine is the only evaluated method to achieve both high forget quality and model utility across ViT-B/16, ViT-L/14, and DeiT-S architectures, and demonstrate generality on language-model benchmarks (TOFU, TDEC, MUSE) across architectures from 22M to 8B parameters, achieving improved forgetting while preserving utility.
Submission history
From: Arpit Garg [view email][v1] Mon, 29 Sep 2025 01:30:15 UTC (2,383 KB)
[v2] Tue, 17 Mar 2026 23:23:56 UTC (344 KB)
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
