---
title: "Latent Algorithmic Structure Precedes Grokking: A Mechanistic Study of ReLU MLPs on Modular Arithmetic"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23784"
published: "2026-03-26"
fetched: "2026-03-27T07:17:03.106583"
---

Computer Science > Machine Learning
[Submitted on 24 Mar 2026]
Title:Latent Algorithmic Structure Precedes Grokking: A Mechanistic Study of ReLU MLPs on Modular Arithmetic
View PDF HTML (experimental)Abstract:Grokking-the phenomenon where validation accuracy of neural networks on modular addition of two integers rises long after training data has been memorized-has been characterized in previous works as producing sinusoidal input weight distributions in transformers and multi-layer perceptrons (MLPs). We find empirically that ReLU MLPs in our experimental setting instead learn near-binary square wave input weights, where intermediate-valued weights appear exclusively near sign-change boundaries, alongside output weight distributions whose dominant Fourier phases satisfy a phase-sum relation $\phi_{\mathrm{out}} = \phi_a + \phi_b$; this relation holds even when the model is trained on noisy data and fails to grok. We extract the frequency and phase of each neuron's weights via DFT and construct an idealized MLP: Input weights are replaced by perfect binary square waves and output weights by cosines, both parametrized by the frequencies, phases, and amplitudes extracted from the dominant Fourier components of the real model weights. This idealized model achieves 95.5% accuracy when the frequencies and phases are extracted from the weights of a model trained on noisy data that itself achieves only 0.23% accuracy. This suggests that grokking does not discover the correct algorithm, but rather sharpens an algorithm substantially encoded during memorization, progressively binarizing the input weights into cleaner square waves and aligning the output weights, until generalization becomes possible.
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
