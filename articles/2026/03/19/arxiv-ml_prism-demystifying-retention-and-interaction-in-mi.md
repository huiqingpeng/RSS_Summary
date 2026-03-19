---
title: "PRISM: Demystifying Retention and Interaction in Mid-Training"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17074"
published: "2026-03-19"
fetched: "2026-03-19T12:07:04.847677"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:PRISM: Demystifying Retention and Interaction in Mid-Training
View PDFAbstract:We present PRISM, a comprehensive empirical study of mid-training design choices for large language models. Through controlled experiments across seven base models spanning four families (Granite, LLaMA, Mistral, Nemotron-H), two architecture types (dense Transformer and attention-Mamba hybrid), and scales from 3B to 24B parameters, we show that mid-training on approximately 27B high-quality tokens yields consistent gains of +15 to +40 points on math, +5 to +12 points on code, and +6 to +13 points on science benchmarks while preserving general performance. The full PRISM to RL pipeline improves macro-average across six reasoning benchmarks from under 12 to 29-42 (a 3-4x improvement), whereas RL applied directly to most of the base models remains substantially less effective, with AIME scores near zero. Data composition matters most at mid-training, not RL: including science data during mid-training unlocks +17 to +28 point GPQA-Diamond gains during RL, while changing the RL mix produces less than 2 point differences. Mechanistically, mid-training densely restructures over 90% of model weights, while RL makes sparse, front-loaded refinements to approximately 5% of parameters. Representation analysis (CKA) confirms that RL consistently preserves mid-training's representational geometry (over 0.998 CKA) across architectures. Crucially, RL applies identical weight changes regardless of starting point, yet only succeeds on mid-trained models, consistent with mid-training placing the model in a configuration from which RL can effectively improve performance. Our results demonstrate that retention-aware mid-training is highly effective for reliable reasoning enhancement and provide practical guidance for designing robust mid-training pipelines.
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
