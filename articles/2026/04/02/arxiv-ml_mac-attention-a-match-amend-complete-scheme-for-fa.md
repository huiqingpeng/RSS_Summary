---
title: "MAC-Attention: a Match-Amend-Complete Scheme for Fast and Accurate Attention Computation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00235"
published: "2026-04-02"
fetched: "2026-04-03T07:19:02.656398"
---

Computer Science > Machine Learning
[Submitted on 31 Mar 2026]
Title:MAC-Attention: a Match-Amend-Complete Scheme for Fast and Accurate Attention Computation
View PDF HTML (experimental)Abstract:Long-context decoding in LLMs is IO-bound: each token re-reads an ever-growing KV cache. Prior accelerations cut bytes via compression, which lowers fidelity, or selection/eviction, which restricts what remains accessible, and both can degrade delayed recall and long-form generation. We introduce MAC-Attention, a fidelity- and access-preserving alternative that accelerates decoding by reusing prior attention computations for semantically similar recent queries. It starts with a match stage that performs pre-RoPE L2 matching over a short local window; an amend stage rectifies the reused attention by recomputing a small band near the match boundary; and a complete stage fuses the rectified results with fresh attention computed on the KV tail through a numerically stable merge. On a match hit, the compute and bandwidth complexity is constant regardless of context length. The method is model-agnostic and composes with IO-aware kernels, paged-KV managers, and MQA/GQA. Across LongBench v2 (120K), RULER (120K), and LongGenBench (16K continuous generation), compared to the latest FlashInfer library, MAC-Attention reduces KV accesses by up to 99%, cuts token generation latency by over 60% at 128K, and achieves over 14.3x attention-phase speedups, up to 2.6x end-to-end, while maintaining full-attention quality. By reusing computation, MAC-Attention delivers long-context inference that is both fast and faithful. Code is available here: this https URL
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
