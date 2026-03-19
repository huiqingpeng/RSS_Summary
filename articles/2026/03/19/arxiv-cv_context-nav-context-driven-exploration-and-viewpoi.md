---
title: "Context-Nav: Context-Driven Exploration and Viewpoint-Aware 3D Spatial Reasoning for Instance Navigation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.09506"
published: "2026-03-19"
fetched: "2026-03-19T16:31:58.742555"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 10 Mar 2026 (v1), last revised 18 Mar 2026 (this version, v3)]
Title:Context-Nav: Context-Driven Exploration and Viewpoint-Aware 3D Spatial Reasoning for Instance Navigation
View PDF HTML (experimental)Abstract:Text-goal instance navigation (TGIN) asks an agent to resolve a single, free-form description into actions that reach the correct object instance among same-category distractors. We present \textit{Context-Nav}, which elevates long, contextual captions from a local matching cue to a global exploration prior and verifies candidates through 3D spatial reasoning. First, we compute dense text-image alignments for a value map that ranks frontiers -- guiding exploration toward regions consistent with the entire description rather than early detections. Second, upon observing a candidate, we perform a viewpoint-aware relation check: the agent samples plausible observer poses, aligns local frames, and accepts a target only if the spatial relations can be satisfied from at least one viewpoint. The pipeline requires no task-specific training or fine-tuning; we attain state-of-the-art performance on InstanceNav and CoIN-Bench. Ablations show that (i) encoding full captions into the value map avoids wasted motion and (ii) explicit, viewpoint-aware 3D verification prevents semantically plausible but incorrect stops. This suggests that geometry-grounded spatial reasoning is a scalable alternative to heavy policy training or human-in-the-loop interaction for fine-grained instance disambiguation in cluttered 3D scenes.
Submission history
From: Won Shik Jang [view email][v1] Tue, 10 Mar 2026 11:08:35 UTC (7,659 KB)
[v2] Wed, 11 Mar 2026 05:28:16 UTC (14,678 KB)
[v3] Wed, 18 Mar 2026 09:49:51 UTC (14,589 KB)
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
