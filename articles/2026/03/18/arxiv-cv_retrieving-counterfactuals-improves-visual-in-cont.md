---
title: "Retrieving Counterfactuals Improves Visual In-Context Learning"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16737"
published: "2026-03-18"
fetched: "2026-03-18T18:19:47.076220"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:Retrieving Counterfactuals Improves Visual In-Context Learning
View PDF HTML (experimental)Abstract:Vision-language models (VLMs) have achieved impressive performance across a wide range of multimodal reasoning tasks, but they often struggle to disentangle fine-grained visual attributes and reason about underlying causal relationships. In-context learning (ICL) offers a promising avenue for VLMs to adapt to new tasks, but its effectiveness critically depends on the selection of demonstration examples. Existing retrieval-augmented approaches typically rely on passive similarity-based retrieval, which tends to select correlated but non-causal examples, amplifying spurious associations and limiting model robustness. We introduce CIRCLES (Composed Image Retrieval for Causal Learning Example Selection), a novel framework that actively constructs demonstration sets by retrieving counterfactual-style examples through targeted, attribute-guided composed image retrieval. By incorporating counterfactual-style examples, CIRCLES enables VLMs to implicitly reason about the causal relations between attributes and outcomes, moving beyond superficial correlations and fostering more robust and grounded reasoning. Comprehensive experiments on four diverse datasets demonstrate that CIRCLES consistently outperforms existing methods across multiple architectures, especially on small-scale models, with pronounced gains under information scarcity. Furthermore, CIRCLES retrieves more diverse and causally informative examples, providing qualitative insights into how models leverage in-context demonstrations for improved reasoning. Our code is available at this https URL.
Current browse context:
cs.CV
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
