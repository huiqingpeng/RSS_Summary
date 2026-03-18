---
title: "Beyond the Embedding Bottleneck: Adaptive Retrieval-Augmented 3D CT Report Generation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.15822"
published: "2026-03-18"
fetched: "2026-03-18T17:19:04.156008"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 16 Mar 2026]
Title:Beyond the Embedding Bottleneck: Adaptive Retrieval-Augmented 3D CT Report Generation
View PDF HTML (experimental)Abstract:Automated radiology report generation from 3D CT volumes often suffers from incomplete pathology coverage. We provide empirical evidence that this limitation stems from a representational bottleneck: contrastive 3D CT embeddings encode discriminative pathology signals, yet exhibit severe dimensional concentration, with as few as 2 effective dimensions out of 512. Corroborating this, scaling the language model yields no measurable improvement, suggesting that the bottleneck lies in the visual representation rather than the generator. This bottleneck limits both generation and retrieval; naive static retrieval fails to improve clinical efficacy and can even degrade performance. We propose \textbf{AdaRAG-CT}, an adaptive augmentation framework that compensates for this visual bottleneck by introducing supplementary textual information through controlled retrieval and selectively integrating it during generation. On the CT-RATE benchmark, AdaRAG-CT achieves state-of-the-art clinical efficacy, improving Clinical F1 from 0.420 (CT-Agent) to 0.480 (+6 points); ablation studies confirm that both the retrieval and generation components contribute to the improvement. Code is available at this https URL.
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
