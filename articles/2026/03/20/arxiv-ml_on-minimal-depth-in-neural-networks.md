---
title: "On Minimal Depth in Neural Networks"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2402.15315"
published: "2026-03-20"
fetched: "2026-03-20T14:04:09.000790"
---

Computer Science > Machine Learning
[Submitted on 23 Feb 2024 (v1), last revised 19 Mar 2026 (this version, v5)]
Title:On Minimal Depth in Neural Networks
View PDF HTML (experimental)Abstract:Understanding the relationship between the depth of a neural network and its representational capacity is a central problem in deep learning theory. In this work, we develop a geometric framework to analyze the expressivity of ReLU networks with the notion of depth complexity for convex polytopes. The depth of a polytope recursively quantifies the number of alternating convex hull and Minkowski sum operations required to construct it. This geometric perspective serves as a rigorous tool for deriving depth lower bounds and understanding the structural limits of deep neural architectures.
We establish lower and upper bounds on the depth of polytopes, as well as tight bounds for classical families. These results yield two main consequences. First, we provide a purely geometric proof of the expressivity bound by Arora et al. (2018), confirming that $\lceil \log_2(n+1)\rceil$ hidden layers suffice to represent any continuous piecewise linear (CPWL) function. Second, we prove that, unlike general ReLU networks, convex polytopes do not admit a universal depth bound. Specifically, the depth of cyclic polytopes in dimensions $n \geq 4$ grows unboundedly with the number of vertices. This result implies that Input Convex Neural Networks (ICNNs) cannot represent all convex CPWL functions with a fixed depth, revealing a sharp separation in expressivity between ICNNs and standard ReLU networks.
Submission history
From: Juan Luis Valerdi Cabrera [view email][v1] Fri, 23 Feb 2024 13:34:03 UTC (17 KB)
[v2] Fri, 7 Jun 2024 10:30:42 UTC (19 KB)
[v3] Sun, 6 Oct 2024 09:02:32 UTC (19 KB)
[v4] Fri, 27 Feb 2026 13:56:38 UTC (124 KB)
[v5] Thu, 19 Mar 2026 14:21:32 UTC (14 KB)
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
