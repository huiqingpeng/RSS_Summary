---
title: "Robust-ComBat: Mitigating Outlier Effects in Diffusion MRI Data Harmonization"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17968"
published: "2026-03-19"
fetched: "2026-03-19T16:19:25.561519"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:Robust-ComBat: Mitigating Outlier Effects in Diffusion MRI Data Harmonization
View PDF HTML (experimental)Abstract:Harmonization methods such as ComBat and its variants are widely used to mitigate diffusion MRI (dMRI) site-specific biases. However, ComBat assumes that subject distributions exhibit a Gaussian profile. In practice, patients with neurological disorders often present diffusion metrics that deviate markedly from those of healthy controls, introducing pathological outliers that distort site-effect estimation. This problem is particularly challenging in clinical practice as most patients undergoing brain imaging have an underlying and yet undiagnosed condition, making it difficult to exclude them from harmonization cohorts, as their scans were precisely prescribed to establish a diagnosis. In this paper, we show that harmonizing data to a normative reference population with ComBat while including pathological cases induces significant distortions. Across 7 neurological conditions, we evaluated 10 outlier rejection methods with 4 ComBat variants over a wide range of scenarios, revealing that many filtering strategies fail in the presence of pathology. In contrast, a simple MLP provides robust outlier compensation enabling reliable harmonization while preserving disease-related signal. Experiments on both control and real multi-site cohorts, comprising up to 80% of subjects with neurological disorders, demonstrate that Robust-ComBat consistently outperforms conventional statistical baselines with lower harmonization error across all ComBat variants.
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
