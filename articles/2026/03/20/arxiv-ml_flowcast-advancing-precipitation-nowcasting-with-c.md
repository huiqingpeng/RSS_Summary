---
title: "FlowCast: Advancing Precipitation Nowcasting with Conditional Flow Matching"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2511.09731"
published: "2026-03-20"
fetched: "2026-03-20T14:08:32.020553"
---

Computer Science > Machine Learning
[Submitted on 12 Nov 2025 (v1), last revised 19 Mar 2026 (this version, v4)]
Title:FlowCast: Advancing Precipitation Nowcasting with Conditional Flow Matching
View PDF HTML (experimental)Abstract:Radar-based precipitation nowcasting, the task of forecasting short-term precipitation fields from previous radar images, is a critical problem for flood risk management and decision-making. While deep learning has substantially advanced this field, two challenges remain fundamental: the uncertainty of atmospheric dynamics and the efficient modeling of high-dimensional data. Diffusion models have shown strong promise by producing sharp, reliable forecasts, but their iterative sampling process is computationally prohibitive for time-critical applications. We introduce FlowCast, the first end-to-end probabilistic model leveraging Conditional Flow Matching (CFM) as a direct noise-to-data generative framework for precipitation nowcasting. Unlike hybrid approaches, FlowCast learns a direct noise-to-data mapping in a compressed latent space, enabling rapid, high-fidelity sample generation. Our experiments demonstrate that FlowCast establishes a new state-of-the-art in probabilistic performance while also exceeding deterministic baselines in predictive accuracy. A direct comparison further reveals the CFM objective is both more accurate and significantly more efficient than a diffusion objective on the same architecture, maintaining high performance with significantly fewer sampling steps. This work positions CFM as a powerful and practical alternative for high-dimensional spatiotemporal forecasting.
Submission history
From: Bernardo Perrone Ribeiro [view email][v1] Wed, 12 Nov 2025 20:40:34 UTC (15,978 KB)
[v2] Sun, 7 Dec 2025 14:10:33 UTC (17,007 KB)
[v3] Sun, 22 Feb 2026 12:54:34 UTC (17,007 KB)
[v4] Thu, 19 Mar 2026 11:47:32 UTC (17,008 KB)
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
