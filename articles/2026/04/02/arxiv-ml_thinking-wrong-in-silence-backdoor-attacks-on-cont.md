---
title: "Thinking Wrong in Silence: Backdoor Attacks on Continuous Latent Reasoning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00770"
published: "2026-04-02"
fetched: "2026-04-03T07:24:29.709827"
---

Computer Science > Machine Learning
[Submitted on 1 Apr 2026]
Title:Thinking Wrong in Silence: Backdoor Attacks on Continuous Latent Reasoning
View PDF HTML (experimental)Abstract:A new generation of language models reasons entirely in continuous hidden states, producing no tokens and leaving
no audit trail. We show that this silence creates a fundamentally new attack surface. ThoughtSteer perturbs a
single embedding vector at the input layer; the model's own multi-pass reasoning amplifies this perturbation into a
hijacked latent trajectory that reliably produces the attacker's chosen answer, while remaining structurally
invisible to every token-level defense. Across two architectures (Coconut and SimCoT), three reasoning benchmarks,
and model scales from 124M to 3B parameters, ThoughtSteer achieves >=99% attack success rate with near-baseline
clean accuracy, transfers to held-out benchmarks without retraining (94-100%), evades all five evaluated active
defenses, and survives 25 epochs of clean fine-tuning. We trace these results to a unifying mechanism: Neural
Collapse in the latent space pulls triggered representations onto a tight geometric attractor, explaining both why
defenses fail and why any effective backdoor must leave a linearly separable signature (probe AUC>=0.999). Yet a
striking paradox emerges: individual latent vectors still encode the correct answer even as the model outputs the
wrong one. The adversarial information is not in any single vector but in the collective trajectory, establishing
backdoor perturbations as a new lens for mechanistic interpretability of continuous reasoning. Code and checkpoints
are available.
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
