---
title: "Likelihood hacking in probabilistic program synthesis"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24126"
published: "2026-03-26"
fetched: "2026-03-27T07:20:53.127591"
---

Computer Science > Machine Learning
[Submitted on 25 Mar 2026]
Title:Likelihood hacking in probabilistic program synthesis
View PDFAbstract:When language models are trained by reinforcement learning (RL) to write probabilistic programs, they can artificially inflate their marginal-likelihood reward by producing programs whose data distribution fails to normalise instead of fitting the data better. We call this failure likelihood hacking (LH). We formalise LH in a core probabilistic programming language (PPL) and give sufficient syntactic conditions for its prevention, proving that a safe language fragment $\mathcal{L}_{\text{safe}}$ satisfying these conditions cannot produce likelihood-hacking programs. Empirically, we show that GRPO-trained models generating PyMC code discover LH exploits within the first few training steps, driving violation rates well above the untrained-model baseline. We implement $\mathcal{L}_{\text{safe}}$'s conditions as $\texttt{SafeStan}$, a LH-resistant modification of Stan, and show empirically that it prevents LH under optimisation pressure. These results show that language-level safety constraints are both theoretically grounded and effective in practice for automated Bayesian model discovery.
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
