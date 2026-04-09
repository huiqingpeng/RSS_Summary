---
title: "Discrete Flow Matching Policy Optimization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.06491"
published: "2026-04-09"
fetched: "2026-04-10T07:05:01.426229"
---

Computer Science > Machine Learning
[Submitted on 7 Apr 2026]
Title:Discrete Flow Matching Policy Optimization
View PDF HTML (experimental)Abstract:We introduce Discrete flow Matching policy Optimization (DoMinO), a unified framework for Reinforcement Learning (RL) fine-tuning Discrete Flow Matching (DFM) models under a broad class of policy gradient methods. Our key idea is to view the DFM sampling procedure as a multi-step Markov Decision Process. This perspective provides a simple and transparent reformulation of fine-tuning reward maximization as a robust RL objective. Consequently, it not only preserves the original DFM samplers but also avoids biased auxiliary estimators and likelihood surrogates used by many prior RL fine-tuning methods. To prevent policy collapse, we also introduce new total-variation regularizers to keep the fine-tuned distribution close to the pretrained one. Theoretically, we establish an upper bound on the discretization error of DoMinO and tractable upper bounds for the regularizers. Experimentally, we evaluate DoMinO on regulatory DNA sequence design. DoMinO achieves stronger predicted enhancer activity and better sequence naturalness than the previous best reward-driven baselines. The regularization further improves alignment with the natural sequence distribution while preserving strong functional performance. These results establish DoMinO as an useful framework for controllable discrete sequence generation.
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
