---
title: "Solution for 10th Competition on Ambivalence/Hesitancy (AH) Video Recognition Challenge using Divergence-Based Multimodal Fusion"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16939"
published: "2026-03-19"
fetched: "2026-03-19T14:21:29.213502"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 15 Mar 2026]
Title:Solution for 10th Competition on Ambivalence/Hesitancy (AH) Video Recognition Challenge using Divergence-Based Multimodal Fusion
View PDF HTML (experimental)Abstract:We address the Ambivalence/Hesitancy (A/H) Video Recognition Challenge at the 10th ABAW Competition (CVPR 2026). We propose a divergence-based multimodal fusion that explicitly measures cross-modal conflict between visual, audio, and textual channels. Visual features are encoded as Action Units (AUs) extracted via Py-Feat, audio via Wav2Vec 2.0, and text via BERT. Each modality is processed by a BiLSTM with attention pooling and projected into a shared embedding space. The fusion module computes pairwise absolute differences between modality embeddings, directly capturing the incongruence that characterizes A/H. On the BAH dataset, our approach achieves a Macro F1 of 0.6808 on the validation test set, outperforming the challenge baseline of 0.2827. Statistical analysis across 1{,}132 videos confirms that temporal variability of AUs is the dominant visual discriminator of A/H.
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
