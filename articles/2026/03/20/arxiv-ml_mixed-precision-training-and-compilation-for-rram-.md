---
title: "Mixed-Precision Training and Compilation for RRAM-based Computing-in-Memory Accelerators"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2601.21737"
published: "2026-03-20"
fetched: "2026-03-20T14:10:12.109906"
---

Computer Science > Machine Learning
[Submitted on 29 Jan 2026 (v1), last revised 19 Mar 2026 (this version, v3)]
Title:Mixed-Precision Training and Compilation for RRAM-based Computing-in-Memory Accelerators
View PDFAbstract:Computing-in-Memory (CIM) accelerators are a promising solution for accelerating Machine Learning (ML) workloads, as they perform Matrix-Vector Multiplications (MVMs) on crossbar arrays directly in memory. Although the bit widths of the crossbar inputs and cells are very limited, most CIM compilers do not support quantization below 8 bit. As a result, a single MVM requires many compute cycles, and weights cannot be efficiently stored in a single crossbar cell. To address this problem, we propose a mixed-precision training and compilation framework for CIM architectures. The biggest challenge is the massive search space, that makes it difficult to find good quantization parameters. This is why we introduce a reinforcement learning-based strategy to find suitable quantization configurations that balance latency and accuracy. In the best case, our approach achieves up to a 2.48x speedup over existing state-of-the-art solutions, with an accuracy loss of only 0.086 %.
Submission history
From: Rebecca Pelke [view email][v1] Thu, 29 Jan 2026 13:54:55 UTC (417 KB)
[v2] Fri, 30 Jan 2026 13:40:21 UTC (417 KB)
[v3] Thu, 19 Mar 2026 09:56:31 UTC (417 KB)
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
