---
title: "Sparse but not Simpler: A Multi-Level Interpretability Analysis of Vision Transformers"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.15919"
published: "2026-03-18"
fetched: "2026-03-18T17:19:17.674916"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 16 Mar 2026]
Title:Sparse but not Simpler: A Multi-Level Interpretability Analysis of Vision Transformers
View PDF HTML (experimental)Abstract:Sparse neural networks are often hypothesized to be more interpretable than dense models, motivated by findings that weight sparsity can produce compact circuits in language models. However, it remains unclear whether structural sparsity itself leads to improved semantic interpretability. In this work, we systematically evaluate the relationship between weight sparsity and interpretability in Vision Transformers using DeiT-III B/16 models pruned with Wanda. To assess interpretability comprehensively, we introduce \textbf{IMPACT}, a multi-level framework that evaluates interpretability across four complementary levels: neurons, layer representations, task circuits, and model-level attribution. Layer representations are analyzed using BatchTopK sparse autoencoders, circuits are extracted via learnable node masking, and explanations are evaluated with transformer attribution using insertion and deletion metrics. Our results reveal a clear structural effect but limited interpretability gains. Sparse models produce circuits with approximately $2.5\times$ fewer edges than dense models, yet the fraction of active nodes remains similar or higher, indicating that pruning redistributes computation rather than isolating simpler functional modules. Consistent with this observation, sparse models show no systematic improvements in neuron-level selectivity, SAE feature interpretability, or attribution faithfulness. These findings suggest that structural sparsity alone does not reliably yield more interpretable vision models, highlighting the importance of evaluation frameworks that assess interpretability beyond circuit compactness.
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
