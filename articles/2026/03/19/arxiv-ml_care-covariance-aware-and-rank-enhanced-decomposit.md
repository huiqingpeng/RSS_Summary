---
title: "CARE: Covariance-Aware and Rank-Enhanced Decomposition for Enabling Multi-Head Latent Attention"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17946"
published: "2026-03-19"
fetched: "2026-03-19T12:18:16.804291"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:CARE: Covariance-Aware and Rank-Enhanced Decomposition for Enabling Multi-Head Latent Attention
View PDF HTML (experimental)Abstract:Converting pretrained attention modules such as grouped-query attention (GQA) into multi-head latent attention (MLA) can improve expressivity without increasing KV-cache cost, making it attractive for efficient inference. However, many practical conversion baselines rely on weight-only low-rank approximations (e.g., SVD-style initializations) and uniform rank allocation. They focus on minimizing the difference between weight matrices rather than on how those weights affect input activations, ignore the covariance structure of activations, and enforce uniform rank across layers, causing activation drift and degraded attention fidelity. To address these issues, we propose CARE, a Covariance-Aware, Rank-Enhanced MLA conversion pipeline under a fixed KV width. CARE introduces three key steps: (i) activation-preserving factorization, which aligns the approximation with the actual input activations rather than just the weights; (ii) adjusted-rank allocation, which spreads a fixed KV budget across layers by giving more capacity to layers that need it most; and (iii) KV-parity mapping, which reparameterizes the converted K and V to fit the MLA format while keeping the KV-cache size unchanged. Our method outperforms a uniform-rank SVD baseline on Qwen3-4B/30B-A3B-Instruct-2507 and Llama-3.1-8B/70B-Instruct, reducing one-shot perplexity by up to 215x and improving mean accuracy by up to 1.70x at matched KV budgets. With a brief post-SVD healing fine-tune, we fully recover the original model's accuracy.
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
