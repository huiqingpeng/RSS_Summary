---
title: "Continual Multimodal Egocentric Activity Recognition via Modality-Aware Novel Detection"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16970"
published: "2026-03-19"
fetched: "2026-03-19T15:03:19.942259"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:Continual Multimodal Egocentric Activity Recognition via Modality-Aware Novel Detection
View PDF HTML (experimental)Abstract:Multimodal egocentric activity recognition integrates visual and inertial cues for robust first-person behavior understanding. However, deploying such systems in open-world environments requires detecting novel activities while continuously learning from non-stationary streams. Existing methods rely on the main logits for novelty scoring, without fully exploiting the complementary evidence available from individual modalities. Because these logits are often dominated by RGB, cues from other modalities, particularly IMU, remain underutilized, and this imbalance worsens over time under catastrophic forgetting. To address this, we propose MAND, a modality-aware framework for multimodal egocentric open-world continual learning. At inference, Modality-aware Adaptive Scoring (MoAS) estimates sample-wise modality reliability from energy scores and adaptively integrates modality logits to better exploit complementary modality cues for novelty detection. During training, Modality-wise Representation Stabilization Training (MoRST) preserves modality-specific discriminability across tasks via auxiliary heads and modality-wise logit distillation. Experiments on a public multimodal egocentric benchmark show that MAND improves novel activity detection AUC by up to 10\% and known-class classification accuracy by up to 2.8\% over state-of-the-art baselines.
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
