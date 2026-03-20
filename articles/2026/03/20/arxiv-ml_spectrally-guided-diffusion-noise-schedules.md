---
title: "Spectrally-Guided Diffusion Noise Schedules"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19222"
published: "2026-03-20"
fetched: "2026-03-20T13:21:54.541467"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 19 Mar 2026]
Title:Spectrally-Guided Diffusion Noise Schedules
View PDF HTML (experimental)Abstract:Denoising diffusion models are widely used for high-quality image and video generation. Their performance depends on noise schedules, which define the distribution of noise levels applied during training and the sequence of noise levels traversed during sampling. Noise schedules are typically handcrafted and require manual tuning across different resolutions. In this work, we propose a principled way to design per-instance noise schedules for pixel diffusion, based on the image's spectral properties. By deriving theoretical bounds on the efficacy of minimum and maximum noise levels, we design ``tight'' noise schedules that eliminate redundant steps. During inference, we propose to conditionally sample such noise schedules. Experiments show that our noise schedules improve generative quality of single-stage pixel diffusion models, particularly in the low-step regime.
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
