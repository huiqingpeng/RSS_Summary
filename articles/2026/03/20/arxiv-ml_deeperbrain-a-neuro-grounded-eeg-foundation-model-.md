---
title: "DeeperBrain: A Neuro-Grounded EEG Foundation Model Towards Universal BCI"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2601.06134"
published: "2026-03-20"
fetched: "2026-03-20T14:09:30.990615"
---

Computer Science > Machine Learning
[Submitted on 5 Jan 2026 (v1), last revised 19 Mar 2026 (this version, v2)]
Title:DeeperBrain: A Neuro-Grounded EEG Foundation Model Towards Universal BCI
View PDF HTML (experimental)Abstract:Electroencephalography (EEG) foundation models hold significant promise for universal Brain-Computer Interfaces (BCIs). However, existing approaches often rely on end-to-end fine-tuning and exhibit limited efficacy under frozen-probing protocols, lacking the intrinsic universality required for broad generalization. This limitation stems from adapting general-purpose sequence architectures that overlook the biophysical and dynamical principles of neural activity. To bridge this gap, we propose DeeperBrain, a neuro-grounded foundation model integrating domain-specific inductive biases into its model design and learning objectives. Architecturally, DeeperBrain incorporates a volume conduction-aware channel encoding to model spatial mixing via 3D geometry, and a neurodynamics-aware temporal encoding capturing slow adaptations using oscillatory and exponential bases. For pretraining, we introduce a dual-objective strategy combining Masked EEG Reconstruction (MER) for local fidelity and Neurodynamics Statistics Prediction (NSP). NSP enforces alignment with macroscopic brain states by predicting interpretable order parameters, including spectral power, functional connectivity, cross-frequency coupling, and dynamic complexity. Extensive experiments demonstrate that DeeperBrain achieves state-of-the-art or highly competitive performance under end-to-end fine-tuning. Crucially, it maintains superior efficacy under a rigorous frozen-probing protocol, verifying that embedding neuroscientific first principles endows learned representations with the intrinsic universality essential for universal BCI. The code will be publicly available.
Submission history
From: Jiquan Wang [view email][v1] Mon, 5 Jan 2026 05:31:45 UTC (14,383 KB)
[v2] Thu, 19 Mar 2026 06:41:01 UTC (14,383 KB)
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
