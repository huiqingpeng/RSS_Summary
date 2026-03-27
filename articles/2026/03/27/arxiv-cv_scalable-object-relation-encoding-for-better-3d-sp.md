---
title: "Scalable Object Relation Encoding for Better 3D Spatial Reasoning in Large Language Models"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.24721"
published: "2026-03-27"
fetched: "2026-03-28T07:15:41.464255"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 25 Mar 2026]
Title:Scalable Object Relation Encoding for Better 3D Spatial Reasoning in Large Language Models
View PDF HTML (experimental)Abstract:Spatial reasoning focuses on locating target objects based on spatial relations in 3D scenes, which plays a crucial role in developing intelligent embodied agents. Due to the limited availability of 3D scene-language paired data, it is challenging to train models with strong reasoning ability from scratch. Previous approaches have attempted to inject 3D scene representations into the input space of Large Language Models (LLMs) and leverage the pretrained comprehension and reasoning abilities for spatial reasoning. However, models encoding absolute positions struggle to extract spatial relations from prematurely fused features, while methods explicitly encoding all spatial relations (which is quadratic in the number of objects) as input tokens suffer from poor scalability. To address these limitations, we propose QuatRoPE, a novel positional embedding method with an input length that is linear to the number of objects, and explicitly calculates pairwise spatial relations through the dot product in attention layers. QuatRoPE's holistic vector encoding of 3D coordinates guarantees a high degree of spatial consistency, maintaining fidelity to the scene's geometric integrity. Additionally, we introduce the Isolated Gated RoPE Extension (IGRE), which effectively limits QuatRoPE's influence to object-related tokens, thereby minimizing interference with the LLM's existing positional embeddings and maintaining the LLM's original capabilities. Extensive experiments demonstrate the effectiveness of our approaches. The code and data are available at this https URL.
Current browse context:
cs.CV
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
