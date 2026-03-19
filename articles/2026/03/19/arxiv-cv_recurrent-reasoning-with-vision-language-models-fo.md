---
title: "Recurrent Reasoning with Vision-Language Models for Estimating Long-Horizon Embodied Task Progress"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17312"
published: "2026-03-19"
fetched: "2026-03-19T15:08:04.130229"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:Recurrent Reasoning with Vision-Language Models for Estimating Long-Horizon Embodied Task Progress
View PDF HTML (experimental)Abstract:Accurately estimating task progress is critical for embodied agents to plan and execute long-horizon, multi-step tasks. Despite promising advances, existing Vision-Language Models (VLMs) based methods primarily leverage their video understanding capabilities, while neglecting their complex reasoning potential. Furthermore, processing long video trajectories with VLMs is computationally prohibitive for real-world deployment. To address these challenges, we propose the Recurrent Reasoning Vision-Language Model ($\text{R}^2$VLM). Our model features a recurrent reasoning framework that processes local video snippets iteratively, maintaining a global context through an evolving Chain of Thought (CoT). This CoT explicitly records task decomposition, key steps, and their completion status, enabling the model to reason about complex temporal dependencies. This design avoids the high cost of processing long videos while preserving essential reasoning capabilities. We train $\text{R}^2$VLM on large-scale, automatically generated datasets from ALFRED and Ego4D. Extensive experiments on progress estimation and downstream applications, including progress-enhanced policy learning, reward modeling for reinforcement learning, and proactive assistance, demonstrate that $\text{R}^2$VLM achieves strong performance and generalization, achieving a new state-of-the-art in long-horizon task progress estimation. The models and benchmarks are publicly available at \href{this https URL}{huggingface}.
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
