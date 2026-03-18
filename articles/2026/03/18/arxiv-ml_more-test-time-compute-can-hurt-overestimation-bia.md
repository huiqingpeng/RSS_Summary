---
title: "More Test-Time Compute Can Hurt: Overestimation Bias in LLM Beam Search"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15377"
published: "2026-03-18"
fetched: "2026-03-18T17:07:49.815738"
---

Computer Science > Machine Learning
[Submitted on 16 Mar 2026 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:More Test-Time Compute Can Hurt: Overestimation Bias in LLM Beam Search
View PDF HTML (experimental)Abstract:Wider beam search should improve LLM reasoning, but when should you stop widening? Prior work on beam width selection has focused on inference efficiency \citep{qin2025dsbd, freitag2017beam}, without analyzing whether wider search can \emph{hurt} output quality. We present an analysis, grounded in Extreme Value Theory, that answers this question. Beam selection over noisy scorer outputs introduces a systematic overestimation bias that grows with the candidate pool size, and we derive a maximum useful beam width $\hat{k}$ beyond which search degrades performance. This critical width depends on the signal-to-noise ratio of the scorer: $\hat{k}$ grows exponentially with $(\Delta/\sigma)^2$, where $\Delta > 0$ is the quality advantage of correct paths over incorrect ones and $\sigma$ is the scorer noise. We validate this theory by comparing perplexity-guided and PRM-guided beam search across three 7B-parameter models and ten domains on MR-BEN (5,975 questions). Perplexity scoring, with its high noise, yields $\hat{k} = 1$: search provides no benefit at any width tested. PRM scoring, with lower noise, yields $\hat{k} \geq 4$, with gains of up to 8.9 percentage points. The same model, the same algorithm, but different scorers place $\hat{k}$ at opposite ends of the beam width range. Our analysis identifies the scorer's signal-to-noise ratio as the key quantity governing beam width selection, and we propose diagnostic indicators for choosing the beam width in practice.
Submission history
From: Gal Dalal [view email][v1] Mon, 16 Mar 2026 14:51:30 UTC (234 KB)
[v2] Tue, 17 Mar 2026 15:04:49 UTC (234 KB)
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
