---
title: "Meteorology-Driven GPT4AP: A Multi-Task Forecasting LLM for Atmospheric Air Pollution in Data-Scarce Settings"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.29974"
published: "2026-04-01"
fetched: "2026-04-02T07:21:18.812378"
---

Computer Science > Machine Learning
[Submitted on 31 Mar 2026]
Title:Meteorology-Driven GPT4AP: A Multi-Task Forecasting LLM for Atmospheric Air Pollution in Data-Scarce Settings
View PDF HTML (experimental)Abstract:Accurate forecasting of air pollution is important for environmental monitoring and policy support, yet data-driven models often suffer from limited generalization in regions with sparse observations. This paper presents Meteorology-Driven GPT for Air Pollution (GPT4AP), a parameter-efficient multi-task forecasting framework based on a pre-trained GPT-2 backbone and Gaussian rank-stabilized low-rank adaptation (rsLoRA). The model freezes the self-attention and feed-forward layers and adapts lightweight positional and output modules, substantially reducing the number of trainable parameters. GPT4AP is evaluated on six real-world air quality monitoring datasets under few-shot, zero-shot, and long-term forecasting settings. In the few-shot regime using 10% of the training data, GPT4AP achieves an average MSE/MAE of 0.686/0.442, outperforming DLinear (0.728/0.530) and ETSformer (0.734/0.505). In zero-shot cross-station transfer, the proposed model attains an average MSE/MAE of 0.529/0.403, demonstrating improved generalization compared with existing baselines. In long-term forecasting with full training data, GPT4AP remains competitive, achieving an average MAE of 0.429, while specialized time-series models show slightly lower errors. These results indicate that GPT4AP provides a data-efficient forecasting approach that performs robustly under limited supervision and domain shift, while maintaining competitive accuracy in data-rich settings.
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
