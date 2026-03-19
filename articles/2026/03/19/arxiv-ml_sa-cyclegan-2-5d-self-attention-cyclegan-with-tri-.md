---
title: "SA-CycleGAN-2.5D: Self-Attention CycleGAN with Tri-Planar Context for Multi-Site MRI Harmonization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17219"
published: "2026-03-19"
fetched: "2026-03-19T13:10:24.202059"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:SA-CycleGAN-2.5D: Self-Attention CycleGAN with Tri-Planar Context for Multi-Site MRI Harmonization
View PDF HTML (experimental)Abstract:Multi-site neuroimaging analysis is fundamentally confounded by scanner-induced covariate shifts, where the marginal distribution of voxel intensities $P(\mathbf{x})$ varies non-linearly across acquisition protocols while the conditional anatomy $P(\mathbf{y}|\mathbf{x})$ remains constant. This is particularly detrimental to radiomic reproducibility, where acquisition variance often exceeds biological pathology variance. Existing statistical harmonization methods (e.g., ComBat) operate in feature space, precluding spatial downstream tasks, while standard deep learning approaches are theoretically bounded by local effective receptive fields (ERF), failing to model the global intensity correlations characteristic of field-strength bias.
We propose SA-CycleGAN-2.5D, a domain adaptation framework motivated by the $H\Delta H$-divergence bound of Ben-David et al., integrating three architectural innovations: (1) A 2.5D tri-planar manifold injection preserving through-plane gradients $\nabla_z$ at $O(HW)$ complexity; (2) A U-ResNet generator with dense voxel-to-voxel self-attention, surpassing the $O(\sqrt{L})$ receptive field limit of CNNs to model global scanner field biases; and (3) A spectrally-normalized discriminator constraining the Lipschitz constant ($K_D \le 1$) for stable adversarial optimization. Evaluated on 654 glioma patients across two institutional domains (BraTS and UPenn-GBM), our method reduces Maximum Mean Discrepancy (MMD) by 99.1% ($1.729 \to 0.015$) and degrades domain classifier accuracy to near-chance (59.7%). Ablation confirms that global attention is statistically essential (Cohen's $d = 1.32$, $p < 0.001$) for the harder heterogeneous-to-homogeneous translation direction. By bridging 2D efficiency and 3D consistency, our framework yields voxel-level harmonized images that preserve tumor pathophysiology, enabling reproducible multi-center radiomic analysis.
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
