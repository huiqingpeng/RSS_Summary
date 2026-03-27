---
title: "Towards Safe Learning-Based Non-Linear Model Predictive Control through Recurrent Neural Network Modeling"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24503"
published: "2026-03-27"
fetched: "2026-03-28T07:10:45.349267"
---

Computer Science > Machine Learning
[Submitted on 25 Mar 2026]
Title:Towards Safe Learning-Based Non-Linear Model Predictive Control through Recurrent Neural Network Modeling
View PDF HTML (experimental)Abstract:The practical deployment of nonlinear model predictive control (NMPC) is often limited by online computation: solving a nonlinear program at high control rates can be expensive on embedded hardware, especially when models are complex or horizons are long. Learning-based NMPC approximations shift this computation offline but typically demand large expert datasets and costly training. We propose Sequential-AMPC, a sequential neural policy that generates MPC candidate control sequences by sharing parameters across the prediction horizon. For deployment, we wrap the policy in a safety-augmented online evaluation and fallback mechanism, yielding Safe Sequential-AMPC. Compared to a naive feedforward policy baseline across several benchmarks, Sequential-AMPC requires substantially fewer expert MPC rollouts and yields candidate sequences with higher feasibility rates and improved closed-loop safety. On high-dimensional systems, it also exhibits better learning dynamics and performance in fewer epochs while maintaining stable validation improvement where the feedforward baseline can stagnate.
Submission history
From: Mihaela-Larisa Clement [view email][v1] Wed, 25 Mar 2026 16:43:11 UTC (1,590 KB)
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
