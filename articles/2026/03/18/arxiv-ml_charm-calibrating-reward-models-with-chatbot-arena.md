---
title: "CHARM: Calibrating Reward Models With Chatbot Arena Scores"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2504.10045"
published: "2026-03-18"
fetched: "2026-03-18T17:09:42.221595"
---

Computer Science > Artificial Intelligence
[Submitted on 14 Apr 2025 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:CHARM: Calibrating Reward Models With Chatbot Arena Scores
View PDF HTML (experimental)Abstract:Reward models (RMs) play a crucial role in Reinforcement Learning from Human Feedback by serving as proxies for human preferences in aligning large language models. However, they suffer from various biases which could lead to reward hacking. In this paper, we identify a model preference bias in RMs, where they systematically assign disproportionately high scores to responses from certain policy models, leading to unfair judgments. To mitigate this bias, we propose a calibration method named CHatbot Arena calibrated Reward Modeling (CHARM) that leverages Elo scores from the Chatbot Arena to construct debiased preference datasets and adjust reward model scoring. We conduct extensive experiments on reward model benchmarks and human preference alignment. Results demonstrate that our calibrated RMs achieve improved evaluation accuracy on RM-Bench and the Chat-Hard domain of RewardBench, exhibit a stronger correlation with human preferences by producing scores more closely aligned with Elo rankings and improve downstream post-training performance. These results demonstrate that CHARM provides a simple, effective, and broadly applicable approach to building more reliable and fair reward models.
Submission history
From: Xiao Zhu [view email][v1] Mon, 14 Apr 2025 09:51:09 UTC (1,925 KB)
[v2] Tue, 17 Mar 2026 12:03:29 UTC (1,019 KB)
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
