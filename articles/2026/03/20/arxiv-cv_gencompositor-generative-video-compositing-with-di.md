---
title: "GenCompositor: Generative Video Compositing with Diffusion Transformer"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2509.02460"
published: "2026-03-20"
fetched: "2026-03-20T16:12:58.303886"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 2 Sep 2025 (v1), last revised 19 Mar 2026 (this version, v2)]
Title:GenCompositor: Generative Video Compositing with Diffusion Transformer
View PDF HTML (experimental)Abstract:Video compositing combines live-action footage to create video production, serving as a crucial technique in video creation and film production. Traditional pipelines require intensive labor efforts and expert collaboration, resulting in lengthy production cycles and high manpower costs. To address this issue, we automate this process with generative models, called generative video compositing. This new task strives to adaptively inject identity and motion information of foreground video to the target video in an interactive manner, allowing users to customize the size, motion trajectory, and other attributes of the dynamic elements added in final video. Specifically, we designed a novel Diffusion Transformer (DiT) pipeline based on its intrinsic properties. To maintain consistency of the target video before and after editing, we revised a light-weight DiT-based background preservation branch with masked token injection. As to inherit dynamic elements from other sources, a DiT fusion block is proposed using full self-attention, along with a simple yet effective foreground augmentation for training. Besides, for fusing background and foreground videos with different layouts based on user control, we developed a novel position embedding, named Extended Rotary Position Embedding (ERoPE). Finally, we curated a dataset comprising 61K sets of videos for our new task, called VideoComp. This data includes complete dynamic elements and high-quality target videos. Experiments demonstrate that our method effectively realizes generative video compositing, outperforming existing possible solutions in fidelity and consistency. Project is available at this https URL
Submission history
From: Shuzhou Yang [view email][v1] Tue, 2 Sep 2025 16:10:13 UTC (17,215 KB)
[v2] Thu, 19 Mar 2026 03:37:51 UTC (20,227 KB)
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
