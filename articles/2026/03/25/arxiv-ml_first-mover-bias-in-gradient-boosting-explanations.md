---
title: "First-Mover Bias in Gradient Boosting Explanations: Mechanism, Detection, and Resolution"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22346"
published: "2026-03-25"
fetched: "2026-03-26T07:12:56.561361"
---

Computer Science > Machine Learning
[Submitted on 22 Mar 2026]
Title:First-Mover Bias in Gradient Boosting Explanations: Mechanism, Detection, and Resolution
View PDF HTML (experimental)Abstract:We isolate and empirically characterize first-mover bias -- a path-dependent concentration of feature importance caused by sequential residual fitting in gradient boosting -- as a specific mechanistic cause of the well-known instability of SHAP-based feature rankings under multicollinearity. When correlated features compete for early splits, gradient boosting creates a self-reinforcing advantage for whichever feature is selected first: subsequent trees inherit modified residuals that favor the incumbent, concentrating SHAP importance on an arbitrary feature rather than distributing it across the correlated group. Scaling up a single model amplifies this effect -- a Large Single Model with the same total tree count as our method produces the worst explanations of any approach tested. We demonstrate that model independence is sufficient to resolve first-mover bias in the linear regime, and remains the most effective mitigation under nonlinear data-generating processes. Both our proposed method, DASH (Diversified Aggregation of SHAP), and simple seed-averaging (Stochastic Retrain) restore stability by breaking the sequential dependency chain, confirming that the operative mechanism is independence between explained models. At rho=0.9, both achieve stability=0.977, while the single-best workflow degrades to 0.958 and the Large Single Model to 0.938. On the Breast Cancer dataset, DASH improves stability from 0.32 to 0.93 (+0.61) against a tree-count-matched baseline. DASH additionally provides two diagnostic tools -- the Feature Stability Index (FSI) and Importance-Stability (IS) Plot -- that detect first-mover bias without ground truth, enabling practitioners to audit explanation reliability before acting on feature rankings. Software and reproducible benchmarks are available at this https URL.
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
