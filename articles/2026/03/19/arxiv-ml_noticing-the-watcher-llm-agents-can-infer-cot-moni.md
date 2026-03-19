---
title: "Noticing the Watcher: LLM Agents Can Infer CoT Monitoring from Blocking Feedback"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16928"
published: "2026-03-19"
fetched: "2026-03-19T13:06:20.976322"
---

Computer Science > Cryptography and Security
[Submitted on 14 Mar 2026]
Title:Noticing the Watcher: LLM Agents Can Infer CoT Monitoring from Blocking Feedback
View PDF HTML (experimental)Abstract:Chain-of-thought (CoT) monitoring is proposed as a method for overseeing the internal reasoning of language-model agents. Prior work has shown that when models are explicitly informed that their reasoning is being monitored, or are fine-tuned to internalize this fact, they may learn to obfuscate their CoTs in ways that allow them to evade CoT-based monitoring systems. We ask whether reasoning agents can autonomously infer that their supposedly private CoT is under surveillance, and whether this awareness leads to strategic evasion, without any explicit training or instructions. In a multi-episode agentic framework, models pursue both a primary task and a concealed side task while being told that their reasoning is private; a hidden CoT monitor blocks episodes when suspicious reasoning is detected. We find that frontier models can deduce the existence of this monitor purely from blocking feedback, with the most capable models reaching a confident belief that their thinking is observed in up to 19% of episodes. This awareness scales with model capability and, in rare cases, escalates to an explicit intent to suppress reasoning about the side task. However, models that form this intent uniformly fail to execute it, openly reasoning about their concealed objectives in the very next episode. This intent-capability gap is reassuring for current deployment, but the autonomous emergence of both monitoring awareness and evasion intent suggests that CoT monitoring is not a permanently reliable safeguard.
Submission history
From: Flemming Kondrup Mr. [view email][v1] Sat, 14 Mar 2026 00:12:14 UTC (430 KB)
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
