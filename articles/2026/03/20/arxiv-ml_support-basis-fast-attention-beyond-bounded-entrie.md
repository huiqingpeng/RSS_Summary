---
title: "Support Basis: Fast Attention Beyond Bounded Entries"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2510.01643"
published: "2026-03-20"
fetched: "2026-03-20T14:08:10.554732"
---

Computer Science > Machine Learning
[Submitted on 2 Oct 2025 (v1), last revised 19 Mar 2026 (this version, v2)]
Title:Support Basis: Fast Attention Beyond Bounded Entries
View PDFAbstract:Large language models (LLMs) have demonstrated remarkable performance across a wide range of tasks. However, the quadratic complexity of softmax attention remains a central bottleneck that limits their scalability. Alman and Song (NeurIPS 2023a; NeurIPS 2024a) proposed sub-quadratic time algorithms for attention inference and training, respectively, but they rely on the restrictive bounded-entry assumption. We show that this assumption rarely holds in practice, which significantly limits their applicability to modern LLMs.
In this paper, we introduce support-basis decomposition, a new technique for accurate and efficient attention inference and training without the bounded-entry assumption. We empirically show that the entries of the query and key matrices exhibit sub-Gaussian behavior. Leveraging this widely observed property, we perform exact computation on sparse components and polynomial approximation on dense components. Without relying on restrictive assumptions, we theoretically show that our algorithm achieves sub-quadratic runtime while matching the approximation error of prior work, and we empirically validate its computational efficiency and downstream task performance. We further generalize our method to a multi-threshold setting that eliminates all distributional assumptions, providing the first theoretical justification for the empirical success of polynomial attention. Moreover, we show that softmax attention can be closely approximated by multiple polynomial attentions with significantly smaller $\ell_p$ error.
Submission history
From: Junze Yin [view email][v1] Thu, 2 Oct 2025 03:51:28 UTC (533 KB)
[v2] Thu, 19 Mar 2026 02:39:27 UTC (776 KB)
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
