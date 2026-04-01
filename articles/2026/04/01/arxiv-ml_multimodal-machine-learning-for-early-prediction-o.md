---
title: "Multimodal Machine Learning for Early Prediction of Metastasis in a Swedish Multi-Cancer Cohort"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.29793"
published: "2026-04-01"
fetched: "2026-04-02T07:20:17.838907"
---

Computer Science > Machine Learning
[Submitted on 31 Mar 2026]
Title:Multimodal Machine Learning for Early Prediction of Metastasis in a Swedish Multi-Cancer Cohort
View PDFAbstract:Multimodal Machine Learning offers a holistic view of a patient's status, integrating structured and unstructured data from electronic health records (EHR). We propose a framework to predict metastasis risk one month prior to diagnosis, using six months of clinical history from EHR data. Data from four cancer cohorts collected at Karolinska University Hospital (Stockholm, Sweden) were analyzed: breast (n = 743), colon (n = 387), lung (n = 870), and prostate (n = 1890). The dataset included demographics, comorbidities, laboratory results, medications, and clinical text. We compared traditional and deep learning classifiers across single modalities and multimodal combinations, using various fusion strategies and a Transparent Reporting of a multivariable prediction model for Individual Prognosis Or Diagnosis (TRIPOD) 2a design, with an 80-20 development-validation split to ensure a rigorous, repeatable evaluation. Performance was evaluated using AUROC, AUPRC, F1 score, sensitivity, and specificity. We then employed a multimodal adaptation of SHAP to analyze the classifiers' reasoning. Intermediate fusion achieved the highest F1 scores on breast (0.845), colon (0.786), and prostate cancer (0.845), demonstrating strong predictive performance. For lung cancer, the intermediate fusion achieved an F1 score of 0.819, while the text-only model achieved the highest, with an F1 score of 0.829. Deep learning classifiers consistently outperformed traditional models. Colon cancer, the smallest cohort, had the lowest performance, highlighting the importance of sufficient training data. SHAP analysis showed that the relative importance of modalities varied across cancer types. Fusion strategies offer distinct strengths and weaknesses. Intermediate fusion consistently delivered the best results, but strategy choices should align with data characteristics and organizational needs.
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
