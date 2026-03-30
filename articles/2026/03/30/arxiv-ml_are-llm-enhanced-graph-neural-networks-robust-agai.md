---
title: "Are LLM-Enhanced Graph Neural Networks Robust against Poisoning Attacks?"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26105"
published: "2026-03-30"
fetched: "2026-03-31T07:21:38.725623"
---

Computer Science > Machine Learning
[Submitted on 27 Mar 2026]
Title:Are LLM-Enhanced Graph Neural Networks Robust against Poisoning Attacks?
View PDF HTML (experimental)Abstract:Large Language Models (LLMs) have advanced Graph Neural Networks (GNNs) by enriching node representations with semantic features, giving rise to LLM-enhanced GNNs that achieve notable performance gains. However, the robustness of these models against poisoning attacks, which manipulate both graph structures and textual attributes during training, remains unexplored. To bridge this gap, we propose a robustness assessment framework that systematically evaluates LLM-enhanced GNNs under poisoning attacks. Our framework enables comprehensive evaluation across multiple dimensions. Specifically, we assess 24 victim models by combining eight LLM- or Language Model (LM)-based feature enhancers with three representative GNN backbones. To ensure diversity in attack coverage, we incorporate six structural poisoning attacks (both targeted and non-targeted) and three textual poisoning attacks operating at the character, word, and sentence levels. Furthermore, we employ four real-world datasets, including one released after the emergence of LLMs, to avoid potential ground truth leakage during LLM pretraining, thereby ensuring fair evaluation. Extensive experiments show that LLM-enhanced GNNs exhibit significantly higher accuracy and lower Relative Drop in Accuracy (RDA) than a shallow embedding-based baseline across various attack settings. Our in-depth analysis identifies key factors that contribute to this robustness, such as the effective encoding of structural and label information in node representations. Based on these insights, we outline future research directions from both offensive and defensive perspectives, and propose a new combined attack along with a graph purification defense. To support future research, we release the source code of our framework at~\url{this https URL}.
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
