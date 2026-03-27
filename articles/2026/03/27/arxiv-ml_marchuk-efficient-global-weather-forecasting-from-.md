---
title: "Marchuk: Efficient Global Weather Forecasting from Mid-Range to Sub-Seasonal Scales via Flow Matching"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24428"
published: "2026-03-27"
fetched: "2026-03-28T07:09:29.459012"
---

Computer Science > Machine Learning
[Submitted on 25 Mar 2026]
Title:Marchuk: Efficient Global Weather Forecasting from Mid-Range to Sub-Seasonal Scales via Flow Matching
View PDF HTML (experimental)Abstract:Accurate subseasonal weather forecasting remains a major challenge due to the inherently chaotic nature of the atmosphere, which limits the predictive skill of conventional models beyond the mid-range horizon (approximately 15 days). In this work, we present \textit{Marchuk}, a generative latent flow-matching model for global weather forecasting spanning mid-range to subseasonal timescales, with prediction horizons of up to 30 days. Marchuk conditions on current-day weather maps and autoregressively predicts subsequent days' weather maps within the learned latent space. We replace rotary positional encodings (RoPE) with trainable positional embeddings and extend the temporal context window, which together enhance the model's ability to represent and propagate long-range temporal dependencies during latent forecasting. Marchuk offers two key advantages: high computational efficiency and strong predictive performance. Despite its compact architecture of only 276 million parameters, the model achieves performance comparable to LaDCast, a substantially larger model with 1.6 billion parameters, while operating at significantly higher inference speeds. We open-source our inference code and model at: this https URL
Submission history
From: Arsen Kuzhamuratov [view email][v1] Wed, 25 Mar 2026 15:36:09 UTC (901 KB)
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
