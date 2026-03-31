---
title: "Hierarchy-Guided Topology Latent Flow for Molecular Graph Generation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.27113"
published: "2026-03-31"
fetched: "2026-04-01T07:21:27.175878"
---

Computer Science > Machine Learning
[Submitted on 28 Mar 2026]
Title:Hierarchy-Guided Topology Latent Flow for Molecular Graph Generation
View PDF HTML (experimental)Abstract:Generating chemically valid 3D molecules is hindered by discrete bond topology: small local bond errors can cause global failures (valence violations, disconnections, implausible rings), especially for drug-like molecules with long-range constraints. Many unconditional 3D generators emphasize coordinates and then infer bonds or rely on post-processing, leaving topology feasibility weakly controlled. We propose Hierarchy-Guided Latent Topology Flow (HLTF), a planner-executor model that generates bond graphs with 3D coordinates, using a latent multi-scale plan for global context and a constraint-aware sampler to suppress topology-driven failures. On QM9, HLTF achieves 98.8% atom stability and 92.9% valid-and-unique, improving PoseBusters validity to 94.0% (+0.9 over the strongest reported baseline). On GEOM-DRUGS, HLTF attains 85.5%/85.0% validity/valid-unique-novel without post-processing and 92.2%/91.2% after standardized relaxation, within 0.9 points of the best post-processed baseline. Explicit topology generation also reduces "false-valid" samples that pass RDKit sanitization but fail stricter checks.
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
