---
title: "Generative Inverse Design with Abstention via Diagonal Flow Matching"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15925"
published: "2026-03-18"
fetched: "2026-03-18T15:37:36.258676"
---

Computer Science > Machine Learning
[Submitted on 16 Mar 2026]
Title:Generative Inverse Design with Abstention via Diagonal Flow Matching
View PDF HTML (experimental)Abstract:Inverse design aims to find design parameters $x$ achieving target performance $y^*$. Generative approaches learn bidirectional mappings between designs and labels, enabling diverse solution sampling. However, standard conditional flow matching (CFM), when adapted to inverse problems by pairing labels with design parameters, exhibits strong sensitivity to their arbitrary ordering and scaling, leading to unstable training. We introduce Diagonal Flow Matching (Diag-CFM), which resolves this through a zero-anchoring strategy that pairs design coordinates with noise and labels with zero, making the learning problem provably invariant to coordinate permutations. This yields order-of-magnitude improvements in round-trip accuracy over CFM and invertible neural network baselines across design dimensions up to $P{=}100$. We develop two architecture-intrinsic uncertainty metrics, Zero-Deviation and Self-Consistency, that enable three practical capabilities: selecting the best candidate among multiple generations, abstaining from unreliable predictions, and detecting out-of-distribution targets; consistently outperforming ensemble and general-purpose alternatives across all tasks. We validate on airfoil, gas turbine combustor, and an analytical benchmark with scalable design dimension.
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
