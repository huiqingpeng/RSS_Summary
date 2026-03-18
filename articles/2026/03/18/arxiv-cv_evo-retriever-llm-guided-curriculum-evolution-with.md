---
title: "Evo-Retriever: LLM-Guided Curriculum Evolution with Viewpoint-Pathway Collaboration for Multimodal Document Retrieval"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16455"
published: "2026-03-18"
fetched: "2026-03-18T18:13:52.033693"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:Evo-Retriever: LLM-Guided Curriculum Evolution with Viewpoint-Pathway Collaboration for Multimodal Document Retrieval
View PDF HTML (experimental)Abstract:Visual-language models (VLMs) excel at data mappings, but real-world document heterogeneity and unstructuredness disrupt the consistency of cross-modal embeddings. Recent late-interaction methods enhance image-text alignment through multi-vector representations, yet traditional training with limited samples and static strategies cannot adapt to the model's dynamic evolution, causing cross-modal retrieval confusion. To overcome this, we introduce Evo-Retriever, a retrieval framework featuring an LLM-guided curriculum evolution built upon a novel Viewpoint-Pathway collaboration. First, we employ multi-view image alignment to enhance fine-grained matching via multi-scale and multi-directional perspectives. Then, a bidirectional contrastive learning strategy generates "hard queries" and establishes complementary learning paths for visual and textual disambiguation to rebalance supervision. Finally, the model-state summary from the above collaboration is fed into an LLM meta-controller, which adaptively adjusts the training curriculum using expert knowledge to promote the model's evolution. On ViDoRe V2 and MMEB (VisDoc), Evo-Retriever achieves state-of-the-art performance, with nDCG@5 scores of 65.2% and 77.1%.
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
