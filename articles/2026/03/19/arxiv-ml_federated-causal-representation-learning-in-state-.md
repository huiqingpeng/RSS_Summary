---
title: "Federated Causal Representation Learning in State-Space Systems for Decentralized Counterfactual Reasoning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2602.19414"
published: "2026-03-19"
fetched: "2026-03-19T14:12:23.840676"
---

Computer Science > Machine Learning
[Submitted on 23 Feb 2026 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:Federated Causal Representation Learning in State-Space Systems for Decentralized Counterfactual Reasoning
View PDF HTML (experimental)Abstract:Networks of interdependent industrial assets (clients) are tightly coupled through physical processes and control inputs, raising a key question: how would the output of one client change if another client were operated differently? This is difficult to answer because client-specific data are high-dimensional and private, making centralization of raw data infeasible. Each client also maintains proprietary local models that cannot be modified. We propose a federated framework for causal representation learning in state-space systems that captures interdependencies among clients under these constraints. Each client maps high-dimensional observations into low-dimensional latent states that disentangle intrinsic dynamics from control-driven influences. A central server estimates the global state-transition and control structure. This enables decentralized counterfactual reasoning where clients predict how outputs would change under alternative control inputs at others while only exchanging compact latent states. We prove convergence to a centralized oracle and provide privacy guarantees. Our experiments demonstrate scalability, and accurate cross-client counterfactual inference on synthetic and real-world industrial control system datasets.
Submission history
From: Ayush Mohanty [view email][v1] Mon, 23 Feb 2026 01:12:21 UTC (5,831 KB)
[v2] Wed, 18 Mar 2026 00:18:23 UTC (6,458 KB)
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
