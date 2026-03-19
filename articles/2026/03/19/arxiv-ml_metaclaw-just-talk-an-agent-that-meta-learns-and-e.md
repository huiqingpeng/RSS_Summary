---
title: "MetaClaw: Just Talk -- An Agent That Meta-Learns and Evolves in the Wild"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17187"
published: "2026-03-19"
fetched: "2026-03-19T12:08:28.536798"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:MetaClaw: Just Talk -- An Agent That Meta-Learns and Evolves in the Wild
View PDF HTML (experimental)Abstract:Large language model (LLM) agents are increasingly used for complex tasks, yet deployed agents often remain static, failing to adapt as user needs evolve. This creates a tension between the need for continuous service and the necessity of updating capabilities to match shifting task distributions. On platforms like OpenClaw, which handle diverse workloads across 20+ channels, existing methods either store raw trajectories without distilling knowledge, maintain static skill libraries, or require disruptive downtime for retraining. We present MetaClaw, a continual meta-learning framework that jointly evolves a base LLM policy and a library of reusable behavioral skills. MetaClaw employs two complementary mechanisms. Skill-driven fast adaptation analyzes failure trajectories via an LLM evolver to synthesize new skills, enabling immediate improvement with zero downtime. Opportunistic policy optimization performs gradient-based updates via cloud LoRA fine-tuning and Reinforcement Learning with a Process Reward Model (RL-PRM). This is triggered during user-inactive windows by the Opportunistic Meta-Learning Scheduler (OMLS), which monitors system inactivity and calendar data. These mechanisms are mutually reinforcing: a refined policy generates better trajectories for skill synthesis, while richer skills provide higher-quality data for policy optimization. To prevent data contamination, a versioning mechanism separates support and query data. Built on a proxy-based architecture, MetaClaw scales to production-size LLMs without local GPUs. Experiments on MetaClaw-Bench and AutoResearchClaw show that skill-driven adaptation improves accuracy by up to 32% relative. The full pipeline advances Kimi-K2.5 accuracy from 21.4% to 40.6% and increases composite robustness by 18.3%. Code is available at this https URL.
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
