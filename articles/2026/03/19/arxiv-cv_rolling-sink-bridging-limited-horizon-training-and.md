---
title: "Rolling Sink: Bridging Limited-Horizon Training and Open-Ended Testing in Autoregressive Video Diffusion"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2602.07775"
published: "2026-03-19"
fetched: "2026-03-19T16:30:49.063218"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 8 Feb 2026 (v1), last revised 18 Mar 2026 (this version, v4)]
Title:Rolling Sink: Bridging Limited-Horizon Training and Open-Ended Testing in Autoregressive Video Diffusion
View PDFAbstract:Recently, autoregressive (AR) video diffusion models have achieved remarkable performance. However, due to their limited training durations, a train-test gap emerges when testing at longer horizons, leading to rapid visual degradations. Following Self Forcing, which studies the train-test gap within the training duration, this work studies the train-test gap beyond the training duration, i.e., the gap between the limited horizons during training and open-ended horizons during testing. Since open-ended testing can extend beyond any finite training window, and long-video training is computationally expensive, we pursue a training-free solution to bridge this gap. To explore a training-free solution, we conduct a systematic analysis of AR cache maintenance. These insights lead to Rolling Sink. Built on Self Forcing (trained on only 5s clips), Rolling Sink effectively scales the AR video synthesis to ultra-long durations (e.g., 5-30 minutes at 16 FPS) at test time, with consistent subjects, stable colors, coherent structures, and smooth motions. As demonstrated by extensive experiments, Rolling Sink achieves superior long-horizon visual fidelity and temporal consistency compared to SOTA baselines. Project page: this https URL
Submission history
From: Haodong Li [view email][v1] Sun, 8 Feb 2026 02:16:02 UTC (32,095 KB)
[v2] Thu, 5 Mar 2026 07:52:20 UTC (32,083 KB)
[v3] Sun, 15 Mar 2026 20:23:20 UTC (32,083 KB)
[v4] Wed, 18 Mar 2026 03:56:47 UTC (32,395 KB)
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
