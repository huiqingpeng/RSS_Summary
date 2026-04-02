---
title: "WARP: Guaranteed Inner-Layer Repair of NLP Transformers"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00938"
published: "2026-04-02"
fetched: "2026-04-03T07:26:14.647450"
---

Computer Science > Machine Learning
[Submitted on 1 Apr 2026]
Title:WARP: Guaranteed Inner-Layer Repair of NLP Transformers
View PDF HTML (experimental)Abstract:Transformer-based NLP models remain vulnerable to adversarial perturbations, yet existing repair methods face a fundamental trade-off: gradient-based approaches offer flexibility but lack verifiability and often overfit; methods that do provide repair guarantees are restricted to the final layer or small networks, significantly limiting the parameter search space available for repair. We present WARP (Weight-Adjusted Repair with Provability), a constraint-based repair framework that extends repair beyond the last layer of Transformer models. WARP formulates repair as a convex quadratic program derived from a first-order linearization of the logit gap, enabling tractable optimization over a high-dimensional parameter space. Under the condition that the first-order approximation holds, this formulation induces three per-sample guarantees: (i) a positive margin constraint ensuring correct classification on repaired inputs, (ii) preservation constraints over a designated remain set, and (iii) a certified robustness radius derived from Lipschitz continuity. To ensure feasibility across varying model architectures, we introduce a sensitivity-based preprocessing step that conditions the optimization landscape accordingly. We further show that the iterative optimization procedure converges to solutions satisfying all repair constraints under mild assumptions. Empirical evaluation on encoder-only Transformers with varying layer architectures validates that these guarantees hold in practice while improving robustness to adversarial inputs. Our results demonstrate that guaranteed, generalizable Transformer repair is achievable through principled constraint-based optimization.
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
