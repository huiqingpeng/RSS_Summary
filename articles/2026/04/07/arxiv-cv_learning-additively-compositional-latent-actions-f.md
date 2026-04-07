---
title: "Learning Additively Compositional Latent Actions for Embodied AI"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2604.03340"
published: "2026-04-07"
fetched: "2026-04-08T07:02:52.823062"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 3 Apr 2026]
Title:Learning Additively Compositional Latent Actions for Embodied AI
View PDF HTML (experimental)Abstract:Latent action learning infers pseudo-action labels from visual transitions, providing an approach to leverage internet-scale video for embodied AI. However, most methods learn latent actions without structural priors that encode the additive, compositional structure of physical motion. As a result, latents often entangle irrelevant scene details or information about future observations with true state changes and miscalibrate motion magnitude. We introduce Additively Compositional Latent Action Model (AC-LAM), which enforces scene-wise additive composition structure over short horizons on the latent action space. These AC constraints encourage simple algebraic structure in the latent action space~(identity, inverse, cycle consistency) and suppress information that does not compose additively. Empirically, AC-LAM learns more structured, motion-specific, and displacement-calibrated latent actions and provides stronger supervision for downstream policy learning, outperforming state-of-the-art LAMs across simulated and real-world tabletop tasks.
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
ScienceCast (What is ScienceCast?)
Demos
Recommenders and Search Tools
Influence Flower (What are Influence Flowers?)
CORE Recommender (What is CORE?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
