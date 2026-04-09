---
title: "Toward a universal foundation model for graph-structured data"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.06391"
published: "2026-04-09"
fetched: "2026-04-10T07:04:57.975239"
---

Computer Science > Machine Learning
[Submitted on 7 Apr 2026]
Title:Toward a universal foundation model for graph-structured data
View PDF HTML (experimental)Abstract:Graphs are a central representation in biomedical research, capturing molecular interaction networks, gene regulatory circuits, cell--cell communication maps, and knowledge graphs. Despite their importance, currently there is not a broadly reusable foundation model available for graph analysis comparable to those that have transformed language and vision. Existing graph neural networks are typically trained on a single dataset and learn representations specific only to that graph's node features, topology, and label space, limiting their ability to transfer across domains. This lack of generalization is particularly problematic in biology and medicine, where networks vary substantially across cohorts, assays, and institutions. Here we introduce a graph foundation model designed to learn transferable structural representations that are not specific to specific node identities or feature schemes. Our approach leverages feature-agnostic graph properties, including degree statistics, centrality measures, community structure indicators, and diffusion-based signatures, and encodes them as structural prompts. These prompts are integrated with a message-passing backbone to embed diverse graphs into a shared representation space. The model is pretrained once on heterogeneous graphs and subsequently reused on unseen datasets with minimal adaptation. Across multiple benchmarks, our pretrained model matches or exceeds strong supervised baselines while demonstrating superior zero-shot and few-shot generalization on held-out graphs. On the SagePPI benchmark, supervised fine-tuning of the pretrained backbone achieves a mean ROC-AUC of 95.5%, a gain of 21.8% over the best supervised message-passing baseline. The proposed technique thus provides a unique approach toward reusable, foundation-scale models for graph-structured data in biomedical and network science applications.
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
