---
title: "EmergeNav: Structured Embodied Inference for Zero-Shot Vision-and-Language Navigation in Continuous Environments"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16947"
published: "2026-03-19"
fetched: "2026-03-19T14:22:02.685198"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 16 Mar 2026]
Title:EmergeNav: Structured Embodied Inference for Zero-Shot Vision-and-Language Navigation in Continuous Environments
View PDF HTML (experimental)Abstract:Zero-shot vision-and-language navigation in continuous environments (VLN-CE) remains challenging for modern vision-language models (VLMs). Although these models encode useful semantic priors, their open-ended reasoning does not directly translate into stable long-horizon embodied execution. We argue that the key bottleneck is not missing knowledge alone, but missing an execution structure for organizing instruction following, perceptual grounding, temporal progress, and stage verification. We propose EmergeNav, a zero-shot framework that formulates continuous VLN as structured embodied inference. EmergeNav combines a Plan--Solve--Transition hierarchy for stage-structured execution, GIPE for goal-conditioned perceptual extraction, contrastive dual-memory reasoning for progress grounding, and role-separated Dual-FOV sensing for time-aligned local control and boundary verification. On VLN-CE, EmergeNav achieves strong zero-shot performance using only open-source VLM backbones and no task-specific training, explicit maps, graph search, or waypoint predictors, reaching 30.00 SR with Qwen3-VL-8B and 37.00 SR with Qwen3-VL-32B. These results suggest that explicit execution structure is a key ingredient for turning VLM priors into stable embodied navigation behavior.
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
