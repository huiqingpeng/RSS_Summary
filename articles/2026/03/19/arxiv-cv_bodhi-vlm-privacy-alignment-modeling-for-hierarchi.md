---
title: "Bodhi VLM: Privacy-Alignment Modeling for Hierarchical Visual Representations in Vision Backbones and VLM Encoders via Bottom-Up and Top-Down Feature Search"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.13728"
published: "2026-03-19"
fetched: "2026-03-19T17:03:30.261858"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 14 Mar 2026 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:Bodhi VLM: Privacy-Alignment Modeling for Hierarchical Visual Representations in Vision Backbones and VLM Encoders via Bottom-Up and Top-Down Feature Search
View PDF HTML (experimental)Abstract:Learning systems that preserve privacy often inject noise into hierarchical visual representations; a central challenge is to \emph{model} how such perturbations align with a declared privacy budget in a way that is interpretable and applicable across vision backbones and vision--language models (VLMs). We propose \emph{Bodhi VLM}, a \emph{privacy-alignment modeling} framework for \emph{hierarchical neural representations}: it (1) links sensitive concepts to layer-wise grouping via NCP and MDAV-based clustering; (2) locates sensitive feature regions using bottom-up (BUA) and top-down (TDA) strategies over multi-scale representations (e.g., feature pyramids or vision-encoder layers); and (3) uses an Expectation-Maximization Privacy Assessment (EMPA) module to produce an interpretable \emph{budget-alignment signal} by comparing the fitted sensitive-feature distribution to an evaluator-specified reference (e.g., Laplace or Gaussian with scale $c/\epsilon$). The output is reference-relative and is \emph{not} a formal differential-privacy estimator. We formalize BUA/TDA over hierarchical feature structures and validate the framework on object detectors (YOLO, PPDPTS, DETR) and on the \emph{visual encoders} of VLMs (CLIP, LLaVA, BLIP). BUA and TDA yield comparable deviation trends; EMPA provides a stable alignment signal under the reported setups. We compare with generic discrepancy baselines (Chi-square, K-L, MMD) and with task-relevant baselines (MomentReg, NoiseMLE, Wass-1). Results are reported as mean$\pm$std over multiple seeds with confidence intervals in the supplementary materials. This work contributes a learnable, interpretable modeling perspective for privacy-aligned hierarchical representations rather than a post hoc audit only. Source code: \href{this https URL}{Bodhi-VLM GitHub repository}
Submission history
From: Bo Ma Dr [view email][v1] Sat, 14 Mar 2026 03:11:31 UTC (3,501 KB)
[v2] Wed, 18 Mar 2026 08:32:49 UTC (3,205 KB)
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
