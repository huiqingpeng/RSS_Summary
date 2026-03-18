---
title: "Behavioral Steering in a 35B MoE Language Model via SAE-Decoded Probe Vectors: One Agency Axis, Not Five Traits"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16335"
published: "2026-03-18"
fetched: "2026-03-18T15:42:45.805264"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:Behavioral Steering in a 35B MoE Language Model via SAE-Decoded Probe Vectors: One Agency Axis, Not Five Traits
View PDF HTML (experimental)Abstract:We train nine sparse autoencoders (SAEs) on the residual stream of Qwen 3.5-35B-A3B, a 35-billion-parameter Mixture-of-Experts model with a hybrid GatedDeltaNet/attention architecture, and use them to identify and steer five agentic behavioral traits. Our method trains linear probes on SAE latent activations, then projects the probe weights back through the SAE decoder to obtain continuous steering vectors in the model's native activation space. This bypasses the SAE's top-k discretization, enabling fine-grained behavioral intervention at inference time with no retraining. Across 1,800 agent rollouts (50 scenarios times 36 conditions), we find that autonomy steering at multiplier 2 achieves Cohen's d = 1.01 (p < 0.0001), shifting the model from asking the user for help 78% of the time to proactively executing code and searching the web. Cross-trait analysis, however, reveals that all five steering vectors primarily modulate a single dominant agency axis (the disposition to act independently versus defer to the user), with trait specific effects appearing only as secondary modulations in tool-type composition and dose-response shape. The tool-use vector steers behavior (d = 0.39); the risk-calibration vector produces only suppression. We additionally show that steering only during autoregressive decoding has zero effect (p > 0.35), providing causal evidence that behavioral commitments are computed during prefill in GatedDeltaNet architectures.
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
