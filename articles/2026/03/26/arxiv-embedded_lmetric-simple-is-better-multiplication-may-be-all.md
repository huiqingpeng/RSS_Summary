---
title: "LMetric: Simple is Better - Multiplication May Be All You Need for LLM Request Scheduling"
source: "arXiv Embedded Systems"
url: "https://arxiv.org/abs/2603.15202"
published: "2026-03-26"
fetched: "2026-03-27T07:12:29.987617"
---

Computer Science > Distributed, Parallel, and Cluster Computing
[Submitted on 16 Mar 2026 (v1), last revised 25 Mar 2026 (this version, v2)]
Title:LMetric: Simple is Better - Multiplication May Be All You Need for LLM Request Scheduling
View PDF HTML (experimental)Abstract:High-quality LLM request scheduling requires achieving two key objectives: whether the routed instance has KV$ to accelerate the request execution and whether the workload is balanced across instances. Achieving both objectives is challenging because pursuing one objective may compromise the other. Current approaches adopt various combinators (e.g., linear combinations) to compute a scheduling score combining indicators for the two objectives, which are complex in that they either require significant workload-specific hyperparameter tuning or model-hardware-aware simulator development, and could still lead to suboptimal performance. In this paper, we show that using a simple multiplication of two carefully chosen indicators-one for KV$-aware (new prefill tokens if routed to an instance) and one for load balancing-aware (current batch size of the instance)-as the scheduling score can simultaneously achieve both objectives well without any hyperparameter tuning. The key idea is that the multiplied score considers both objectives in a manner similar to a linear combination, with a nice property that the original hyperparameters are canceled out during comparison so we don't need tuning to find the best parameters. The two indicators are chosen based on our analysis of LLM characteristics, and our extensive experiments show that this simple approach can reduce TTFT by 92% and 52%, and TPOT by 21% and 20%, compared to vLLM-v1 and a production scheduler on real-world workloads covering chatbots, API calls, and coding agents. We also mathematically derive the conditions under which multiplication may fail, and find that such conditions are extremely rare in practice and can be detected (and mitigated) beforehand.
Submission history
From: Dingyan Zhang [view email][v1] Mon, 16 Mar 2026 12:43:32 UTC (3,468 KB)
[v2] Wed, 25 Mar 2026 05:01:41 UTC (3,430 KB)
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
