---
title: "Laya: A LeJEPA Approach to EEG via Latent Prediction over Reconstruction"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16281"
published: "2026-03-18"
fetched: "2026-03-18T15:42:29.733030"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:Laya: A LeJEPA Approach to EEG via Latent Prediction over Reconstruction
View PDF HTML (experimental)Abstract:Electroencephalography (EEG) is a widely used tool for studying brain function, with applications in clinical neuroscience, diagnosis, and brain-computer interfaces (BCIs). Recent EEG foundation models trained on large unlabeled corpora aim to learn transferable representations, but their effectiveness remains unclear; reported improvements over smaller task-specific models are often modest, sensitive to downstream adaptation and fine-tuning strategies, and limited under linear probing. We hypothesize that one contributing factor is the reliance on signal reconstruction as the primary self-supervised learning (SSL) objective, which biases representations toward high-variance artifacts rather than task-relevant neural structure. To address this limitation, we explore an SSL paradigm based on Joint Embedding Predictive Architectures (JEPA), which learn by predicting latent representations instead of reconstructing raw signals. While earlier JEPA-style methods often rely on additional heuristics to ensure training stability, recent advances such as LeJEPA provide a more principled and stable formulation. We introduce Laya, the first EEG foundation model based on LeJEPA. Across a range of EEG benchmarks, Laya demonstrates improved performance under linear probing compared to reconstruction-based baselines, suggesting that latent predictive objectives offer a promising direction for learning transferable, high-level EEG representations.
Submission history
From: Saarang Panchavati [view email][v1] Tue, 17 Mar 2026 09:13:29 UTC (26,639 KB)
Current browse context:
cs.LG
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
IArxiv Recommender
(What is IArxiv?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
