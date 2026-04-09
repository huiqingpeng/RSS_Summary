---
title: "When Does Context Help? A Systematic Study of Target-Conditional Molecular Property Prediction"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.06558"
published: "2026-04-09"
fetched: "2026-04-10T07:05:03.461596"
---

Computer Science > Machine Learning
[Submitted on 8 Apr 2026]
Title:When Does Context Help? A Systematic Study of Target-Conditional Molecular Property Prediction
View PDF HTML (experimental)Abstract:We present the first systematic study of when target context helps molecular property prediction, evaluating context conditioning across 10 diverse protein families, 4 fusion architectures, data regimes spanning 67-9,409 training compounds, and both temporal and random evaluation splits. Using NestDrug, a FiLM-based architecture that conditions molecular representations on target identity, we characterize both success and failure modes with three principal findings. First, fusion architecture dominates: FiLM outperforms concatenation by 24.2 percentage points and additive conditioning by 8.6 pp; how you incorporate context matters more than whether you include it. Second, context enables otherwise impossible predictions: on data-scarce CYP3A4 (67 training compounds), multi-task transfer achieves 0.686 AUC where per-target Random Forest collapses to 0.238. Third, context can systematically hurt: distribution mismatch causes 10.2 pp degradation on BACE1; few-shot adaptation consistently underperforms zero-shot. Beyond methodology, we expose fundamental flaws in standard benchmarking: 1-nearest-neighbor Tanimoto achieves 0.991 AUC on DUD-E without any learning, and 50% of actives leak from training data, rendering absolute performance metrics meaningless. Our temporal split evaluation (train up to 2020, test 2021-2024) achieves stable 0.843 AUC with no degradation, providing the first rigorous evidence that context-conditional molecular representations generalize to future chemical space.
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
