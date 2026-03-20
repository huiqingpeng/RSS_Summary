---
title: "Few-shot Acoustic Synthesis with Multimodal Flow Matching"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.19176"
published: "2026-03-20"
fetched: "2026-03-20T16:09:23.832076"
---

Computer Science > Sound
[Submitted on 19 Mar 2026]
Title:Few-shot Acoustic Synthesis with Multimodal Flow Matching
View PDF HTML (experimental)Abstract:Generating audio that is acoustically consistent with a scene is essential for immersive virtual environments. Recent neural acoustic field methods enable spatially continuous sound rendering but remain scene-specific, requiring dense audio measurements and costly training for each environment. Few-shot approaches improve scalability across rooms but still rely on multiple recordings and, being deterministic, fail to capture the inherent uncertainty of scene acoustics under sparse context. We introduce flow-matching acoustic generation (FLAC), a probabilistic method for few-shot acoustic synthesis that models the distribution of plausible room impulse responses (RIRs) given minimal scene context. FLAC leverages a diffusion transformer trained with a flow-matching objective to generate RIRs at arbitrary positions in novel scenes, conditioned on spatial, geometric, and acoustic cues. FLAC outperforms state-of-the-art eight-shot baselines with one-shot on both the AcousticRooms and Hearing Anything Anywhere datasets. To complement standard perceptual metrics, we further introduce AGREE, a joint acoustic-geometry embedding, enabling geometry-consistent evaluation of generated RIRs through retrieval and distributional metrics. This work is the first to apply generative flow matching to explicit RIR synthesis, establishing a new direction for robust and data-efficient acoustic synthesis.
Submission history
From: Amandine Brunetto [view email][v1] Thu, 19 Mar 2026 17:32:06 UTC (9,820 KB)
Current browse context:
cs.SD
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
