---
title: "HindSight: Evaluating LLM-Generated Research Ideas via Future Impact"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15164"
published: "2026-03-18"
fetched: "2026-03-18T17:17:22.996200"
---

Computer Science > Computation and Language
[Submitted on 16 Mar 2026 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:HindSight: Evaluating LLM-Generated Research Ideas via Future Impact
View PDF HTML (experimental)Abstract:Evaluating AI-generated research ideas typically relies on LLM judges or human panels -- both subjective and disconnected from actual research impact. We introduce HindSight, a time-split evaluation framework that measures idea quality by matching generated ideas against real future publications and scoring them by citation impact and venue acceptance. Using a temporal cutoff~$T$, we restrict an idea generation system to pre-$T$ literature, then evaluate its outputs against papers published in the subsequent 30 months. Experiments across 10 AI/ML research topics reveal a striking disconnect: LLM-as-Judge finds no significant difference between retrieval-augmented and vanilla idea generation ($p{=}0.584$), while HindSight shows the retrieval-augmented system produces 2.5$\times$ higher-scoring ideas ($p{<}0.001$). Moreover, HindSight scores are \emph{negatively} correlated with LLM-judged novelty ($\rho{=}{-}0.29$, $p{<}0.01$), suggesting that LLMs systematically overvalue novel-sounding ideas that never materialize in real research.
Submission history
From: Bo Jiang [view email][v1] Mon, 16 Mar 2026 11:59:24 UTC (71 KB)
[v2] Tue, 17 Mar 2026 13:42:43 UTC (92 KB)
Current browse context:
cs.CL
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
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
