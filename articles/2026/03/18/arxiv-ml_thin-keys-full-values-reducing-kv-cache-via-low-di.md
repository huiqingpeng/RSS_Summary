---
title: "Thin Keys, Full Values: Reducing KV Cache via Low-Dimensional Attention Selection"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.04427"
published: "2026-03-18"
fetched: "2026-03-18T17:05:05.781761"
---

Computer Science > Machine Learning
[Submitted on 16 Feb 2026 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:Thin Keys, Full Values: Reducing KV Cache via Low-Dimensional Attention Selection
View PDF HTML (experimental)Abstract:Standard transformer attention uses identical dimensionality for queries, keys, and values, yet these components serve
different roles: queries and keys produce scalar attention weights (selection), while values carry rich representations
(value transfer). We show that selection requires only $O(\log N)$ dimensions to distinguish among $N$ relevant token
categories (e.g., syntactic roles, semantic clusters, positional patterns) -- far fewer than value transfer needs.
We introduce factored keys, which exploit this asymmetry to physically shrink the KV cache of any pretrained model without
retraining from scratch -- unlike GQA and MLA, which must be designed into the architecture before pretraining. We factorize
each key projection $W_K \approx A_{d \times r} B_{r \times d}$ via truncated SVD (where $r = d_{\text{select}}$), set $W_K'
= A$ as the new key projection producing compact $r$-dimensional keys for the cache, and absorb $B^\top$ into the query
projection ($W_Q' = W_Q B^\top$) at zero cost -- since queries are never cached. At 7B scale, training from scratch with $r =
d_{\text{model}}/4$ matches full-attention perplexity (9.2 vs 9.3 PPL after 20B tokens) while using 12% fewer parameters and
training 8% faster. For existing models, SVD + QK fine-tuning (3 epochs, less than 1% of pretraining data) achieves 75% key
cache savings at approximately 2% quality cost on both GPT-2 and Mistral-7B. The approach composes with GQA and quantization
for up to $16\times$ combined key cache compression. For a 7B model serving 128K context, factored keys save 25 GB of KV
cache per user, enabling approximately 60% more concurrent users on identical hardware.
Submission history
From: Yao Hengshuai [view email][v1] Mon, 16 Feb 2026 23:45:39 UTC (16 KB)
[v2] Tue, 17 Mar 2026 17:54:04 UTC (39 KB)
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
