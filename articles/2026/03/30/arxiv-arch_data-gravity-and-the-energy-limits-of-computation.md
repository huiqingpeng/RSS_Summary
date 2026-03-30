---
title: "Data Gravity and the Energy Limits of Computation"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.26053"
published: "2026-03-30"
fetched: "2026-03-31T07:05:53.665109"
---

Computer Science > Hardware Architecture
[Submitted on 27 Mar 2026]
Title:Data Gravity and the Energy Limits of Computation
View PDF HTML (experimental)Abstract:Unlike the von Neumann architecture, which separates computation from memory, the brain tightly integrates them, an organization that large language models increasingly resemble. The crucial difference lies in the ratio of energy spent on computation versus data access: in the brain, most energy fuels compute, while in von Neumann architectures, data movement dominates. To capture this imbalance, we introduce the \emph{operation-operand disjunction constant} $G_d$, a dimensionless measure of the energy required for data transport relative to computation. As part of this framework, we propose the metaphor of \emph{data gravity}: just as mass exerts gravitational pull, large and frequently accessed data sets attract computation. We develop expressions for optimal computation placement and show that bringing the computation closer to the data can reduce energy consumption by a factor of $G_d^{(\beta - 1)/2}$, where $\beta \in (1, 3)$ captures the empirically observed distance-dependent energy scaling. We demonstrate that these findings are consistent with measurements across processors from 45\,nm to 7\,nm, as well as with results from processing-in-memory (PIM) architectures. High $G_d$ values are limiting; as $G_d$ increases, the energy required for data movement threatens to stall progress, slowing the scaling of large language models and pushing modern computing toward a plateau. Unless computation is realigned with data gravity, the growth of AI may be capped not by algorithms but by physics.
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
