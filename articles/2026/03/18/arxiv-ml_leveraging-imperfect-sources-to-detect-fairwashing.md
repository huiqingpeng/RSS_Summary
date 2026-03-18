---
title: "Leveraging Imperfect Sources to Detect Fairwashing in Black-Box Auditing"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2305.13883"
published: "2026-03-18"
fetched: "2026-03-18T16:15:28.001067"
---

Computer Science > Machine Learning
[Submitted on 23 May 2023 (v1), last revised 16 Mar 2026 (this version, v3)]
Title:Leveraging Imperfect Sources to Detect Fairwashing in Black-Box Auditing
View PDF HTML (experimental)Abstract:Algorithmic auditing has become central to platform accountability under frameworks such as the AI Act and the Digital Services Act. In practice, this obligation is discharged through dedicated Audit APIs. This architecture creates a paradox: the entity under scrutiny controls the evaluation interface. A platform facing legal sanctions can serve a compliant surrogate model on its Audit API, while running a discriminatory production system. This deceptive practice is known as fairwashing. Manipulation is undetectable if the auditor relies on only one source. To address this limitation, we introduce the Two-Source Audit Model (2SAM). This model cross-references the Audit API with an independent trusted stream. The key insight is that the trusted stream does not need to be perfectly aligned with the Audit API. We introduce a consistency proxy, a probabilistic mapping that can reconcile discrepancies between sources. This approach yields three results. First, we quantify the rate of manipulation above which a single-source auditor is blind. Second, we show how proxy quality governs detection power. Third, we provide a closed-form budget condition guaranteeing detection at any target confidence level, closing the blind spot mentioned above. We validate 2SAM on the UCI Adult dataset, achieving $70\%$ detection power with as few as $127$ cross-verification queries out of a total budget of $750$, using a name-based gender proxy with $94.2\%$ accuracy.
Submission history
From: Jade Garcia Bourrée [view email][v1] Tue, 23 May 2023 10:06:22 UTC (355 KB)
[v2] Tue, 10 Jun 2025 12:30:27 UTC (576 KB)
[v3] Mon, 16 Mar 2026 10:30:53 UTC (100 KB)
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
