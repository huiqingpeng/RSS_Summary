---
title: "PRISM: Breaking the O(n) Memory Wall in Long-Context LLM Inference via O(1) Photonic Block Selection"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.21576"
published: "2026-03-26"
fetched: "2026-03-27T07:13:53.477153"
---

Physics > Optics
[Submitted on 23 Mar 2026 (v1), last revised 25 Mar 2026 (this version, v2)]
Title:PRISM: Breaking the O(n) Memory Wall in Long-Context LLM Inference via O(1) Photonic Block Selection
View PDF HTML (experimental)Abstract:Long-context LLM inference is bottlenecked not by compute but by the O(n) memory bandwidth cost of scanning the KV cache at every decode step -- a wall that no amount of arithmetic scaling can break. Recent photonic accelerators have demonstrated impressive throughput for dense attention computation; however, these approaches inherit the same O(n) memory scaling as electronic attention when applied to long contexts. We observe that the real leverage point is the coarse block-selection step: a memory-bound similarity search that determines which KV blocks to fetch. We identify, for the first time, that this task is structurally matched to the photonic broadcast-and-weight paradigm -- the query fans out to all candidates via passive splitting, signatures are quasi-static (matching electro-optic MRR programming), and only rank order matters (relaxing precision to 4-6 bits). Crucially, the photonic advantage grows with context length: as N increases, the electronic scan cost rises linearly while the photonic evaluation remains O(1). We instantiate this insight in PRISM (Photonic Ranking via Inner-product Similarity with Microring weights), a thin-film lithium niobate (TFLN) similarity engine. Hardware-impaired needle-in-a-haystack evaluation on Qwen2.5-7B confirms 100% accuracy from 4K through 64K tokens at k=32, with 16x traffic reduction at 64K context. PRISM achieves a four-order-of-magnitude energy advantage over GPU baselines at practical context lengths (n >= 4K).
Submission history
From: Hyoseok Park [view email][v1] Mon, 23 Mar 2026 04:55:56 UTC (883 KB)
[v2] Wed, 25 Mar 2026 10:38:21 UTC (874 KB)
Current browse context:
physics.optics
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
