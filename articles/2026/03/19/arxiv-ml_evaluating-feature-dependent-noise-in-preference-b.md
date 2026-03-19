---
title: "Evaluating Feature Dependent Noise in Preference-based Reinforcement Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2601.01904"
published: "2026-03-19"
fetched: "2026-03-19T14:10:52.795723"
---

Computer Science > Machine Learning
[Submitted on 5 Jan 2026 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:Evaluating Feature Dependent Noise in Preference-based Reinforcement Learning
View PDF HTML (experimental)Abstract:Learning from Preferences in Reinforcement Learning (PbRL) has gained attention recently, as it serves as a natural fit for complicated tasks where the reward function is not easily available. However, preferences often come with uncertainty and noise if they are not from perfect teachers. Much prior literature aimed to detect noise, but with limited types of noise and most being uniformly distributed with no connection to observations. In this work, we formalize the notion of targeted feature-dependent noise and propose several variants like trajectory feature noise, trajectory similarity noise, margin dependent noise, and Language Model noise. We evaluate feature-dependent noise, where noise is correlated with certain features in complex continuous control tasks from DMControl and Meta-world. Our experiments show that in some feature-dependent noise settings, the state-of-the-art noise-robust PbRL method's learning performance is significantly deteriorated, while PbRL method with no explicit denoising can surprisingly outperform noise-robust PbRL in the majority of settings. We also find language models' noise exhibits similar characteristics to feature-dependent noise, thereby simulating realistic humans and call for further study in learning with feature-dependent noise robustly.
Submission history
From: Yuxuan Li [view email][v1] Mon, 5 Jan 2026 08:49:30 UTC (9,607 KB)
[v2] Tue, 17 Mar 2026 19:33:09 UTC (13,876 KB)
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
