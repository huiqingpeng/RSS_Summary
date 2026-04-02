---
title: "SAGE: Subsurface AI-driven Geostatistical Extraction with proxy posterior"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00307"
published: "2026-04-02"
fetched: "2026-04-03T07:20:05.667775"
---

Computer Science > Machine Learning
[Submitted on 31 Mar 2026]
Title:SAGE: Subsurface AI-driven Geostatistical Extraction with proxy posterior
View PDF HTML (experimental)Abstract:Recent advances in generative networks have enabled new approaches to subsurface velocity model synthesis, offering a compelling alternative to traditional methods such as Full Waveform Inversion. However, these approaches predominantly rely on the availability of large-scale datasets of high-quality, geologically realistic subsurface velocity models, which are often difficult to obtain in practice. We introduce SAGE, a novel framework for statistically consistent proxy velocity generation from incomplete observations, specifically sparse well logs and migrated seismic images. During training, SAGE learns a proxy posterior over velocity models conditioned on both modalities (wells and seismic); at inference, it produces full-resolution velocity fields conditioned solely on migrated images, with well information implicitly encoded in the learned distribution. This enables the generation of geologically plausible and statistically accurate velocity realizations. We validate SAGE on both synthetic and field datasets, demonstrating its ability to capture complex subsurface variability under limited observational constraints. Furthermore, samples drawn from the learned proxy distribution can be leveraged to train downstream networks, supporting inversion workflows. Overall, SAGE provides a scalable and data-efficient pathway toward learning geological proxy posterior for seismic imaging and inversion. Repo link: this https URL.
Submission history
From: Huseyin Tuna Erdinc [view email][v1] Tue, 31 Mar 2026 23:06:32 UTC (6,159 KB)
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
