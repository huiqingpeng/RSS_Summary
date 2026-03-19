---
title: "KGS-GCN: Enhancing Sparse Skeleton Sensing via Kinematics-Driven Gaussian Splatting and Probabilistic Topology for Action Recognition"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16943"
published: "2026-03-19"
fetched: "2026-03-19T14:21:37.523041"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 16 Mar 2026]
Title:KGS-GCN: Enhancing Sparse Skeleton Sensing via Kinematics-Driven Gaussian Splatting and Probabilistic Topology for Action Recognition
View PDFAbstract:Skeleton-based action recognition is widely utilized in sensor systems including human-computer interaction and intelligent surveillance. Nevertheless, current sensor devices typically generate sparse skeleton data as discrete coordinates, which inevitably discards fine-grained spatiotemporal details during highly dynamic movements. Moreover, the rigid constraints of predefined physical sensor topologies hinder the modeling of latent long-range dependencies. To overcome these limitations, we propose KGS-GCN, a graph convolutional network that integrates kinematics-driven Gaussian splatting with probabilistic topology. Our framework explicitly addresses the challenges of sensor data sparsity and topological rigidity by transforming discrete joints into continuous generative representations. Firstly, a kinematics-driven Gaussian splatting module is designed to dynamically construct anisotropic covariance matrices using instantaneous joint velocity vectors. This module enhances visual representation by rendering sparse skeleton sequences into multi-view continuous heatmaps rich in spatiotemporal semantics. Secondly, to transcend the limitations of fixed physical connections, a probabilistic topology construction method is proposed. This approach generates an adaptive prior adjacency matrix by quantifying statistical correlations via the Bhattacharyya distance between joint Gaussian distributions. Ultimately, the GCN backbone is adaptively modulated by the rendered visual features via a visual context gating mechanism. Empirical results demonstrate that KGS-GCN significantly enhances the modeling of complex spatiotemporal dynamics. By addressing the inherent limitations of sparse inputs, our framework offers a robust solution for processing low-fidelity sensor data. This approach establishes a practical pathway for improving perceptual reliability in real-world sensing applications.
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
