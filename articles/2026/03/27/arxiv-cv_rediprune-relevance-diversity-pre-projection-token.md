---
title: "ReDiPrune: Relevance-Diversity Pre-Projection Token Pruning for Efficient Multimodal LLMs"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.24680"
published: "2026-03-27"
fetched: "2026-03-28T07:14:22.601530"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 25 Mar 2026]
Title:ReDiPrune: Relevance-Diversity Pre-Projection Token Pruning for Efficient Multimodal LLMs
View PDF HTML (experimental)Abstract:Recent multimodal large language models are computationally expensive because Transformers must process a large number of visual tokens. We present \textbf{ReDiPrune}, a training-free token pruning method applied before the vision-language projector, where visual features remain rich and discriminative. Unlike post-projection pruning methods that operate on compressed representations, ReDiPrune selects informative tokens directly from vision encoder outputs, preserving fine-grained spatial and semantic cues. Each token is scored by a lightweight rule that jointly consider text-conditioned relevance and max-min diversity, ensuring the selected tokens are both query-relevant and non-redundant. ReDiPrune is fully plug-and-play, requiring no retraining or architectural modifications, and can be seamlessly inserted between the encoder and projector. Across four video and five image benchmarks, it consistently improves the accuracy-efficiency trade-off. For example, on EgoSchema with LLaVA-NeXT-Video-7B, retaining only 15\% of visual tokens yields a +2.0\% absolute accuracy gain while reducing computation by more than $6\times$ in TFLOPs. Code is available at this https URL.
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
