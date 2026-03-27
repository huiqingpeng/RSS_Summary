---
title: "BiFM: Bidirectional Flow Matching for Few-Step Image Editing and Generation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.24942"
published: "2026-03-27"
fetched: "2026-03-28T07:18:50.918500"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 26 Mar 2026]
Title:BiFM: Bidirectional Flow Matching for Few-Step Image Editing and Generation
View PDF HTML (experimental)Abstract:Recent diffusion and flow matching models have demonstrated strong capabilities in image generation and editing by progressively removing noise through iterative sampling. While this enables flexible inversion for semantic-preserving edits, few-step sampling regimes suffer from poor forward process approximation, leading to degraded editing quality. Existing few-step inversion methods often rely on pretrained generators and auxiliary modules, limiting scalability and generalization across different architectures. To address these limitations, we propose BiFM (Bidirectional Flow Matching), a unified framework that jointly learns generation and inversion within a single model. BiFM directly estimates average velocity fields in both ``image $\to$ noise" and ``noise $\to$ image" directions, constrained by a shared instantaneous velocity field derived from either predefined schedules or pretrained multi-step diffusion models. Additionally, BiFM introduces a novel training strategy using continuous time-interval supervision, stabilized by a bidirectional consistency objective and a lightweight time-interval embedding. This bidirectional formulation also enables one-step inversion and can integrate seamlessly into popular diffusion and flow matching backbones. Across diverse image editing and generation tasks, BiFM consistently outperforms existing few-step approaches, achieving superior performance and editability.
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
