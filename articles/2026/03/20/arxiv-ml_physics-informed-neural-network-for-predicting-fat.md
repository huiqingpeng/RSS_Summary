---
title: "Physics-informed neural network for predicting fatigue life of unirradiated and irradiated austenitic and ferritic/martensitic steels under reactor-relevant conditions"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2508.17303"
published: "2026-03-20"
fetched: "2026-03-20T14:06:59.972081"
---

Computer Science > Machine Learning
[Submitted on 24 Aug 2025 (v1), last revised 19 Mar 2026 (this version, v3)]
Title:Physics-informed neural network for predicting fatigue life of unirradiated and irradiated austenitic and ferritic/martensitic steels under reactor-relevant conditions
View PDFAbstract:This study proposes a Physics-Informed Neural Network (PINN) framework to predict the low-cycle fatigue (LCF) life of irradiated austenitic and ferritic/martensitic (F/M) steels used in nuclear reactors. These materials undergo cyclic loading, neutron irradiation, and elevated temperatures, leading to complex degradation mechanisms that are difficult to capture with conventional empirical or purely data-driven models. The proposed PINN embeds fatigue-life governing physical constraints into the loss function, enabling physically consistent learning while improving predictive accuracy, reliability, and generalizability. The model was trained on 495 strain-controlled fatigue data points spanning irradiated and unirradiated conditions. Compared with traditional machine learning approaches, including Random Forest, Gradient Boosting, eXtreme Gradient Boosting, and conventional neural networks, the PINN demonstrated superior performance. SHapley Additive exPlanations (SHAP) analysis identified strain amplitude, irradiation dose, and test temperature as the dominant features, each exhibiting physically meaningful inverse correlations with fatigue life. Univariate and multivariate analyses revealed clear alloy-specific degradation characteristics. Austenitic steels exhibited strong nonlinear coupling among strain amplitude, irradiation dose, and temperature, resulting in pronounced fatigue degradation under combined loading. In contrast, F/M steels demonstrated comparatively stable irradiation responses, including dose-saturation behavior, but showed sensitivity to elevated temperatures beyond tempering thresholds. Overall, the proposed PINN framework serves as a reliable and interpretable tool for reactor-relevant fatigue assessment, enabling performance evaluation for advanced nuclear applications.
Submission history
From: Ankur Chauhan [view email][v1] Sun, 24 Aug 2025 11:09:54 UTC (4,655 KB)
[v2] Sun, 14 Dec 2025 07:31:30 UTC (5,421 KB)
[v3] Thu, 19 Mar 2026 12:29:13 UTC (5,884 KB)
Current browse context:
cs.LG
Change to browse by:
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
