---
title: "Balancing Performance and Fairness in Explainable AI for Anomaly Detection in Distributed Power Plants Monitoring"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18954"
published: "2026-03-20"
fetched: "2026-03-20T12:17:12.475372"
---

Computer Science > Machine Learning
[Submitted on 19 Mar 2026]
Title:Balancing Performance and Fairness in Explainable AI for Anomaly Detection in Distributed Power Plants Monitoring
View PDF HTML (experimental)Abstract:Reliable anomaly detection in distributed power plant monitoring systems is essential for ensuring operational continuity and reducing maintenance costs, particularly in regions where telecom operators heavily rely on diesel generators. However, this task is challenged by extreme class imbalance, lack of interpretability, and potential fairness issues across regional clusters. In this work, we propose a supervised ML framework that integrates ensemble methods (LightGBM, XGBoost, Random Forest, CatBoost, GBDT, AdaBoost) and baseline models (Support Vector Machine, K-Nearrest Neighbors, Multilayer Perceptrons, and Logistic Regression) with advanced resampling techniques (SMOTE with Tomek Links and ENN) to address imbalance in a dataset of diesel generator operations in Cameroon. Interpretability is achieved through SHAP (SHapley Additive exPlanations), while fairness is quantified using the Disparate Impact Ratio (DIR) across operational clusters. We further evaluate model generalization using Maximum Mean Discrepancy (MMD) to capture domain shifts between regions. Experimental results show that ensemble models consistently outperform baselines, with LightGBM achieving an F1-score of 0.99 and minimal bias across clusters (DIR $\approx 0.95$). SHAP analysis highlights fuel consumption rate and runtime per day as dominant predictors, providing actionable insights for operators. Our findings demonstrate that it is possible to balance performance, interpretability, and fairness in anomaly detection, paving the way for more equitable and explainable AI systems in industrial power management. {\color{black} Finally, beyond offline evaluation, we also discuss how the trained models can be deployed in practice for real-time monitoring. We show how containerized services can process in real-time, deliver low-latency predictions, and provide interpretable outputs for operators.
Submission history
From: Marcellin Atemkeng [view email][v1] Thu, 19 Mar 2026 14:24:05 UTC (7,636 KB)
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
