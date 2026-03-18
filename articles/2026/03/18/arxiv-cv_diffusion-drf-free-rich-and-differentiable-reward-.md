---
title: "Diffusion-DRF: Free, Rich, and Differentiable Reward for Video Diffusion Fine-Tuning"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2601.04153"
published: "2026-03-18"
fetched: "2026-03-18T18:31:48.430313"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 7 Jan 2026 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:Diffusion-DRF: Free, Rich, and Differentiable Reward for Video Diffusion Fine-Tuning
View PDF HTML (experimental)Abstract:Video diffusion alignment has been heavily relied on scalar rewards. These rewards are typically derived from learned reward models in human preference datasets, requiring additional training and extensive collection. Moreover, scalar rewards provide coarse, global supervision, offering limited prompt-generation mismatch credit assignment and making models prone to reward exploitation and unstable optimization. We propose Diffusion-DRF, a free, rich, and differentiable reward framework for video diffusion fine-tuning. Diffusion-DRF employs a frozen, off-the-shelf Vision-Language Model (VLM) as the critic, eliminating the need for reward model training. Instead of relying on a single scalar reward, it decomposes each user prompt into multi-dimensional questions with freeform dense VQA explanation queries, yielding information-rich feedback. By direct differentiable optimization over this rich feedback, Diffusion-DRF achieves stable reward-based tuning without preference datasets collection. Diffusion-DRF achieves significant gains both quantitatively and qualitatively, outperforming state-of-the-art Flow-GRPO by 4.74% in overall performance on unseen VBench-2.0.
Submission history
From: Yifan Wang [view email][v1] Wed, 7 Jan 2026 18:05:08 UTC (3,492 KB)
[v2] Tue, 17 Mar 2026 17:21:55 UTC (22,552 KB)
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
