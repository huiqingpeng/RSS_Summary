---
title: "Temporal Gains, Spatial Costs: Revisiting Video Fine-Tuning in Multimodal Large Language Models"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17541"
published: "2026-03-19"
fetched: "2026-03-19T15:13:20.007051"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:Temporal Gains, Spatial Costs: Revisiting Video Fine-Tuning in Multimodal Large Language Models
View PDF HTML (experimental)Abstract:Multimodal large language models (MLLMs) are typically trained in multiple stages, with video-based supervised fine-tuning (Video-SFT) serving as a key step for improving visual understanding. Yet its effect on the fine-grained evolution of visual capabilities, particularly the balance between spatial and temporal understanding, remains poorly understood. In this paper, we systematically study how Video-SFT reshapes visual capabilities in MLLMs. Across architectures, parameter scales, and frame sampling settings, we observe a consistent pattern: Video-SFT reliably improves video performance, but often yields limited gains or even degradation on static image benchmarks. We further show that this trade-off is closely tied to temporal budget: increasing the number of sampled frames generally improves video performance, but does not reliably improve static image performance. Motivated by this finding, we study an instruction-aware Hybrid-Frame strategy that adaptively allocates frame counts and partially mitigates the image-video trade-off. Our results indicate that Video-SFT is not a free lunch for MLLMs, and preserving spatial understanding remains a central challenge in joint image-video training.
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
