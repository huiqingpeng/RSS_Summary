---
title: "Expert Streaming: Accelerating Low-Batch MoE Inference via Multi-chiplet Architecture and Dynamic Expert Trajectory Scheduling"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.27624"
published: "2026-03-31"
fetched: "2026-04-01T07:15:56.645923"
---

Computer Science > Hardware Architecture
[Submitted on 29 Mar 2026]
Title:Expert Streaming: Accelerating Low-Batch MoE Inference via Multi-chiplet Architecture and Dynamic Expert Trajectory Scheduling
View PDF HTML (experimental)Abstract:Mixture-of-Experts is a promising approach for edge AI with low-batch inference. Yet, on-device deployments often face limited on-chip memory and severe workload imbalance; the prevalent use of offloading further incurs off-chip memory access bottlenecks. Moreover, MoE sparsity and dynamic gating shift distributed strategies toward much finer granularity and introduce runtime scheduling considerations. Recently, high die-to-die bandwidth chiplet interconnects have created new opportunities for multi-chiplet systems to address workload imbalance and offloading bottlenecks with fine-grained scheduling. In this paper, we propose Fully Sharded Expert Data Parallelism, a parallelization paradigm specifically architected for low-batch MoE inference on multi-chiplet accelerators. FSE-DP attains adaptive computation-communication overlap and balanced load by orchestrating fine-grained, complementary expert streams along dynamic trajectories across high-bandwidth D2D links. The attendant dataflow complexity is tamed by a minimal, hardware-amenable set of virtualization rules and a lightweight scheduling algorithm. Our approach achieves 1.22 to 2.00 times speedup over state-of-the-art baselines and saves up to 78.8 percent on-chip memory.
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
