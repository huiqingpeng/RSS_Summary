---
title: "Flood Risk Follows Valleys, Not Grids: Graph Neural Networks for Flash Flood Susceptibility Mapping in Himachal Pradesh with Conformal Uncertainty Quantification"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15681"
published: "2026-03-18"
fetched: "2026-03-18T15:33:47.906453"
---

Computer Science > Machine Learning
[Submitted on 15 Mar 2026]
Title:Flood Risk Follows Valleys, Not Grids: Graph Neural Networks for Flash Flood Susceptibility Mapping in Himachal Pradesh with Conformal Uncertainty Quantification
View PDF HTML (experimental)Abstract:Flash floods are the most destructive natural hazard in Himachal Pradesh (HP), India, causing over 400 fatalities and $1.2 billion in losses in the 2023 monsoon season alone. Existing risk maps treat every pixel independently, ignoring the basic fact that flooding upstream raises risk downstream. We address this with a Graph Neural Network (GraphSAGE) trained on a watershed connectivity graph (460 sub-watersheds, 1,700 directed edges), built from a six-year Sentinel-1 SAR flood inventory (2018-2023, 3,000 events) and 12 environmental variables at 30 m resolution. Four pixel-based ML models (RF, XGBoost, LightGBM, stacking ensemble) serve as baselines. All models are evaluated with leave-one-basin-out spatial cross-validation to avoid the 5-15% AUC inflation of random splits. Conformal prediction produces the first HP susceptibility maps with statistically guaranteed 90% coverage intervals.
The GNN achieved AUC = 0.978 +/- 0.017, outperforming the best baseline (AUC = 0.881) and the published HP benchmark (AUC = 0.88). The +0.097 gain confirms that river connectivity carries predictive signal that pixel-based models miss. High-susceptibility zones overlap 1,457 km of highways (including 217 km of the Manali-Leh corridor), 2,759 bridges, and 4 major hydroelectric installations. Conformal intervals achieved 82.9% empirical coverage on the held-out 2023 test set; lower coverage in high-risk zones (45-59%) points to SAR label noise as a target for future work.
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
