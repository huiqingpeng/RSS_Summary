---
title: "A Survey of On-Policy Distillation for Large Language Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00626"
published: "2026-04-02"
fetched: "2026-04-03T07:23:10.345774"
---

Computer Science > Machine Learning
[Submitted on 1 Apr 2026]
Title:A Survey of On-Policy Distillation for Large Language Models
View PDF HTML (experimental)Abstract:Knowledge distillation has become a primary mechanism for transferring reasoning and domain expertise from frontier Large Language Models (LLMs) to smaller, deployable students. However, the dominant paradigm remains \textit{off-policy}: students train on static teacher-generated data and never encounter their own errors during learning. This train--test mismatch, an instance of \textit{exposure bias}, causes prediction errors to compound autoregressively at inference time. On-Policy Distillation (OPD) addresses this by letting the student generate its own trajectories and receive teacher feedback on these self-generated outputs, grounding distillation in the theory of interactive imitation learning. Despite rapid growth spanning divergence minimization, reward-guided learning, and self-play, the OPD literature remains fragmented with no unified treatment. This survey provides the first comprehensive overview of OPD for LLMs. We introduce a unified $f$-divergence framework over on-policy samples and organize the landscape along three orthogonal dimensions: \emph{feedback signal} (logit-based, outcome-based, or self-play), \emph{teacher access} (white-box, black-box, or teacher-free), and \emph{loss granularity} (token-level, sequence-level, or hybrid). We systematically analyze representative methods, examine industrial deployments, and identify open problems including distillation scaling laws, uncertainty-aware feedback, and agent-level distillation.
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
