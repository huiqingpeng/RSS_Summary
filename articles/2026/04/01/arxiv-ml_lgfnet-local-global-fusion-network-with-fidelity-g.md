---
title: "LGFNet: Local-Global Fusion Network with Fidelity Gap Delta Learning for Multi-Source Aerodynamics"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.29303"
published: "2026-04-01"
fetched: "2026-04-02T07:17:20.963472"
---

Computer Science > Machine Learning
[Submitted on 31 Mar 2026]
Title:LGFNet: Local-Global Fusion Network with Fidelity Gap Delta Learning for Multi-Source Aerodynamics
View PDFAbstract:The precise fusion of computational fluid dynamic (CFD) data, wind tunnel tests data, and flight tests data in aerodynamic area is essential for obtaining comprehensive knowledge of both localized flow structures and global aerodynamic trends across the entire flight envelope. However, existing methodologies often struggle to balance high-resolution local fidelity with wide-range global dependency, leading to either a loss of sharp discontinuities or an inability to capture long-range topological correlations. We propose Local-Global Fusion Network (LGFNet) for multi-scale feature decomposition to extract this dual-natured aerodynamic knowledge. To this end, LGFNet combines a spatial perception layer that integrates a sliding window mechanism with a relational reasoning layer based on self-attention, simultaneously reinforcing the continuity of fine-grained local features (e.g., shock waves) and capturing long-range flow information. Furthermore, the fidelity gap delta learning (FGDL) strategy is proposed to treat CFD data as a "low-frequency carrier" to explicitly approximate nonlinear discrepancies. This approach prevents unphysical smoothing while inheriting the foundational physical trends from the simulation baseline. Experiments demonstrate that LGFNet achieves state-of-the-art (SOTA) performance in both accuracy and uncertainty reduction across diverse aerodynamic scenarios.
Current browse context:
cs.LG
Change to browse by:
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
