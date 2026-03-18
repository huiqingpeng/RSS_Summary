---
title: "World Models for Learning Dexterous Hand-Object Interactions from Human Videos"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2512.13644"
published: "2026-03-18"
fetched: "2026-03-18T19:06:22.871644"
---

Computer Science > Robotics
[Submitted on 15 Dec 2025 (v1), last revised 16 Mar 2026 (this version, v2)]
Title:World Models for Learning Dexterous Hand-Object Interactions from Human Videos
View PDF HTML (experimental)Abstract:Modeling dexterous hand-object interactions is challenging as it requires understanding how subtle finger motions influence the environment through contact with objects. While recent world models address interaction modeling, they typically rely on coarse action spaces that fail to capture fine-grained dexterity. We, therefore, introduce DexWM, a Dexterous Interaction World Model that predicts future latent states of the environment conditioned on past states and dexterous actions. To overcome the scarcity of finely annotated dexterous datasets, DexWM represents actions using finger keypoints extracted from egocentric videos, enabling training on over 900 hours of human and non-dexterous robot data. Further, to accurately model dexterity, we find that predicting visual features alone is insufficient; therefore, we incorporate an auxiliary hand consistency loss that enforces accurate hand configurations. DexWM outperforms prior world models conditioned on text, navigation, or full-body actions in future-state prediction and demonstrates strong zero-shot transfer to unseen skills on a Franka Panda arm with an Allegro gripper, surpassing Diffusion Policy by over 50% on average across grasping, placing, and reaching tasks.
Submission history
From: Raktim Gautam Goswami [view email][v1] Mon, 15 Dec 2025 18:37:12 UTC (38,467 KB)
[v2] Mon, 16 Mar 2026 21:03:20 UTC (39,066 KB)
Current browse context:
cs.RO
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
