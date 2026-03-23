---
title: "The Residual Stream Is All You Need: On the Redundancy of the KV Cache in Transformer Inference"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19664"
published: "2026-03-23"
fetched: "2026-03-24T07:20:57.944536"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:The Residual Stream Is All You Need: On the Redundancy of the KV Cache in Transformer Inference
View PDF HTML (experimental)Abstract:The key-value (KV) cache is widely treated as essential state in transformer inference, and a large body of work engineers policies to compress, evict, or approximate its entries. We prove that this state is entirely redundant: keys and values at every layer are deterministic projections of the residual stream, and recomputing them from a single residual vector per token incurs exactly zero reconstruction error, not approximately, but bit-identically. We verify this across six models from four architecture families (135M to 4B parameters). Cross-task residual patching at every layer produces D_KL = 0 between patched and original output distributions, confirming that the residual stream satisfies a Markov property and is the sole information-carrying state. Removing the cache entirely and recomputing from scratch yields token-identical output under greedy decoding on all models tested. We build on this result with KV-Direct, a bounded-memory inference scheme that checkpoints residual vectors (5 KB per token on Gemma 3-4B) instead of full KV pairs (136 KB), recomputing keys and values on demand. Over 20 conversation turns, KV-Direct holds peak memory at 42 MB while the standard cache grows past 103 MB. Against five eviction baselines (H2O, StreamingLLM, SnapKV, TOVA, window-only), KV-Direct maintains 100% token match at every cache budget; all baselines degrade to 5-28%. A per-operation latency analysis shows recomputation runs up to 5x faster than reading cached tensors at moderate batch sizes. Code is available at this https URL.
Submission history
From: Kaleem Ullah Qasim [view email][v1] Fri, 20 Mar 2026 05:59:50 UTC (1,693 KB)
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
