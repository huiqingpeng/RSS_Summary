---
title: "Generate Any Scene: Scene Graph Driven Data Synthesis for Visual Generation Training"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2412.08221"
published: "2026-03-18"
fetched: "2026-03-18T17:09:12.984411"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 11 Dec 2024 (v1), last revised 17 Mar 2026 (this version, v4)]
Title:Generate Any Scene: Scene Graph Driven Data Synthesis for Visual Generation Training
View PDF HTML (experimental)Abstract:Recent advances in text-to-vision generation excel in visual fidelity but struggle with compositional generalization and semantic alignment. Existing datasets are noisy and weakly compositional, limiting models' understanding of complex scenes, while scalable solutions for dense, high-quality annotations remain a challenge. We introduce Generate Any Scene, a data engine that systematically enumerates scene graphs representing the combinatorial array of possible visual scenes. Generate Any Scene dynamically constructs scene graphs of varying complexity from a structured taxonomy of objects, attributes, and relations. Given a sampled scene graph, Generate Any Scene translates it into a caption for text-to-image or text-to-video generation; it also translates it into a set of visual question answers that allow automatic evaluation and reward modeling of semantic alignment. Using Generate Any Scene, we first design a self-improving framework where models iteratively enhance their performance using generated data. Stable Diffusion v1.5 achieves an average 4% improvement over baselines and surpassing fine-tuning on CC3M. Second, we also design a distillation algorithm to transfer specific strengths from proprietary models to their open-source counterparts. Using fewer than 800 synthetic captions, we fine-tune Stable Diffusion v1.5 and achieve a 10% increase in TIFA score on compositional and hard concept generation. Third, we create a reward model to align model generation with semantic accuracy at a low cost. Using GRPO algorithm, we fine-tune SimpleAR-0.5B-SFT and surpass CLIP-based methods by +5% on DPG-Bench. Finally, we apply these ideas to the downstream task of content moderation where we train models to identify challenging cases by learning from synthetic data.
Submission history
From: Ziqi Gao [view email][v1] Wed, 11 Dec 2024 09:17:39 UTC (17,453 KB)
[v2] Mon, 16 Dec 2024 09:54:46 UTC (17,453 KB)
[v3] Thu, 9 Oct 2025 23:10:23 UTC (8,606 KB)
[v4] Tue, 17 Mar 2026 00:31:19 UTC (44,483 KB)
Current browse context:
cs.CV
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
