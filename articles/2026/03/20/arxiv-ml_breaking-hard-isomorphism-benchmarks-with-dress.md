---
title: "Breaking Hard Isomorphism Benchmarks with DRESS"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18582"
published: "2026-03-20"
fetched: "2026-03-20T13:14:56.938674"
---

Computer Science > Data Structures and Algorithms
[Submitted on 19 Mar 2026]
Title:Breaking Hard Isomorphism Benchmarks with DRESS
View PDF HTML (experimental)Abstract:In this paper we study the single-deletion variant $\Delta$-DRESS, part of the broader DRESS framework. We demonstrate empirically that $\Delta$-DRESS, a single level of vertex deletion applied to the DRESS graph fingerprint, achieves unique fingerprints within each tested SRG parameter family across all 51,718 non-isomorphic strongly regular graphs (SRGs) considered, spanning 16 parameter families: the complete Spence collection (12 families, 43,703 graphs on up to 64 vertices) plus four additional SRG families with up to 4,466 graphs per family. Combined with 18 additional hard graph families (102 graphs including Miyazaki, Chang, Paley, Latin square, and Steiner constructions), $\Delta$-DRESS achieves 100% within-family separation across 34 benchmark families covering 51,816 distinct graph instances, implicitly resolving over 576 million within-family non-isomorphic pairs. Moreover, the classical Rook $L_2(4)$ vs. Shrikhande pair, SRG(16,6,2,2), is known to be indistinguishable by the original 3-WL algorithm, yet $\Delta$-DRESS separates it, proving that $\Delta$-DRESS escapes the theoretical boundaries of 3-WL. The method runs in polynomial time $\mathcal{O}(n \cdot I \cdot m \cdot d_{\max})$ per graph; a streamed implementation of the combined fingerprint uses $\mathcal{O}(m + B + n)$ memory, where $B$ is the number of histogram bins, while the experiments reported here additionally retain the full deleted-subgraph multiset matrix for post-hoc analysis.
Submission history
From: Eduar Castrillo Velilla [view email][v1] Thu, 19 Mar 2026 07:41:16 UTC (15 KB)
Current browse context:
cs.DS
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
