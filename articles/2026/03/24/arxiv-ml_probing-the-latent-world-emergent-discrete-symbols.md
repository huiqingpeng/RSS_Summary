---
title: "Probing the Latent World: Emergent Discrete Symbols and Physical Structure in Latent Representations"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20327"
published: "2026-03-24"
fetched: "2026-03-25T07:07:33.973758"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:Probing the Latent World: Emergent Discrete Symbols and Physical Structure in Latent Representations
View PDF HTML (experimental)Abstract:Video world models trained with Joint Embedding Predictive Architectures (JEPA) acquire rich spatiotemporal representations by predicting masked regions in latent space rather than reconstructing pixels. This removes the visual verification pathway of generative models, creating a structural interpretability gap: the encoder has learned physical structure inaccessible in any inspectable form. Existing probing methods either operate in continuous space without a structured intermediate layer, or attach generative components whose parameters confound attribution of behavior to the encoder.
We propose the AI Mother Tongue (AIM) framework as a passive quantization probe: a lightweight, vocabulary-free probe that converts V-JEPA 2 continuous latent vectors into discrete symbol sequences without task-specific supervision or modifying the encoder. Because the encoder is kept completely frozen, any symbolic structure in the AIM codebook is attributable entirely to V-JEPA 2 pre-trained representations -- not to the probe.
We evaluate through category-contrast experiments on Kinetics-mini along three physical dimensions: grasp angle, object geometry, and motion temporal structure. AIM symbol distributions differ significantly across all three experiments (chi^2 p < 10^{-4}; MI 0.036--0.117 bits, NMI 1.2--3.9% of the 3-bit maximum; JSD up to 0.342; codebook active ratio 62.5%). The experiments reveal that V-JEPA 2 latent space is markedly compact: diverse action categories share a common representational core, with semantic differences encoded as graded distributional variations rather than categorical boundaries. These results establish Stage 1 of a four-stage roadmap toward an action-conditioned symbolic world model, demonstrating that structured symbolic manifolds are discoverable properties of frozen JEPA latent spaces.
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
