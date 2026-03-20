---
title: "Adaptive Regime-Aware Stock Price Prediction Using Autoencoder-Gated Dual Node Transformers with Reinforcement Learning Control"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19136"
published: "2026-03-20"
fetched: "2026-03-20T13:05:13.886074"
---

Computer Science > Machine Learning
[Submitted on 19 Mar 2026]
Title:Adaptive Regime-Aware Stock Price Prediction Using Autoencoder-Gated Dual Node Transformers with Reinforcement Learning Control
View PDF HTML (experimental)Abstract:Stock markets exhibit regime-dependent behavior where prediction models optimized for stable conditions often fail during volatile periods. Existing approaches typically treat all market states uniformly or require manual regime labeling, which is expensive and quickly becomes stale as market dynamics evolve. This paper introduces an adaptive prediction framework that adaptively identifies deviations from normal market conditions and routes data through specialized prediction pathways. The architecture consists of three components: (1) an autoencoder trained on normal market conditions that identifies anomalous regimes through reconstruction error, (2) dual node transformer networks specialized for stable and event-driven market conditions respectively, and (3) a Soft Actor-Critic reinforcement learning controller that adaptively tunes the regime detection threshold and pathway blending weights based on prediction performance feedback. The reinforcement learning component enables the system to learn adaptive regime boundaries, defining anomalies as market states where standard prediction approaches fail. Experiments on 20 S&P 500 stocks spanning 1982 to 2025 demonstrate that the proposed framework achieves 0.68% MAPE for one-day predictions without the reinforcement controller and 0.59% MAPE with the full adaptive system, compared to 0.80% for the baseline integrated node transformer. Directional accuracy reaches 72% with the complete framework. The system maintains robust performance during high-volatility periods, with MAPE below 0.85% when baseline models exceed 1.5%. Ablation studies confirm that each component contributes meaningfully: autoencoder routing accounts for 36% relative MAPE degradation upon removal, followed by the SAC controller at 15% and the dual-path architecture at 7%.
Submission history
From: Mohammad Al Ridhawi [view email][v1] Thu, 19 Mar 2026 16:55:33 UTC (2,345 KB)
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
