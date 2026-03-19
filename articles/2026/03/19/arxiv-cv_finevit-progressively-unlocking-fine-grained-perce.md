---
title: "FineViT: Progressively Unlocking Fine-Grained Perception with Dense Recaptions"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17326"
published: "2026-03-19"
fetched: "2026-03-19T15:08:20.619260"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:FineViT: Progressively Unlocking Fine-Grained Perception with Dense Recaptions
View PDF HTML (experimental)Abstract:While Multimodal Large Language Models (MLLMs) have experienced rapid advancements, their visual encoders frequently remain a performance bottleneck. Conventional CLIP-based encoders struggle with dense spatial tasks due to the loss of visual details caused by low-resolution pretraining and the reliance on noisy, coarse web-crawled image-text pairs. To overcome these limitations, we introduce FineViT, a novel vision encoder specifically designed to unlock fine-grained perception. By replacing coarse web data with dense recaptions, we systematically mitigate information loss through a progressive training paradigm.: first, the encoder is trained from scratch at a high native resolution on billions of global recaptioned image-text pairs, establishing a robust, detail rich semantic foundation. Subsequently, we further enhance its local perception through LLM alignment, utilizing our curated FineCap-450M dataset that comprises over $450$ million high quality local captions. Extensive experiments validate the effectiveness of the progressive strategy. FineViT achieves state-of-the-art zero-shot recognition and retrieval performance, especially in long-context retrieval, and consistently outperforms multimodal visual encoders such as SigLIP2 and Qwen-ViT when integrated into MLLMs. We hope FineViT could serve as a powerful new baseline for fine-grained visual perception.
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
