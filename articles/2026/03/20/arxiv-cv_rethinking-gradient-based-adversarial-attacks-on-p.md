---
title: "Rethinking Gradient-based Adversarial Attacks on Point Cloud Classification"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2505.21854"
published: "2026-03-20"
fetched: "2026-03-20T16:11:36.914153"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 28 May 2025 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:Rethinking Gradient-based Adversarial Attacks on Point Cloud Classification
View PDF HTML (experimental)Abstract:Gradient-based adversarial attacks are widely used to evaluate the robustness of 3D point cloud classifiers, yet they often rely on uniform update rules that neglect point-wise heterogeneity, leading to perceptible perturbations. We propose two complementary strategies to improve both the effectiveness and imperceptibility of the attack. \textbf{WAAttack} employs weighted gradients to dynamically adjust per-point perturbation magnitudes and uses an adaptive step size strategy to regulate the global perturbation scale. \textbf{SubAttack} partitions the point cloud into subsets and, at each iteration, perturbs only those combinations with high adversarial efficacy and low perceptual saliency. Together, these methods offer a principled refinement of gradient-based attacks for 3D point clouds. Extensive experiments show that our approach consistently outperforms state-of-the-art methods in generating highly imperceptible adversarial examples. The code is available at this https URL.
Submission history
From: Chongshou Li Dr. [view email][v1] Wed, 28 May 2025 00:55:36 UTC (42,461 KB)
[v2] Wed, 18 Mar 2026 13:36:28 UTC (26,548 KB)
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
