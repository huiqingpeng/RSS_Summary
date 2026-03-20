---
title: "One-to-More: High-Fidelity Training-Free Anomaly Generation with Attention Control"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18093"
published: "2026-03-20"
fetched: "2026-03-20T15:06:01.265653"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:One-to-More: High-Fidelity Training-Free Anomaly Generation with Attention Control
View PDF HTML (experimental)Abstract:Industrial anomaly detection (AD) is characterized by an abundance of normal images but a scarcity of anomalous ones. Although numerous few-shot anomaly synthesis methods have been proposed to augment anomalous data for downstream AD tasks, most existing approaches require time-consuming training and struggle to learn distributions that are faithful to real anomalies, thereby restricting the efficacy of AD models trained on such data. To address these limitations, we propose a training-free few-shot anomaly generation method, namely O2MAG, which leverages the self-attention in One reference anomalous image to synthesize More realistic anomalies, supporting effective downstream anomaly detection. Specifically, O2MAG manipulates three parallel diffusion processes via self-attention grafting and incorporates the anomaly mask to mitigate foreground-background query confusion, synthesizing text-guided anomalies that closely adhere to real anomalous distributions. To bridge the semantic gap between the encoded anomaly text prompts and the true anomaly semantics, Anomaly-Guided Optimization is further introduced to align the synthesis process with the target anomalous distribution, steering the generation toward realistic and text-consistent anomalies. Moreover, to mitigate faint anomaly synthesis inside anomaly masks, Dual-Attention Enhancement is adopted during generation to reinforce both self- and cross-attention on masked regions. Extensive experiments validate the effectiveness of O2MAG, demonstrating its superior performance over prior state-of-the-art methods on downstream AD tasks.
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
