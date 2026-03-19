---
title: "EchoGen: Cycle-Consistent Learning for Unified Layout-Image Generation and Understanding"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18001"
published: "2026-03-19"
fetched: "2026-03-19T16:20:30.145587"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:EchoGen: Cycle-Consistent Learning for Unified Layout-Image Generation and Understanding
View PDF HTML (experimental)Abstract:In this work, we present EchoGen, a unified framework for layout-to-image generation and image grounding, capable of generating images with accurate layouts and high fidelity to text descriptions (e.g., spatial relationships), while grounding the image robustly at the same time. We believe that image grounding possesses strong text and layout understanding abilities, which can compensate for the corresponding limitations in layout-to-image generation. At the same time, images generated from layouts exhibit high diversity in content, thereby enhancing the robustness of image grounding. Jointly training both tasks within a unified model can promote performance improvements for each. However, we identify that this joint training paradigm encounters several optimization challenges and results in restricted performance. To address these issues, we propose progressive training strategies. First, the Parallel Multi-Task Pre-training (PMTP) stage equips the model with basic abilities for both tasks, leveraging shared tokens to accelerate training. Next, the Dual Joint Optimization (DJO) stage exploits task duality to sequentially integrate the two tasks, enabling unified optimization. Finally, the Cycle RL stage eliminates reliance on visual supervision by using consistency constraints as rewards, significantly enhancing the model's unified capabilities via the GRPO strategy. Extensive experiments demonstrate state-of-the-art results on both layout-to-image generation and image grounding benchmarks, and reveal clear synergistic gains from optimizing the two tasks together.
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
