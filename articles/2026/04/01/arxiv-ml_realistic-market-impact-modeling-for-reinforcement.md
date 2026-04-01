---
title: "Realistic Market Impact Modeling for Reinforcement Learning Trading Environments"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.29086"
published: "2026-04-01"
fetched: "2026-04-02T07:15:03.329833"
---

Computer Science > Machine Learning
[Submitted on 30 Mar 2026]
Title:Realistic Market Impact Modeling for Reinforcement Learning Trading Environments
View PDF HTML (experimental)Abstract:Reinforcement learning (RL) has shown promise for trading, yet most open-source backtesting environments assume negligible or fixed transaction costs, causing agents to learn trading behaviors that fail under realistic execution. We introduce three Gymnasium-compatible trading environments -- MACE (Market-Adjusted Cost Execution) stock trading, margin trading, and portfolio optimization -- that integrate nonlinear market impact models grounded in the Almgren-Chriss framework and the empirically validated square-root impact law. Each environment provides pluggable cost models, permanent impact tracking with exponential decay, and comprehensive trade-level logging. We evaluate five DRL algorithms (A2C, PPO, DDPG, SAC, TD3) on the NASDAQ-100, comparing a fixed 10 bps baseline against the AC model with Optuna-tuned hyperparameters. Our results show that (i) the cost model materially changes both absolute performance and the relative ranking of algorithms across all three environments; (ii) the AC model produces dramatically different trading behavior, e.g., daily costs dropping from $200k to $8k with turnover falling from 19% to 1%; (iii) hyperparameter optimization is essential for constraining pathological trading, with costs dropping up to 82%; and (iv) algorithm-cost model interactions are strongly environment-specific, e.g., DDPG's OOS Sharpe jumps from -2.1 to 0.3 under AC in margin trading while SAC's drops from -0.5 to -1.2. We release the full suite as an open-source extension to FinRL-Meta.
Submission history
From: Lucas Riera Abbade [view email][v1] Mon, 30 Mar 2026 23:57:11 UTC (745 KB)
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
