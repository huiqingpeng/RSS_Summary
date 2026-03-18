---
title: "Learning through Creation: A Hash-Free Framework for On-the-Fly Category Discovery"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.13858"
published: "2026-03-18"
fetched: "2026-03-18T19:03:50.354876"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 14 Mar 2026 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:Learning through Creation: A Hash-Free Framework for On-the-Fly Category Discovery
View PDF HTML (experimental)Abstract:On-the-Fly Category Discovery (OCD) aims to recognize known classes while simultaneously discovering emerging novel categories during inference, using supervision only from known classes during offline training. Existing approaches rely either on fixed label supervision or on diffusion-based augmentations to enhance the backbone, yet none of them explicitly train the model to perform the discovery task required at test time. It is fundamentally unreasonable to expect a model optimized on limited labeled data to carry out a qualitatively different discovery objective during inference. This mismatch creates a clear optimization misalignment between the offline learning stage and the online discovery stage. In addition, prior methods often depend on hash-based encodings or severe feature compression, which further limits representational capacity. To address these issues, we propose Learning through Creation (LTC), a fully feature-based and hash-free framework that injects novel-category awareness directly into offline learning. At its core is a lightweight, online pseudo-unknown generator driven by kernel-energy minimization and entropy maximization (MKEE). Unlike previous methods that generate synthetic samples once before training, our generator evolves jointly with the model dynamics and synthesizes pseudo-novel instances on the fly at negligible cost. These samples are incorporated through a dual max-margin objective with adaptive thresholding, strengthening the model's ability to delineate and detect unknown regions through explicit creation. Extensive experiments across seven benchmarks show that LTC consistently outperforms prior work, achieving improvements ranging from 1.5 percent to 13.1 percent in all-class accuracy. The code is available at this https URL
Submission history
From: Yanan Wu [view email][v1] Sat, 14 Mar 2026 09:35:31 UTC (12,240 KB)
[v2] Tue, 17 Mar 2026 15:50:33 UTC (9,819 KB)
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
