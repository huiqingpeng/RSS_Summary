---
title: "Towards Effective Experiential Learning: Dual Guidance for Utilization and Internalization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24093"
published: "2026-03-26"
fetched: "2026-03-27T07:20:12.240706"
---

Computer Science > Machine Learning
[Submitted on 25 Mar 2026]
Title:Towards Effective Experiential Learning: Dual Guidance for Utilization and Internalization
View PDFAbstract:Recently, reinforcement learning~(RL) has become an important approach for improving the capabilities of large language models~(LLMs). In particular, reinforcement learning from verifiable rewards~(RLVR) has emerged as a promising paradigm for reasoning tasks. However, existing RL-based training still remains only a rough approximation to human learning. Human learners leverage both external and internal experience to guide exploration and gradually internalize useful trajectories into stable knowledge. Motivated by this gap, we ask: how can LLMs better utilize and internalize experience during RLVR training? To answer this question, we propose \textbf{D}ual \textbf{G}uidance \textbf{O}ptimization~(\textbf{DGO}), a unified framework that leverages \emph{external} and \emph{internal experience} to improve training effectiveness. Specifically, DGO first constructs an experience bank from previously explored trajectories. The policy then performs exploration under the joint guidance of the experience bank and the model's internal knowledge. The resulting trajectories are further used to refine the experience bank and optimize model parameters, forming a closed loop of experience utilization and internalization. Experiments show that DGO consistently outperforms baseline methods, suggesting that better utilization and internalization of experience lead to more effective reasoning.
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
