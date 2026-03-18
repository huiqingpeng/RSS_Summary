---
title: "Flow Matching for Tabular Data Synthesis"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2512.00698"
published: "2026-03-18"
fetched: "2026-03-18T17:03:18.249560"
---

Computer Science > Machine Learning
[Submitted on 30 Nov 2025 (v1), last revised 16 Mar 2026 (this version, v3)]
Title:Flow Matching for Tabular Data Synthesis
View PDF HTML (experimental)Abstract:Synthetic data generation is an important tool for privacy-preserving data sharing. Although diffusion models have set recent benchmarks, flow matching (FM) offers a promising alternative. This paper presents different ways to implement FM for tabular data synthesis. We provide a comprehensive empirical study that compares flow matching (FM and variational FM) with a state-of-the-art diffusion method (TabDDPM and TabSyn) in tabular data synthesis. We evaluate both the standard Optimal Transport (OT) and the Variance Preserving (VP) probability paths, and also compare deterministic and stochastic samplers -- something possible when learning to generate using \textit{variational} FM -- characterising the empirical relationship between data utility and privacy risk. Our key findings reveal that FM, particularly TabbyFlow, outperforms diffusion baselines. Flow matching methods also achieve better performance with remarkably low function evaluations ($\leq$ 100 steps), offering a substantial computational advantage. The choice of probability path is also crucial, as using the OT is a strong default and more robust to early stopping on average, while VP has potential to produce synthetic data with lower privacy risk. Lastly, our results show that making flows stochastic not only preserves marginal distributions but, in some instances, enables the generation of high utility synthetic data with reduced disclosure risk. The implementation code associated with this paper is publicly available at this https URL.
Submission history
From: Bahrul Ilmi Nasution [view email][v1] Sun, 30 Nov 2025 02:18:04 UTC (135 KB)
[v2] Wed, 4 Feb 2026 10:33:41 UTC (149 KB)
[v3] Mon, 16 Mar 2026 19:53:48 UTC (146 KB)
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
