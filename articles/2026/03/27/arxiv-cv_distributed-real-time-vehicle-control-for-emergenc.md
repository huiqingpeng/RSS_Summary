---
title: "Distributed Real-Time Vehicle Control for Emergency Vehicle Transit: A Scalable Cooperative Method"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.25000"
published: "2026-03-27"
fetched: "2026-03-28T07:19:55.489185"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 26 Mar 2026]
Title:Distributed Real-Time Vehicle Control for Emergency Vehicle Transit: A Scalable Cooperative Method
View PDF HTML (experimental)Abstract:Rapid transit of emergency vehicles is critical for saving lives and reducing property loss but often relies on surrounding ordinary vehicles to cooperatively adjust their driving behaviors. It is important to ensure rapid transit of emergency vehicles while minimizing the impact on ordinary vehicles. Centralized mathematical solver and reinforcement learning are the state-of-the-art methods. The former obtains optimal solutions but is only practical for small-scale scenarios. The latter implicitly learns through extensive centralized training but the trained model exhibits limited scalability to different traffic conditions. Hence, existing methods suffer from two fundamental limitations: high computational cost and lack of scalability. To overcome above limitations, this work proposes a scalable distributed vehicle control method, where vehicles adjust their driving behaviors in a distributed manner online using only local instead of global information. We proved that the proposed distributed method using only local information is approximately equivalent to the one using global information, which enables vehicles to evaluate their candidate states and make approximately optimal decisions in real time without pre-training and with natural adaptability to varying traffic conditions. Then, a distributed conflict resolution mechanism is further proposed to guarantee vehicles' safety by avoiding their decision conflicts, which eliminates the single-point-of-failure risk of centralized methods and provides deterministic safety guarantees that learned methods cannot offer. Compared with existing methods, simulation experiments based on real-world traffic datasets demonstrate that the proposed method achieves faster decision-making, less impact on ordinary vehicles, and maintains much stronger scalability across different traffic densities and road configurations.
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
