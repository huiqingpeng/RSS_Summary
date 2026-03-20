---
title: "Discounted Beta--Bernoulli Reward Estimation for Sample-Efficient Reinforcement Learning with Verifiable Rewards"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18444"
published: "2026-03-20"
fetched: "2026-03-20T12:11:41.381550"
---

Computer Science > Machine Learning
[Submitted on 19 Mar 2026]
Title:Discounted Beta--Bernoulli Reward Estimation for Sample-Efficient Reinforcement Learning with Verifiable Rewards
View PDF HTML (experimental)Abstract:Reinforcement learning with verifiable rewards (RLVR) has emerged as an effective post-training paradigm for improving the reasoning capabilities of large language models. However, existing group-based RLVR methods often suffer from severe sample inefficiency. This inefficiency stems from reliance on point estimation of rewards from a small number of rollouts, leading to high estimation variance, variance collapse, and ineffective utilization of generated responses. In this work, we reformulate RLVR from a statistical estimation perspective by modeling rewards as samples drawn from a policy-induced distribution and casting advantage computation as the problem of estimating the reward distribution from finite data. Building on this view, we propose Discounted Beta--Bernoulli (DBB) reward estimation, which leverages historical reward statistics for the non-stationary distribution. Although biased, the resulting estimator exhibits reduced and stable variance, theoretically avoids estimated variance collapse, and achieves lower mean squared error than standard point estimation. Extensive experiments across six in-distribution and three out-of-distribution reasoning benchmarks demonstrate that GRPO with DBB consistently outperforms naive GRPO, achieving average Acc@8 improvements of 3.22/2.42 points in-distribution and 12.49/6.92 points out-of-distribution on the 1.7B and 8B models, respectively, without additional computational cost or memory usage.
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
