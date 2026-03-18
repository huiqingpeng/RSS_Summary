---
title: "FlowComposer: Composable Flows for Compositional Zero-Shot Learning"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16641"
published: "2026-03-18"
fetched: "2026-03-18T18:16:13.685668"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:FlowComposer: Composable Flows for Compositional Zero-Shot Learning
View PDF HTML (experimental)Abstract:Compositional zero-shot learning (CZSL) aims to recognize unseen attribute-object compositions by recombining primitives learned from seen pairs. Recent CZSL methods built on vision-language models (VLMs) typically adopt parameter-efficient fine-tuning (PEFT). They apply visual disentanglers for decomposition and manipulate token-level prompts or prefixes to encode compositions. However, such PEFT-based designs suffer from two fundamental limitations: (1) Implicit Composition Construction, where composition is realized only via token concatenation or branch-wise prompt tuning rather than an explicit operation in the embedding space; (2) Remained Feature Entanglement, where imperfect disentanglement leaves attribute, object, and composition features mutually contaminated. Together, these issues limit the generalization ability of current CZSL models. In this paper, we are the first to systematically study flow matching for CZSL and introduce FlowComposer, a model-agnostic framework that learns two primitive flows to transport visual features toward attribute and object text embeddings, and a learnable Composer that explicitly fuses their velocity fields into a composition flow. To exploit the inevitable residual entanglement, we further devise a leakage-guided augmentation scheme that reuses leaked features as auxiliary signals. We thoroughly evaluate FlowComposer on three public CZSL benchmarks by integrating it as a plug-and-play component into various baselines, consistently achieving significant improvements.
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
