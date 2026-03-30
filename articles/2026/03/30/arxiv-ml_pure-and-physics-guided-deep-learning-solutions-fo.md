---
title: "Pure and Physics-Guided Deep Learning Solutions for Spatio-Temporal Groundwater Level Prediction at Arbitrary Locations"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.25779"
published: "2026-03-30"
fetched: "2026-03-31T07:17:43.642022"
---

Computer Science > Machine Learning
[Submitted on 26 Mar 2026]
Title:Pure and Physics-Guided Deep Learning Solutions for Spatio-Temporal Groundwater Level Prediction at Arbitrary Locations
View PDF HTML (experimental)Abstract:Groundwater represents a key element of the water cycle, yet it exhibits intricate and context-dependent relationships that make its modeling a challenging task. Theory-based models have been the cornerstone of scientific understanding. However, their computational demands, simplifying assumptions, and calibration requirements limit their use. In recent years, data-driven models have emerged as powerful alternatives. In particular, deep learning has proven to be a leading approach for its design flexibility and ability to learn complex relationships.
We proposed an attention-based pure deep learning model, named STAINet, to predict weekly groundwater levels at an arbitrary and variable number of locations, leveraging both spatially sparse groundwater measurements and spatially dense weather information. Then, to enhance the model's trustworthiness and generalization ability, we considered different physics-guided strategies to inject the groundwater flow equation into the model. Firstly, in the STAINet-IB, by introducing an inductive bias, we also estimated the governing equation components. Then, by adopting a learning bias strategy, we proposed the STAINet-ILB, trained with additional loss terms adding supervision on the estimated equation components. Lastly, we developed the STAINet-ILRB, leveraging the groundwater body recharge zone information estimated by domain experts.
The STAINet-ILB performed the best, achieving overwhelming test performances in a rollout setting (median MAPE 0.16%, KGE 0.58). Furthermore, it predicted sensible equation components, providing insights into the model's physical soundness. Physics-guided approaches represent a promising opportunity to enhance both the generalization ability and the trustworthiness, thereby paving the way to a new generation of disruptive hybrid deep learning Earth system models.
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
