---
title: "An Interpretable Machine Learning Framework for Non-Small Cell Lung Cancer Drug Response Analysis"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16330"
published: "2026-03-18"
fetched: "2026-03-18T16:12:00.879973"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:An Interpretable Machine Learning Framework for Non-Small Cell Lung Cancer Drug Response Analysis
View PDF HTML (experimental)Abstract:Lung cancer is a condition where there is abnormal growth of malignant cells that spread in an uncontrollable fashion in the lungs. Some common treatment strategies are surgery, chemotherapy, and radiation which aren't the best options due to the heterogeneous nature of cancer. In personalized medicine, treatments are tailored according to the individual's genetic information along with lifestyle aspects. In addition, AI-based deep learning methods can analyze large sets of data to find early signs of cancer, types of tumor, and prospects of treatment. The paper focuses on the development of personalized treatment plans using specific patient data focusing primarily on the genetic profile. Multi-Omics data from Genomics of Drug Sensitivity in Cancer have been used to build a predictive model along with machine learning techniques. The value of the target variable, LN-IC50, determines how sensitive or resistive a drug is. An XGBoost regressor is utilized to predict the drug response focusing on molecular and cellular features extracted from cancer datasets. Cross-validation and Randomized Search are performed for hyperparameter tuning to further optimize the model's predictive performance. For explanation purposes, SHAP (SHapley Additive exPlanations) was used. SHAP values measure each feature's impact on an individual prediction. Furthermore, interpreting feature relationships was performed using DeepSeek, a large language model trained to verify the biological validity of the features. Contextual explanations regarding the most important genes or pathways were provided by DeepSeek alongside the top SHAP value constituents, supporting the predictability of the model.
Current browse context:
cs.CV
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
