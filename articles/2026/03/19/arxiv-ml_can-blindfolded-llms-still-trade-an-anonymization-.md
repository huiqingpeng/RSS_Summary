---
title: "Can Blindfolded LLMs Still Trade? An Anonymization-First Framework for Portfolio Optimization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17692"
published: "2026-03-19"
fetched: "2026-03-19T12:15:38.849155"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:Can Blindfolded LLMs Still Trade? An Anonymization-First Framework for Portfolio Optimization
View PDF HTML (experimental)Abstract:For LLM trading agents to be genuinely trustworthy, they must demonstrate understanding of market dynamics rather than exploitation of memorized ticker associations. Building responsible multi-agent systems demands rigorous signal validation: proving that predictions reflect legitimate patterns, not pre-trained recall. We address two sources of spurious performance: memorization bias from ticker-specific pre-training, and survivorship bias from flawed backtesting. Our approach is to blindfold the agents--anonymizing all identifiers--and verify whether meaningful signals persist. BlindTrade anonymizes tickers and company names, and four LLM agents output scores along with reasoning. We construct a GNN graph from reasoning embeddings and trade using PPO-DSR policy. On 2025 YTD (through 2025-08-01), we achieved Sharpe 1.40 +/- 0.22 across 20 seeds and validated signal legitimacy through negative control experiments. To assess robustness beyond a single OOS window, we additionally evaluate an extended period (2024--2025), revealing market-regime dependency: the policy excels in volatile conditions but shows reduced alpha in trending bull markets.
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
