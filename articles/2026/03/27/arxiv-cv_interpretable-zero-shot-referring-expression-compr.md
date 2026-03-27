---
title: "Interpretable Zero-shot Referring Expression Comprehension with Query-driven Scene Graphs"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.25004"
published: "2026-03-27"
fetched: "2026-03-28T07:20:05.827686"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 26 Mar 2026]
Title:Interpretable Zero-shot Referring Expression Comprehension with Query-driven Scene Graphs
View PDF HTML (experimental)Abstract:Zero-shot referring expression comprehension (REC) aims to locate target objects in images given natural language queries without relying on task-specific training data, demanding strong visual understanding capabilities. Existing Vision-Language Models~(VLMs), such as CLIP, commonly address zero-shot REC by directly measuring feature similarities between textual queries and image regions. However, these methods struggle to capture fine-grained visual details and understand complex object relationships. Meanwhile, Large Language Models~(LLMs) excel at high-level semantic reasoning, their inability to directly abstract visual features into textual semantics limits their application in REC tasks. To overcome these limitations, we propose \textbf{SGREC}, an interpretable zero-shot REC method leveraging query-driven scene graphs as structured intermediaries. Specifically, we first employ a VLM to construct a query-driven scene graph that explicitly encodes spatial relationships, descriptive captions, and object interactions relevant to the given query. By leveraging this scene graph, we bridge the gap between low-level image regions and higher-level semantic understanding required by LLMs. Finally, an LLM infers the target object from the structured textual representation provided by the scene graph, responding with detailed explanations for its decisions that ensure interpretability in the inference process. Extensive experiments show that SGREC achieves top-1 accuracy on most zero-shot REC benchmarks, including RefCOCO val (66.78\%), RefCOCO+ testB (53.43\%), and RefCOCOg val (73.28\%), highlighting its strong visual scene understanding.
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
