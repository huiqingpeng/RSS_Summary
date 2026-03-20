---
title: "Off-Policy Learning with Limited Supply"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18702"
published: "2026-03-20"
fetched: "2026-03-20T12:14:56.694869"
---

Computer Science > Machine Learning
[Submitted on 19 Mar 2026]
Title:Off-Policy Learning with Limited Supply
View PDF HTML (experimental)Abstract:We study off-policy learning (OPL) in contextual bandits, which plays a key role in a wide range of real-world applications such as recommendation systems and online advertising. Typical OPL in contextual bandits assumes an unconstrained environment where a policy can select the same item infinitely. However, in many practical applications, including coupon allocation and e-commerce, limited supply constrains items through budget limits on distributed coupons or inventory restrictions on products. In these settings, greedily selecting the item with the highest expected reward for the current user may lead to early depletion of that item, making it unavailable for future users who could potentially generate higher expected rewards. As a result, OPL methods that are optimal in unconstrained settings may become suboptimal in limited supply settings. To address the issue, we provide a theoretical analysis showing that conventional greedy OPL approaches may fail to maximize the policy performance, and demonstrate that policies with superior performance must exist in limited supply settings. Based on this insight, we introduce a novel method called Off-Policy learning with Limited Supply (OPLS). Rather than simply selecting the item with the highest expected reward, OPLS focuses on items with relatively higher expected rewards compared to the other users, enabling more efficient allocation of items with limited supply. Our empirical results on both synthetic and real-world datasets show that OPLS outperforms existing OPL methods in contextual bandit problems with limited supply.
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
