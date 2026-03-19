---
title: "KANtize: Exploring Low-bit Quantization of Kolmogorov-Arnold Networks for Efficient Inference"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.17230"
published: "2026-03-19"
fetched: "2026-03-19T12:03:07.891537"
---

Computer Science > Hardware Architecture
[Submitted on 18 Mar 2026]
Title:KANtize: Exploring Low-bit Quantization of Kolmogorov-Arnold Networks for Efficient Inference
View PDF HTML (experimental)Abstract:Kolmogorov-Arnold Networks (KANs) have gained attention for their potential to outperform Multi-Layer Perceptrons (MLPs) in terms of parameter efficiency and interpretability. Unlike traditional MLPs, KANs use learnable non-linear activation functions, typically spline functions, expressed as linear combinations of basis splines (B-splines). B-spline coefficients serve as the model's learnable parameters. However, evaluating these spline functions increases computational complexity during inference. Conventional quantization reduces this complexity by lowering the numerical precision of parameters and activations. However, the impact of quantization on KANs, and especially its effectiveness in reducing computational complexity, is largely unexplored, particularly for quantization levels below 8 bits. The study investigates the impact of low-bit quantization on KANs and its impact on computational complexity and hardware efficiency. Results show that B-splines can be quantized to 2-3 bits with negligible loss in accuracy, significantly reducing computational complexity. Hence, we investigate the potential of using low-bit quantized precomputed tables as a replacement for the recursive B-spline algorithm. This approach aims to further reduce the computational complexity of KANs and enhance hardware efficiency while maintaining accuracy. For example, ResKAN18 achieves a 50x reduction in BitOps without loss of accuracy using low-bit-quantized B-spline tables. Additionally, precomputed 8-bit lookup tables improve GPU inference speedup by up to 2.9x, while on FPGA-based systolic-array accelerators, reducing B-spline table precision from 8 to 3 bits cuts resource usage by 36%, increases clock frequency by 50%, and enhances speedup by 1.24x. On a 28nm FD-SOI ASIC, reducing the B-spline bit-width from 16 to 3 bits achieves 72% area reduction and 50% higher maximum frequency.
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
