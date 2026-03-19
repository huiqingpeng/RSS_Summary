---
title: "PaAgent: Portrait-Aware Image Restoration Agent via Subjective-Objective Reinforcement Learning"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17055"
published: "2026-03-19"
fetched: "2026-03-19T15:04:18.400810"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:PaAgent: Portrait-Aware Image Restoration Agent via Subjective-Objective Reinforcement Learning
View PDF HTML (experimental)Abstract:Image Restoration (IR) agents, leveraging multimodal large language models to perceive degradation and invoke restoration tools, have shown promise in automating IR tasks. However, existing IR agents typically lack an insight summarization mechanism for past interactions, which results in an exhaustive search for the optimal IR tool. To address this limitation, we propose a portrait-aware IR agent, dubbed PaAgent, which incorporates a self-evolving portrait bank for IR tools and Retrieval-Augmented Generation (RAG) to select a suitable IR tool for input. Specifically, to construct and evolve the portrait bank, the PaAgent continuously enriches it by summarizing the characteristics of various IR tools with restored images, selected IR tools, and degraded images. In addition, the RAG is employed to select the optimal IR tool for the input image by retrieving relevant insights from the portrait bank. Furthermore, to enhance PaAgent's ability to perceive degradation in complex scenes, we propose a subjective-objective reinforcement learning strategy that considers both image quality scores and semantic insights in reward generation, which accurately provides the degradation information even under partial and non-uniform degradation. Extensive experiments across 8 IR benchmarks, covering six single-degradation and eight mixed-degradation scenarios, validate PaAgent's superiority in addressing complex IR tasks. Our project page is \href{this https URL}{PaAgent}.
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
