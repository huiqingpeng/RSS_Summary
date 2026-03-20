---
title: "When Names Change Verdicts: Intervention Consistency Reveals Systematic Bias in LLM Decision-Making"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18530"
published: "2026-03-20"
fetched: "2026-03-20T13:13:57.111542"
---

Computer Science > Computation and Language
[Submitted on 19 Mar 2026]
Title:When Names Change Verdicts: Intervention Consistency Reveals Systematic Bias in LLM Decision-Making
View PDF HTML (experimental)Abstract:Large language models (LLMs) are increasingly used for high-stakes decisions, yet their susceptibility to spurious features remains poorly characterized. We introduce ICE-Guard, a framework applying intervention consistency testing to detect three types of spurious feature reliance: demographic (name/race swaps), authority (credential/prestige swaps), and framing (positive/negative restatements). Across 3,000 vignettes spanning 10 high-stakes domains, we evaluate 11 LLMs from 8 families and find that (1) authority bias (mean 5.8%) and framing bias (5.0%) substantially exceed demographic bias (2.2%), challenging the field's narrow focus on demographics; (2) bias concentrates in specific domains -- finance shows 22.6% authority bias while criminal justice shows only 2.8%; (3) structured decomposition, where the LLM extracts features and a deterministic rubric decides, reduces flip rates by up to 100% (median 49% across 9 models). We demonstrate an ICE-guided detect-diagnose-mitigate-verify loop achieving cumulative 78% bias reduction via iterative prompt patching. Validation against real COMPAS recidivism data shows COMPAS-derived flip rates exceed pooled synthetic rates, suggesting our benchmark provides a conservative estimate of real-world bias. Code and data are publicly available.
Current browse context:
cs.CL
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
