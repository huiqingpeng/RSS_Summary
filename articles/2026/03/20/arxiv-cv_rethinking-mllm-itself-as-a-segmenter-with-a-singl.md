---
title: "Rethinking MLLM Itself as a Segmenter with a Single Segmentation Token"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.19026"
published: "2026-03-20"
fetched: "2026-03-20T15:18:11.309985"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 19 Mar 2026]
Title:Rethinking MLLM Itself as a Segmenter with a Single Segmentation Token
View PDF HTML (experimental)Abstract:Recent segmentation methods leveraging Multi-modal Large Language Models (MLLMs) have shown reliable object-level segmentation and enhanced spatial perception. However, almost all previous methods predominantly rely on specialist mask decoders to interpret masks from generated segmentation-related embeddings and visual features, or incorporate multiple additional tokens to assist. This paper aims to investigate whether and how we can unlock segmentation from MLLM itSELF with 1 segmentation Embedding (SELF1E) while achieving competitive results, which eliminates the need for external decoders. To this end, our approach targets the fundamental limitation of resolution reduction in pixel-shuffled image features from MLLMs. First, we retain image features at their original uncompressed resolution, and refill them with residual features extracted from MLLM-processed compressed features, thereby improving feature precision. Subsequently, we integrate pixel-unshuffle operations on image features with and without LLM processing, respectively, to unleash the details of compressed features and amplify the residual features under uncompressed resolution, which further enhances the resolution of refilled features. Moreover, we redesign the attention mask with dual perception pathways, i.e., image-to-image and image-to-segmentation, enabling rich feature interaction between pixels and the segmentation token. Comprehensive experiments across multiple segmentation tasks validate that SELF1E achieves performance competitive with specialist mask decoder-based methods, demonstrating the feasibility of decoder-free segmentation in MLLMs. Project page: this https URL.
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
