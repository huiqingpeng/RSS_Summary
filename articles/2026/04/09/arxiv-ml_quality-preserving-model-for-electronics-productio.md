---
title: "Quality-preserving Model for Electronics Production Quality Tests Reduction"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.06451"
published: "2026-04-09"
fetched: "2026-04-10T07:04:59.578675"
---

Computer Science > Machine Learning
[Submitted on 7 Apr 2026]
Title:Quality-preserving Model for Electronics Production Quality Tests Reduction
View PDF HTML (experimental)Abstract:Manufacturing test flows in high-volume electronics production are typically fixed during product development and executed unchanged on every unit, even as failure patterns and process conditions evolve. This protects quality, but it also imposes unnecessary test cost, while existing data-driven methods mostly optimize static test subsets and neither adapt online to changing defect distributions nor explicitly control escape risk. In this study, we present an adaptive test-selection framework that combines offline minimum-cost diagnostic subset construction using greedy set cover with an online Thompson-sampling multi-armed bandit that switches between full and reduced test plans using a rolling process-stability signal. We evaluate the framework on two printed circuit board assembly stages-Functional Circuit Test and End-of-Line test-covering 28,000 board runs. Offline analysis identified zero-escape reduced plans that cut test time by 18.78% in Functional Circuit Test and 91.57\% in End-of-Line testing. Under temporal validation with real concept drift, static reduction produced 110 escaped defects in Functional Circuit Test and 8 in End-of-Line, whereas the adaptive policy reduced escapes to zero by reverting to fuller coverage when instability emerged in practice. These results show that online learning can preserve manufacturing quality while reducing test burden, offering a practical route to adaptive test planning across production domains, and offering both economic and logistics improvement for companies.
Submission history
From: Teddy Lazebnik Prof. [view email][v1] Tue, 7 Apr 2026 20:47:27 UTC (7,274 KB)
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
