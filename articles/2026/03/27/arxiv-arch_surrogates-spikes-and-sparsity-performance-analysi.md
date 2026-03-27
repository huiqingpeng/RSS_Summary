---
title: "Surrogates, Spikes, and Sparsity: Performance Analysis and Characterization of SNN Hyperparameters on Hardware"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.24891"
published: "2026-03-27"
fetched: "2026-03-28T07:07:08.649823"
---

Computer Science > Hardware Architecture
[Submitted on 26 Mar 2026]
Title:Surrogates, Spikes, and Sparsity: Performance Analysis and Characterization of SNN Hyperparameters on Hardware
View PDFAbstract:Spiking Neural Networks (SNNs) offer inherent advantages for low-power inference through sparse, event-driven computation. However, the theoretical energy benefits of SNNs are often decoupled from real hardware performance due to the opaque relationship between training-time choices and inference-time sparsity. While prior work has focused on weight pruning and compression, the role of training hyperparameters -- specifically surrogate gradient functions and neuron model configurations -- in shaping hardware-level activation sparsity remains underexplored.
This paper presents a workload characterization study quantifying the sensitivity of hardware latency to SNN hyperparameters. We decouple the impact of surrogate gradient functions (e.g., Fast Sigmoid, Spike Rate Escape) and neuron models (LIF, Lapicque) on classification accuracy and inference efficiency across three event-based vision datasets: DVS128-Gesture, N-MNIST, and DVS-CIFAR10. Our analysis reveals that standard accuracy metrics are poor predictors of hardware efficiency. While Fast Sigmoid achieves the highest accuracy on DVS-CIFAR10, Spike Rate Escape reduces inference latency by up to 12.2% on DVS128-Gesture with minimal accuracy trade-offs. We also demonstrate that neuron model selection is as critical as parameter tuning; transitioning from LIF to Lapicque neurons yields up to 28% latency reduction. We validate on a custom cycle-accurate FPGA-based SNN instrumentation platform, showing that sparsity-aware hyperparameter selection can improve accuracy by 9.1% and latency by over 2x compared to baselines. These findings establish a methodology for predicting hardware behavior from training parameters. The RTL and reproducibility artifacts are at this https URL.
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
