---
title: "ACPV-Net: All-Class Polygonal Vectorization for Seamless Vector Map Generation from Aerial Imagery"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16616"
published: "2026-03-18"
fetched: "2026-03-18T18:15:45.186205"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:ACPV-Net: All-Class Polygonal Vectorization for Seamless Vector Map Generation from Aerial Imagery
View PDF HTML (experimental)Abstract:We tackle the problem of generating a complete vector map representation from aerial imagery in a single run: producing polygons for all land-cover classes with shared boundaries and without gaps or overlaps. Existing polygonization methods are typically class-specific; extending them to multiple classes via per-class runs commonly leads to topological inconsistencies, such as duplicated edges, gaps, and overlaps. We formalize this new task as All-Class Polygonal Vectorization (ACPV) and release the first public benchmark, Deventer-512, with standardized metrics jointly evaluating semantic fidelity, geometric accuracy, vertex efficiency, per-class topological fidelity and global topological consistency. To realize ACPV, we propose ACPV-Net, a unified framework introducing a novel Semantically Supervised Conditioning (SSC) mechanism coupling semantic perception with geometric primitive generation, along with a topological reconstruction that enforces shared-edge consistency by design. While enforcing such strict topological constraints, ACPV-Net surpasses all class-specific baselines in polygon quality across classes on Deventer-512. It also applies to single-class polygonal vectorization without any architectural modification, achieving the best-reported results on WHU-Building. Data, code, and models will be released at: this https URL.
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
