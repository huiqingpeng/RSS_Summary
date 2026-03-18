---
title: "SpecMoE: Spectral Mixture-of-Experts Foundation Model for Cross-Species EEG Decoding"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16739"
published: "2026-03-18"
fetched: "2026-03-18T15:47:18.672305"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:SpecMoE: Spectral Mixture-of-Experts Foundation Model for Cross-Species EEG Decoding
View PDF HTML (experimental)Abstract:Decoding the orchestration of neural activity in electroencephalography (EEG) signals is a central challenge in bridging neuroscience with artificial intelligence. Foundation models have made strides in generalized EEG decoding, yet many existing frameworks primarily relying on separate temporal and spectral masking of raw signals during self-supervised pretraining. Such strategies often tend to bias learning toward high-frequency oscillations, as low-frequency rhythmic patterns can be easily inferred from the unmasked signal. We introduce a foundation model that utilizes a novel Gaussian-smoothed masking scheme applied to short-time Fourier transform (STFT) maps. By jointly applying time, frequency, and time-frequency Gaussian masks, we make the reconstruction task much more challenging, forcing the model to learn intricate neural patterns across both high- and low-frequency domains. To effectively recover signals under this aggressive masking strategy, we design SpecHi-Net, a U-shaped hierarchical architecture with multiple encoding and decoding stages. To accelerate large-scale pretraining, we partition the data into three subsets, each used to train an independent expert model. We then combine these models through SpecMoE, a mixture of experts framework guided by a learned spectral gating mechanism. SpecMoE achieves state-of-the-art performance across a diverse set of EEG decoding tasks, including sleep staging, emotion recognition, motor imagery classification, abnormal signal detection, and drug effect prediction. Importantly, the model demonstrates strong cross-species and cross-subject generalization, maintaining high accuracy on both human and murine EEG datasets.
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
