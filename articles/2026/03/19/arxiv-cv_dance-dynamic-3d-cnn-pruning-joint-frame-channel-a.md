---
title: "DANCE: Dynamic 3D CNN Pruning: Joint Frame, Channel, and Feature Adaptation for Energy Efficiency on the Edge"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17275"
published: "2026-03-19"
fetched: "2026-03-19T15:07:21.955550"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:DANCE: Dynamic 3D CNN Pruning: Joint Frame, Channel, and Feature Adaptation for Energy Efficiency on the Edge
View PDF HTML (experimental)Abstract:Modern convolutional neural networks (CNNs) are workhorses for video and image processing, but fail to adapt to the computational complexity of input samples in a dynamic manner to minimize energy consumption. In this research, we propose DANCE, a fine-grained, input-aware, dynamic pruning framework for 3D CNNs to maximize power efficiency with negligible to zero impact on performance. In the proposed two-step approach, the first step is called activation variability amplification (AVA), and the 3D CNN model is retrained to increase the variance of the magnitude of neuron activations across the network in this step, facilitating pruning decisions across diverse CNN input scenarios. In the second step, called adaptive activation pruning (AAP), a lightweight activation controller network is trained to dynamically prune frames, channels, and features of 3D convolutional layers of the network (different for each layer), based on statistics of the outputs of the first layer of the network. Our method achieves substantial savings in multiply-accumulate (MAC) operations and memory accesses by introducing sparsity within convolutional layers. Hardware validation on the NVIDIA Jetson Nano GPU and the Qualcomm Snapdragon 8 Gen 1 platform demonstrates respective speedups of 1.37X and 2.22X, achieving up to 1.47X higher energy efficiency compared to the state of the art.
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
