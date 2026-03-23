---
title: "Toward Reproducible and Standardized Computer Architecture Simulation with gem5"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2512.13479"
published: "2026-03-23"
fetched: "2026-03-24T07:14:52.158462"
---

Computer Science > Hardware Architecture
[Submitted on 15 Dec 2025 (v1), last revised 20 Mar 2026 (this version, v2)]
Title:Toward Reproducible and Standardized Computer Architecture Simulation with gem5
View PDF HTML (experimental)Abstract:Reproducibility in simulation-based computer architecture research requires coordinating artifacts like disk images, kernels, and benchmarks, but existing workflows are inconsistent. We improve gem5, an open-source simulator with over 1600 forks, and gem5 Resources, a centralized repository of over 2000 pre-packaged artifacts, to address these issues. While gem5 Resources enables artifact sharing, researchers still face challenges. Creating custom disk images is complex and time-consuming, with no standardized process across ISAs, making it difficult to extend and share images. gem5 provides limited guest-host communication features through a set of predefined exit events that restrict researchers' ability to dynamically control and monitor simulations. Lastly, running simulations with multiple workloads requires researchers to write custom external scripts to coordinate multiple gem5 simulations which creates error-prone and hard-to-reproduce workflows. To overcome this, we introduce several features in gem5 and gem5 Resources. We standardize disk-image creation across x86, ARM, and RISC-V using Packer, and provide validated base images with pre-annotated benchmark suites (NPB, GAPBS). We provide 12 new disk images, 6 new kernels, and over 200 workloads across three ISAs. We refactor the exit event system to a class-based model and introduce hypercalls for enhanced guest-host communication that allows researchers to define custom behavior for their exit events. We also provide a utility to remotely monitor simulations and the gem5-bridge driver for user-space m5 operations. Additionally, we implemented Suites and MultiSim to enable parallel full-system simulations from gem5 configuration scripts, eliminating the need for external scripting. These features reduce setup complexity and provide extensible, validated resources that improve reproducibility and standardization.
Submission history
From: Kunal Pai [view email][v1] Mon, 15 Dec 2025 16:16:44 UTC (310 KB)
[v2] Fri, 20 Mar 2026 01:01:37 UTC (226 KB)
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
