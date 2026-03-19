---
title: "End-to-end data-driven prediction of urban airflow and pollutant dispersion"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17606"
published: "2026-03-19"
fetched: "2026-03-19T12:14:18.799344"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:End-to-end data-driven prediction of urban airflow and pollutant dispersion
View PDF HTML (experimental)Abstract:Climate change and the rapid growth of urban populations are intensifying environmental stresses within cities, making the behavior of urban atmospheric flows a critical factor in public health, energy use, and overall livability. This study targets to develop fast and accurate models of urban pollutant dispersion to support decision-makers, enabling them to implement mitigation measures in a timely and cost-effective manner. To reach this goal, an end-to-end data-driven approach is proposed to model and predict the airflow and pollutant dispersion in a street canyon in skimming flow regime. A series of time-resolved snapshots obtained from large eddy simulation (LES) serves as the database. The proposed framework is based on four fundamental steps. Firstly, a reduced basis is obtained by spectral proper orthogonal decomposition (SPOD) of the database. The projection of the time series snapshot data onto the SPOD modes (time-domain approach) provides the temporal coefficients of the dynamics. Secondly, a nonlinear compression of the temporal coefficients is performed by autoencoder to reduce further the dimensionality of the problem. Thirdly, a reduced-order model (ROM) is learned in the latent space using Long Short-Term Memory (LSTM) netowrks. Finally, the pollutant dispersion is estimated from the predicted velocity field through convolutional neural network that maps both fields. The results demonstrate the efficacy of the model in predicting the instantaneous as well as statistically stationary fields over long time horizon.
Submission history
From: Laurent Cordier Dr [view email][v1] Wed, 18 Mar 2026 11:19:13 UTC (6,044 KB)
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
