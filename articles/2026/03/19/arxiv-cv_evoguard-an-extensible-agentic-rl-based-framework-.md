---
title: "EvoGuard: An Extensible Agentic RL-based Framework for Practical and Evolving AI-Generated Image Detection"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17343"
published: "2026-03-19"
fetched: "2026-03-19T15:08:29.038782"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:EvoGuard: An Extensible Agentic RL-based Framework for Practical and Evolving AI-Generated Image Detection
View PDF HTML (experimental)Abstract:The rapid proliferation of AI-Generated Images (AIGIs) has introduced severe risks of misinformation, making AIGI detection a critical yet challenging task. While traditional detection paradigms mainly rely on low-level features, recent research increasingly focuses on leveraging the general understanding ability of Multimodal Large Language Models (MLLMs) to achieve better generalization, but still suffer from limited extensibility and expensive training data annotations. To better address complex and dynamic real-world environments, we propose EvoGuard, a novel agentic framework for AIGI detection. It encapsulates various state-of-the-art (SOTA) off-the-shelf MLLM and non-MLLM detectors as callable tools, and coordinates them through a capability-aware dynamic orchestration mechanism. Empowered by the agent's capacities for autonomous planning and reflection, it intelligently selects suitable tools for given samples, reflects intermediate results, and decides the next action, reaching a final conclusion through multi-turn invocation and reasoning. This design effectively exploits the complementary strengths among heterogeneous detectors, transcending the limits of any single model. Furthermore, optimized by a GRPO-based Agentic Reinforcement Learning algorithm using only low-cost binary labels, it eliminates the reliance on fine-grained annotations. Extensive experiments demonstrate that EvoGuard achieves SOTA accuracy while mitigating the bias between positive and negative samples. More importantly, it allows the plug-and-play integration of new detectors to boost overall performance in a train-free manner, offering a highly practical, long-term solution to ever-evolving AIGI threats. Source code will be publicly available upon acceptance.
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
