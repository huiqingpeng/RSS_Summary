---
title: "An Optimised Greedy-Weighted Ensemble Framework for Financial Loan Default Prediction"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18927"
published: "2026-03-20"
fetched: "2026-03-20T12:16:51.457805"
---

Computer Science > Machine Learning
[Submitted on 19 Mar 2026]
Title:An Optimised Greedy-Weighted Ensemble Framework for Financial Loan Default Prediction
View PDF HTML (experimental)Abstract:Accurate prediction of loan defaults is a central challenge in credit risk management, particularly in modern financial datasets characterised by nonlinear relationships, class imbalance, and evolving borrower behaviour. Traditional statistical models and static ensemble methods often struggle to maintain reliable performance under such conditions. This study proposes an Optimised Greedy-Weighted Ensemble framework for loan default prediction that dynamically allocates model weights based on empirical predictive performance. The framework integrates multiple machine learning classifiers, with their hyperparameters first optimised using Particle Swarm Optimisation. Model predictions are then combined via a regularised greedy weighting mechanism. At the same time, a neural-network-based meta-learner is employed within stacked-ensemble to capture higher-order relationships among model outputs. Experiments conducted on the Lending Club dataset demonstrate that the proposed framework improves predictive performance compared with individual classifiers. The BlendNet ensemble achieved the strongest results with an AUC of 0.80, a macro-average F1-score of 0.73, and a default recall of 0.81. Calibration analysis further shows that tree-based ensembles such as Extra Trees and Gradient Boosting provide the most reliable probability estimates, while the stacked ensemble offers superior ranking capability. Feature analysis using Recursive Feature Elimination identifies revolving utilisation, annual income, and debt-to-income ratio as the most influential predictors of loan default. These findings demonstrate that performance-driven ensemble weighting can improve both predictive accuracy and interpretability in credit risk modelling. The proposed framework provides a scalable data-driven approach to support institutional credit assessment, risk monitoring, and financial decision-making.
Submission history
From: Marcellin Atemkeng [view email][v1] Thu, 19 Mar 2026 14:04:37 UTC (1,130 KB)
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
