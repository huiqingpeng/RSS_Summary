---
title: "Scaling Attention via Feature Sparsity"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22300"
published: "2026-03-25"
fetched: "2026-03-26T07:08:37.207471"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:Scaling Attention via Feature Sparsity
View PDF HTML (experimental)Abstract:Scaling Transformers to ultra-long contexts is bottlenecked by the $O(n^2 d)$ cost of self-attention. Existing methods reduce this cost along the sequence axis through local windows, kernel approximations, or token-level sparsity, but these approaches consistently degrade accuracy. In this paper, we instead explore an orthogonal axis: feature sparsity. We propose Sparse Feature Attention (SFA), where queries and keys are represented as $k$-sparse codes that preserve high-dimensional expressivity while reducing the cost of attention from $\Theta(n^2 d)$ to $\Theta(n^2 k^2/d)$. To make this efficient at scale, we introduce FlashSFA, an IO-aware kernel that extends FlashAttention to operate directly on sparse overlaps without materializing dense score matrices. Across GPT-2 and Qwen3 pretraining, SFA matches dense baselines while improving speed by up to $2.5\times$ and reducing FLOPs and KV-cache by nearly 50\%. On synthetic and downstream benchmarks, SFA preserves retrieval accuracy and robustness at long contexts, outperforming short-embedding baselines that collapse feature diversity. These results establish feature-level sparsity as a complementary and underexplored axis for efficient attention, enabling Transformers to scale to orders-of-magnitude longer contexts with minimal quality loss. Code is available at this https URL.
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
