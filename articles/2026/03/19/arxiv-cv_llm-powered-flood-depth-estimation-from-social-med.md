---
title: "LLM-Powered Flood Depth Estimation from Social Media Imagery: A Vision-Language Model Framework with Mechanistic Interpretability for Transportation Resilience"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17108"
published: "2026-03-19"
fetched: "2026-03-19T15:05:07.395533"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:LLM-Powered Flood Depth Estimation from Social Media Imagery: A Vision-Language Model Framework with Mechanistic Interpretability for Transportation Resilience
View PDFAbstract:Urban flooding poses an escalating threat to transportation network continuity, yet no operational system currently provides real-time, street-level flood depth information at the centimeter resolution required for dynamic routing, electric vehicle (EV) safety, and autonomous vehicle (AV) operations. This study presents FloodLlama, a fine-tuned open-source vision-language model (VLM) for continuous flood depth estimation from single street-level images, supported by a multimodal sensing pipeline using TikTok data. A synthetic dataset of approximately 190000 images was generated, covering seven vehicle types, four weather conditions, and 41 depth levels (0-40 cm at 1 cm resolution). Progressive curriculum training enabled coarse-to-fine learning, while LLaMA 3.2-11B Vision was fine-tuned using QLoRA. Evaluation across 34797 trials reveals a depth-dependent prompt effect: simple prompts perform better for shallow flooding, whereas chain-of-thought (CoT) reasoning improves performance at greater depths. FloodLlama achieves a mean absolute error (MAE) below 0.97 cm and Acc@5cm above 93.7% for deep flooding, exceeding 96.8% for shallow depths. A five-phase mechanistic interpretability framework identifies layer L23 as the critical depth-encoding transition and enables selective fine-tuning that reduces trainable parameters by 76-80% while maintaining accuracy. The Tier 3 configuration achieves 98.62% accuracy on real-world data and shows strong robustness under visual occlusion. A TikTok-based data pipeline, validated on 676 annotated flood frames from Detroit, demonstrates the feasibility of real-time, crowd-sourced flood sensing. The proposed framework provides a scalable, infrastructure-free solution with direct implications for EV safety, AV deployment, and resilient transportation management.
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
