---
title: "Engineering Verifiable Modularity in Transformers via Per-Layer Supervision"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18029"
published: "2026-03-20"
fetched: "2026-03-20T12:05:03.515717"
---

Computer Science > Machine Learning
[Submitted on 8 Mar 2026]
Title:Engineering Verifiable Modularity in Transformers via Per-Layer Supervision
View PDF HTML (experimental)Abstract:Transformers resist surgical control. Ablating an attention head identified as critical for capitalization produces minimal behavioral change because distributed redundancy compensates for damage. This Hydra effect renders interpretability illusory: we may identify components through correlation, but cannot predict or control their causal role. We demonstrate that architectural interventions can expose hidden modularity. Our approach combines dual-stream processing separating token and contextual representations, per-layer supervision providing independent gradient signal at each depth, and gated attention regularizing toward discrete activation patterns. When trained with per-layer supervision, models produce ablation effects 5 to 23 times larger than architecturally identical controls trained with standard objectives. This enables 4 times greater control leverage on targeted behaviors: scaling identified attention heads produces smooth, predictable changes in model output. The key finding is architectural. Without per-layer supervision, ablation damage concentrates near zero with low variance (Winograd standard deviation 0.63%). With per-layer supervision, effects spread widely (standard deviation 6.32%), revealing which predictions depend on which circuits. The larger variance is not measurement noise but the signature of unmasked modularity. We validate our approach through three components: engineered features that capture computational dynamics rather than vocabulary structure (validated by near-zero correlation with raw activation clustering), an architecture providing positive control for modularity, and causal experiments demonstrating functional reorganization where different tasks route through different attention heads. This es tablishes a methodology for transforming interpretability from passive observation to active control.
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
