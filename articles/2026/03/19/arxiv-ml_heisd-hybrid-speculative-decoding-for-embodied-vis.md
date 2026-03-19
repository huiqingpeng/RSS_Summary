---
title: "HeiSD: Hybrid Speculative Decoding for Embodied Vision-Language-Action Models with Kinematic Awareness"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17573"
published: "2026-03-19"
fetched: "2026-03-19T13:13:51.090619"
---

Computer Science > Robotics
[Submitted on 18 Mar 2026]
Title:HeiSD: Hybrid Speculative Decoding for Embodied Vision-Language-Action Models with Kinematic Awareness
View PDF HTML (experimental)Abstract:Vision-Language-Action (VLA) Models have become the mainstream solution for robot control, but suffer from slow inference speeds. Speculative Decoding (SD) is a promising acceleration method which can be divided into two categories: drafter-based SD and retrieval-based SD. Existing methods fail to analyze the advantages and disadvantages of these two types of SD in VLA models, leading to their sole application or optimization. In this paper, we analyze the trajectory patterns of robots controlled by the VLA model and derive a key insight: the two types of SD should be used in a hybrid manner. However, achieving hybrid SD in VLA models poses several challenges: (1) draft rejection and persistent errors in retrieval-based SD; (2) difficulty in determining the hybrid boundary. To address these, we propose the HeiSD framework. We propose a retrieval-based SD optimization method in HeiSD,which contains a verify-skip mechanism and a sequence-wise relaxed acceptance strategy. Moreover, we proposed a kinematic-based fused metric in HeiSD to automatically determine the hybrid boundary. Experimental results demonstrate that HeiSD attains a speedup of up to 2.45x in simulation benchmarks and 2.06x~2.41x in real-world scenarios, while sustaining a high task success rate.
Current browse context:
cs.RO
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
