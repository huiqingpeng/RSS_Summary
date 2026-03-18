---
title: "Segmentation-before-Staining Improves Structural Fidelity in Virtual IHC-to-Multiplex IF Translation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16160"
published: "2026-03-18"
fetched: "2026-03-18T18:07:10.177257"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:Segmentation-before-Staining Improves Structural Fidelity in Virtual IHC-to-Multiplex IF Translation
View PDF HTML (experimental)Abstract:Multiplex immunofluorescence (mIF) enables simultaneous single-cell quantification of multiple biomarkers within intact tissue architecture, yet its high reagent cost, multi-round staining protocols, and need for specialized imaging platforms limit routine clinical adoption. Virtual staining can synthesize mIF channels from widely available brightfield immunohistochemistry (IHC), but current translators optimize pixel-level fidelity without explicitly constraining nuclear morphology. In pathology, this gap is clinically consequential: subtle distortions in nuclei count, shape, or spatial arrangement propagate directly to quantification endpoints such as the Ki67 proliferation index, where errors of a few percent can shift treatment-relevant risk categories. This work introduces a supervision-free, architecture-agnostic conditioning strategy that injects a continuous cell probability map from a pretrained nuclei segmentation foundation model as an explicit input prior, together with a variance-preserving regularization term that matches local intensity statistics to maintain cell-level heterogeneity in synthesized fluorescence channels. The soft prior retains gradient-level boundary information lost by binary thresholding, providing a richer conditioning signal without task-specific tuning. Controlled experiments across Pix2Pix with U-Net and ResNet generators, deterministic regression U-Net, and conditional diffusion on two independent datasets demonstrate consistent improvements in nuclei count fidelity and perceptual quality, as the sole modifications. Code will be made publicly available upon acceptance.
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
