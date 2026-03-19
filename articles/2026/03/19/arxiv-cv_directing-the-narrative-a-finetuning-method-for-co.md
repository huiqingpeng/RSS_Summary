---
title: "Directing the Narrative: A Finetuning Method for Controlling Coherence and Style in Story Generation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17295"
published: "2026-03-19"
fetched: "2026-03-19T15:07:27.250835"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:Directing the Narrative: A Finetuning Method for Controlling Coherence and Style in Story Generation
View PDF HTML (experimental)Abstract:Story visualization requires generating sequential imagery that aligns semantically with evolving narratives while maintaining rigorous consistency in character identity and visual style. However, existing methodologies often struggle with subject inconsistency and identity drift, particularly when depicting complex interactions or extended narrative arcs. To address these challenges, we propose a cohesive two-stage framework designed for robust and consistent story generation. First, we introduce Group-Shared Attention (GSA), a mechanism that fosters intrinsic consistency by enabling lossless cross-sample information flow within attention layers. This allows the model to structurally encode identity correspondence across frames without relying on external encoders. Second, we leverage Direct Preference Optimization (DPO) to align generated outputs with human aesthetic and narrative standards. Unlike conventional methods that rely on conflicting auxiliary losses, our approach simultaneously enhances visual fidelity and identity preservation by learning from holistic preference data. Extensive evaluations on the ViStoryBench benchmark demonstrate that our method establishes a new state-of-the-art, significantly outperforming strong baselines with gains of +10.0 in Character Identity (CIDS) and +18.7 in Style Consistency (CSD), all while preserving high-fidelity generation.
Submission history
From: Jianzhang Zhang [view email][v1] Wed, 18 Mar 2026 02:43:02 UTC (16,939 KB)
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
