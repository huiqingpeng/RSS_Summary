---
title: "Semantic Identity Compression: Exact Zero-Error Laws, Rate-Distortion, and Neurosymbolic Necessity"
source: "arXiv Information Theory"
url: "https://arxiv.org/abs/2601.14252"
published: "2026-03-18"
fetched: "2026-03-18T19:10:07.745650"
---

Computer Science > Information Theory
[Submitted on 20 Jan 2026 (v1), last revised 16 Mar 2026 (this version, v4)]
Title:Semantic Identity Compression: Exact Zero-Error Laws, Rate-Distortion, and Neurosymbolic Necessity
View PDF HTML (experimental)Abstract:Symbolic systems operate over exact identities: variables denote specific objects, pointers target precise memory locations, and database keys refer to singular records. Neural embeddings generalize by compressing away semantic detail, but this compression creates collision ambiguity: multiple distinct entities can share the same representation value. We characterize exactly how much additional information must be supplied to recover precise identity from such representations.
The answer is controlled by a single combinatorial object: the collision-fiber geometry of the representation map $\pi$. Let $A_{\pi}=\max_u |\pi^{-1}(u)|$ be the largest collision fiber. We prove a tight fixed-length converse $L \ge \log_2 A_{\pi}$, an exact finite-block scaling law, a pointwise adaptive budget $\lceil \log_2 |\pi^{-1}(u)|\rceil$, and the rate-distortion tradeoff with an explicit distortion floor when identity bits are withheld. The same fiber geometry determines query complexity and canonical structure for distinguishing families.
Because this residual ambiguity is structural rather than representation-specific, symbolic identity mechanisms (handles, keys, pointers, nominal tags) are the necessary system-level complement to any non-injective semantic representation. All main results are machine-checked in Lean 4. Keywords: semantics-aware compression, zero-error coding, neurosymbolic systems, learned representations, side information
Submission history
From: Tristan Simas [view email][v1] Tue, 20 Jan 2026 18:58:51 UTC (177 KB)
[v2] Thu, 22 Jan 2026 01:11:26 UTC (177 KB)
[v3] Fri, 20 Feb 2026 21:52:16 UTC (196 KB)
[v4] Mon, 16 Mar 2026 23:06:17 UTC (373 KB)
Current browse context:
cs.IT
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
