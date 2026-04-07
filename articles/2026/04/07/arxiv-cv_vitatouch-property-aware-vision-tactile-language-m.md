---
title: "VitaTouch: Property-Aware Vision-Tactile-Language Model for Robotic Quality Inspection in Manufacturing"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2604.03322"
published: "2026-04-07"
fetched: "2026-04-08T07:02:49.536282"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 2 Apr 2026]
Title:VitaTouch: Property-Aware Vision-Tactile-Language Model for Robotic Quality Inspection in Manufacturing
View PDF HTML (experimental)Abstract:Quality inspection in smart manufacturing requires identifying intrinsic material and surface properties beyond visible geometry, yet vision-only methods remain vulnerable to occlusion and reflection. We propose VitaTouch, a property-aware vision-tactile-language model for material-property inference and natural-language attribute description. VitaTouch uses modality-specific encoders and a dual Q-Former to extract language-relevant visual and tactile features, which are compressed into prefix tokens for a large language model. We align each modality with text and explicitly couple vision and touch through contrastive learning. We also construct VitaSet, a multimodal dataset with 186 objects, 52k images, and 5.1k human-verified instruction-answer pairs. VitaTouch achieves the best performance on HCT and the overall TVL benchmark, while remaining competitive on SSVTP. On VitaSet, it reaches 88.89% hardness accuracy, 75.13% roughness accuracy, and 54.81% descriptor recall; the material-description task further achieves a peak semantic similarity of 0.9009. With LoRA-based fine-tuning, VitaTouch attains 100.0%, 96.0%, and 92.0% accuracy for 2-, 3-, and 5-category defect recognition, respectively, and delivers 94.0% closed-loop recognition accuracy and 94.0% end-to-end sorting success in 100 laboratory robotic trials. More details are available at the project page: this https URL
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
ScienceCast (What is ScienceCast?)
Demos
Recommenders and Search Tools
Influence Flower (What are Influence Flowers?)
CORE Recommender (What is CORE?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
