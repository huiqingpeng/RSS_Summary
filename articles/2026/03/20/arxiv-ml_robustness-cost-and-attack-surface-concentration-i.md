---
title: "Robustness, Cost, and Attack-Surface Concentration in Phishing Detection"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19204"
published: "2026-03-20"
fetched: "2026-03-20T13:06:46.286363"
---

Computer Science > Machine Learning
[Submitted on 19 Mar 2026]
Title:Robustness, Cost, and Attack-Surface Concentration in Phishing Detection
View PDF HTML (experimental)Abstract:Phishing detectors built on engineered website features attain near-perfect accuracy under i.i.d.\ evaluation, yet deployment security depends on robustness to post-deployment feature manipulation. We study this gap through a cost-aware evasion framework that models discrete, monotone feature edits under explicit attacker budgets. Three diagnostics are introduced: minimal evasion cost (MEC), the evasion survival rate $S(B)$, and the robustness concentration index (RCI).
On the UCI Phishing Websites benchmark (11\,055 instances, 30 ternary features), Logistic Regression, Random Forests, Gradient Boosted Trees, and XGBoost all achieve $\mathrm{AUC}\ge 0.979$ under static evaluation. Under budgeted sanitization-style evasion, robustness converges across architectures: the median MEC equals 2 with full features, and over 80\% of successful minimal-cost evasions concentrate on three low-cost surface features. Feature restriction improves robustness only when it removes all dominant low-cost transitions. Under strict cost schedules, infrastructure-leaning feature sets exhibit 17-19\% infeasible mass for ensemble models, while the median MEC among evadable instances remains unchanged. We formalize this convergence: if a positive fraction of correctly detected phishing instances admit evasion through a single feature transition of minimal cost $c_{\min}$, no classifier can raise the corresponding MEC quantile above $c_{\min}$ without modifying the feature representation or cost model. Adversarial robustness in phishing detection is governed by feature economics rather than model complexity.
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
