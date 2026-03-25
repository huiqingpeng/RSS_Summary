---
title: "ST-GDance++: A Scalable Spatial-Temporal Diffusion for Long-Duration Group Choreography"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22316"
published: "2026-03-25"
fetched: "2026-03-26T07:10:16.388792"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:ST-GDance++: A Scalable Spatial-Temporal Diffusion for Long-Duration Group Choreography
View PDF HTML (experimental)Abstract:Group dance generation from music requires synchronizing multiple dancers while maintaining spatial coordination, making it highly relevant to applications such as film production, gaming, and animation. Recent group dance generation models have achieved promising generation quality, but they remain difficult to deploy in interactive scenarios due to bidirectional attention dependencies. As the number of dancers and the sequence length increase, the attention computation required for aligning music conditions with motion sequences grows quadratically, leading to reduced efficiency and increased risk of motion collisions. Effectively modeling dense spatial-temporal interactions is therefore essential, yet existing methods often struggle to capture such complexity, resulting in limited scalability and unstable multi-dancer coordination. To address these challenges, we propose ST-GDance++, a scalable framework that decouples spatial and temporal dependencies to enable efficient and collision-aware group choreography generation. For spatial modeling, we introduce lightweight distance-aware graph convolutions to capture inter-dancer relationships while reducing computational overhead. For temporal modeling, we design a diffusion noise scheduling strategy together with an efficient temporal-aligned attention mask, enabling stream-based generation for long motion sequences and improving scalability in long-duration scenarios. Experiments on the AIOZ-GDance dataset show that ST-GDance++ achieves competitive generation quality with significantly reduced latency compared to existing methods.
Current browse context:
cs.LG
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
IArxiv Recommender
(What is IArxiv?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
