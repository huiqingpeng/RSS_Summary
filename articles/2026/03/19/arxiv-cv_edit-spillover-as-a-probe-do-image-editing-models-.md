---
title: "Edit Spillover as a Probe: Do Image Editing Models Implicitly Understand World Relations?"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17876"
published: "2026-03-19"
fetched: "2026-03-19T16:17:39.194063"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:Edit Spillover as a Probe: Do Image Editing Models Implicitly Understand World Relations?
View PDF HTML (experimental)Abstract:Instruction-following image editing models are expected to modify only the specified region while keeping the rest of the image unchanged. However, in practice, we observe a pervasive phenomenon -- edit spillover: models alter semantically related but unspecified content outside the edit region. This raises a fundamental question -- does spillover reflect genuine implicit world understanding, or is it merely attention leakage? We propose EditSpilloverProbe, a systematic framework that repurposes edit spillover as a natural probe for world knowledge in image editing models. We introduce a spillover taxonomy (spatial, semantic, mixed, random), an automated detection-and-classification pipeline, and a benchmark dataset constructed from real-world Chinese text editing tasks, EditSpilloverBench. Systematic evaluation of 5 representative editing models reveals three core findings: (1) spillover rates vary dramatically across architectures, from 3.49% to 11.46%, with a 3.3x ratio; (2) absolute semantic spillover quantity reveals models' world understanding capability -- nano_banana produces the most semantic spillover (27.8 per image), while qwen_2511 has the most precise editing control but lower semantic spillover (16.3 per image), revealing a trade-off between editing control and world understanding; (3) spatial decay analysis shows spillover area density decays exponentially with distance, but the proportion of semantically relevant spillover remains constant (40%-58%), providing direct evidence that semantic spillover reflects genuine world understanding rather than spatial diffusion.
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
