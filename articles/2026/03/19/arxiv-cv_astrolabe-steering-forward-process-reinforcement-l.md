---
title: "Astrolabe: Steering Forward-Process Reinforcement Learning for Distilled Autoregressive Video Models"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17051"
published: "2026-03-19"
fetched: "2026-03-19T15:04:06.044291"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:Astrolabe: Steering Forward-Process Reinforcement Learning for Distilled Autoregressive Video Models
View PDFAbstract:Distilled autoregressive (AR) video models enable efficient streaming generation but frequently misalign with human visual preferences. Existing reinforcement learning (RL) frameworks are not naturally suited to these architectures, typically requiring either expensive re-distillation or solver-coupled reverse-process optimization that introduces considerable memory and computational overhead. We present Astrolabe, an efficient online RL framework tailored for distilled AR models. To overcome existing bottlenecks, we introduce a forward-process RL formulation based on negative-aware fine-tuning. By contrasting positive and negative samples directly at inference endpoints, this approach establishes an implicit policy improvement direction without requiring reverse-process unrolling. To scale this alignment to long videos, we propose a streaming training scheme that generates sequences progressively via a rolling KV-cache, applying RL updates exclusively to local clip windows while conditioning on prior context to ensure long-range coherence. Finally, to mitigate reward hacking, we integrate a multi-reward objective stabilized by uncertainty-aware selective regularization and dynamic reference updates. Extensive experiments demonstrate that our method consistently enhances generation quality across multiple distilled AR video models, serving as a robust and scalable alignment solution.
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
