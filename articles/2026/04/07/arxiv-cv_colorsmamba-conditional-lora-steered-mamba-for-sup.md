---
title: "CoLoRSMamba: Conditional LoRA-Steered Mamba for Supervised Multimodal Violence Detection"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2604.03329"
published: "2026-04-07"
fetched: "2026-04-08T07:02:51.011341"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 2 Apr 2026]
Title:CoLoRSMamba: Conditional LoRA-Steered Mamba for Supervised Multimodal Violence Detection
View PDF HTML (experimental)Abstract:Violence detection benefits from audio, but real-world soundscapes can be noisy or weakly related to the visible scene. We present CoLoRSMamba, a directional Video to Audio multimodal architecture that couples VideoMamba and AudioMamba through CLS-guided conditional LoRA. At each layer, the VideoMamba CLS token produces a channel-wise modulation vector and a stabilization gate that adapt the AudioMamba projections responsible for the selective state-space parameters (Delta, B, C), including the step-size pathway, yielding scene-aware audio dynamics without token-level cross-attention. Training combines binary classification with a symmetric AV-InfoNCE objective that aligns clip-level audio and video embeddings. To support fair multimodal evaluation, we curate audio-filtered clip level subsets of the NTU-CCTV and DVD datasets from temporal annotations, retaining only clips with available audio. On these subsets, CoLoRSMamba outperforms representative audio-only, video-only, and multimodal baselines, achieving 88.63% accuracy / 86.24% F1-V on NTU-CCTV and 75.77% accuracy / 72.94% F1-V on DVD. It further offers a favorable accuracy-efficiency tradeoff, surpassing several larger models with fewer parameters and FLOPs.
Submission history
From: Damith Chamalke Senadeera Mr [view email][v1] Thu, 2 Apr 2026 22:14:25 UTC (10,409 KB)
Current browse context:
cs.CV
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
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
