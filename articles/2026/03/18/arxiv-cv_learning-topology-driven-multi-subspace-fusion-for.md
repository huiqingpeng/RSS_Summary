---
title: "Learning Topology-Driven Multi-Subspace Fusion for Grassmannian Deep Network"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2511.08628"
published: "2026-03-18"
fetched: "2026-03-18T18:28:22.799729"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 9 Nov 2025 (v1), last revised 17 Mar 2026 (this version, v3)]
Title:Learning Topology-Driven Multi-Subspace Fusion for Grassmannian Deep Network
View PDF HTML (experimental)Abstract:Grassmannian manifold offers a powerful carrier for geometric representation learning by modelling high-dimensional data as low-dimensional subspaces. However, existing approaches predominantly rely on static single-subspace representations, neglecting the dynamic interplay between multiple subspaces critical for capturing complex geometric structures. To address this limitation, we propose a topology-driven multi-subspace fusion framework that enables adaptive subspace collaboration on the Grassmannian. Our solution introduces two key innovations: (1) Inspired by the Kolmogorov-Arnold representation theorem, an adaptive multi-subspace modelling mechanism is proposed that dynamically selects and weights task-relevant subspaces via topological convergence analysis, and (2) a multi-subspace interaction block that fuses heterogeneous geometric representations through Fréchet mean optimisation on the manifold. Theoretically, we establish the convergence guarantees of adaptive subspaces under a projection metric topology, ensuring stable gradient-based optimisation. Practically, we integrate Riemannian batch normalisation and mutual information regularisation to enhance discriminability and robustness. Extensive experiments on 3D action recognition (HDM05, FPHA), EEG classification (MAMEM-SSVEPII), and graph tasks demonstrate state-of-the-art performance. Our work not only advances geometric deep learning but also successfully adapts the proven multi-channel interaction philosophy of Euclidean networks to non-Euclidean domains, achieving superior discriminability and interpretability.
Submission history
From: Xuan Yu [view email][v1] Sun, 9 Nov 2025 10:33:13 UTC (897 KB)
[v2] Fri, 14 Nov 2025 04:39:42 UTC (2,591 KB)
[v3] Tue, 17 Mar 2026 01:08:38 UTC (2,591 KB)
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
