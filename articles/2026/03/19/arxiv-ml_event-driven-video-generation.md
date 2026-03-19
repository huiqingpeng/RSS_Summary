---
title: "Event-Driven Video Generation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.13402"
published: "2026-03-19"
fetched: "2026-03-19T14:19:25.740994"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 12 Mar 2026 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:Event-Driven Video Generation
View PDF HTML (experimental)Abstract:State-of-the-art text-to-video models often look realistic frame-by-frame yet fail on simple interactions: motion starts before contact, actions are not realized, objects drift after placement, and support relations break. We argue this stems from frame-first denoising, which updates latent state everywhere at every step without an explicit notion of when and where an interaction is active. We introduce Event-Driven Video Generation (EVD), a minimal DiT-compatible framework that makes sampling event-grounded: a lightweight event head predicts token-aligned event activity, event-grounded losses couple activity to state change during training, and event-gated sampling (with hysteresis and early-step scheduling) suppresses spurious updates while concentrating updates during interactions. On EVD-Bench, EVD consistently improves human preference and VBench dynamics, substantially reducing failure modes in state persistence, spatial accuracy, support relations, and contact stability without sacrificing appearance. These results indicate that explicit event grounding is a practical abstraction for reducing interaction hallucinations in video generation.
Submission history
From: Chika Maduabuchi [view email][v1] Thu, 12 Mar 2026 00:16:56 UTC (3,115 KB)
[v2] Wed, 18 Mar 2026 16:49:27 UTC (3,331 KB)
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
