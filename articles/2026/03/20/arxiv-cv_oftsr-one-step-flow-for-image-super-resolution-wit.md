---
title: "OFTSR: One-Step Flow for Image Super-Resolution with Tunable Fidelity-Realism Trade-offs"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2412.09465"
published: "2026-03-20"
fetched: "2026-03-20T16:10:34.407388"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 12 Dec 2024 (v1), last revised 19 Mar 2026 (this version, v3)]
Title:OFTSR: One-Step Flow for Image Super-Resolution with Tunable Fidelity-Realism Trade-offs
View PDFAbstract:Recent advances in diffusion and flow-based generative models have demonstrated remarkable success in image restoration tasks, achieving superior perceptual quality compared to traditional deep learning approaches. However, these methods either require numerous sampling steps to generate high-quality images, resulting in significant computational overhead, or rely on common model distillation, which usually imposes a fixed fidelity-realism trade-off and thus lacks flexibility. In this paper, we introduce OFTSR, a novel flow-based framework for one-step image super-resolution that can produce outputs with tunable levels of fidelity and realism. Our approach first trains a conditional flow-based super-resolution model to serve as a teacher model. We then distill this teacher model by applying a specialized constraint. Specifically, we force the predictions from our one-step student model for same input to lie on the same sampling ODE trajectory of the teacher model. This alignment ensures that the student model's single-step predictions from initial states match the teacher's predictions from a closer intermediate state. Through extensive experiments on datasets including FFHQ (256$\times$256), DIV2K, and ImageNet (256$\times$256), we demonstrate that OFTSR achieves state-of-the-art performance for one-step image super-resolution, while having the ability to flexibly tune the fidelity-realism trade-off. Codes: \href{this https URL}{this https URL}.
Submission history
From: Yuanzhi Zhu [view email][v1] Thu, 12 Dec 2024 17:14:58 UTC (12,392 KB)
[v2] Wed, 3 Sep 2025 22:09:05 UTC (12,743 KB)
[v3] Thu, 19 Mar 2026 12:57:45 UTC (22,266 KB)
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
