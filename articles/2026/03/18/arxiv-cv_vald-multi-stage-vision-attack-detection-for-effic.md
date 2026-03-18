---
title: "VALD: Multi-Stage Vision Attack Detection for Efficient LVLM Defense"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2602.19570"
published: "2026-03-18"
fetched: "2026-03-18T18:32:31.784328"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 23 Feb 2026 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:VALD: Multi-Stage Vision Attack Detection for Efficient LVLM Defense
View PDF HTML (experimental)Abstract:Large Vision-Language Models (LVLMs) can be vulnerable to adversarial images that subtly bias their outputs toward plausible yet incorrect responses. We introduce a general, efficient, and training-free defense that combines image transformations with agentic data consolidation to recover correct model behavior. A key component of our approach is a two-stage detection mechanism that quickly filters out the majority of clean inputs. We first assess image consistency under content-preserving transformations at negligible computational cost. For more challenging cases, we examine discrepancies in a text-embedding space. Only when necessary do we invoke a powerful LLM to resolve attack-induced divergences. A key idea is to consolidate multiple responses, leveraging both their similarities and their differences. We show that our method achieves state-of-the-art accuracy while maintaining notable efficiency: most clean images skip costly processing, and even in the presence of numerous adversarial examples, the overhead remains minimal.
Submission history
From: Nadav Kadvil [view email][v1] Mon, 23 Feb 2026 07:39:43 UTC (2,345 KB)
[v2] Tue, 17 Mar 2026 11:20:48 UTC (3,306 KB)
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
