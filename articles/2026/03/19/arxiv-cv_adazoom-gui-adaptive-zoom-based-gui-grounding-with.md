---
title: "AdaZoom-GUI: Adaptive Zoom-based GUI Grounding with Instruction Refinement"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17441"
published: "2026-03-19"
fetched: "2026-03-19T15:10:57.705332"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:AdaZoom-GUI: Adaptive Zoom-based GUI Grounding with Instruction Refinement
View PDF HTML (experimental)Abstract:GUI grounding is a critical capability for vision-language models (VLMs) that enables automated interaction with graphical user interfaces by locating target elements from natural language instructions. However, grounding on GUI screenshots remains challenging due to high-resolution images, small UI elements, and ambiguous user instructions. In this work, we propose AdaZoom-GUI, an adaptive zoom-based GUI grounding framework that improves both localization accuracy and instruction understanding. Our approach introduces an instruction refinement module that rewrites natural language commands into explicit and detailed descriptions, allowing the grounding model to focus on precise element localization. In addition, we design a conditional zoom-in strategy that selectively performs a second-stage inference on predicted small elements, improving localization accuracy while avoiding unnecessary computation and context loss on simpler cases. To support this framework, we construct a high-quality GUI grounding dataset and train the grounding model using Group Relative Policy Optimization (GRPO), enabling the model to predict both click coordinates and element bounding boxes. Experiments on public benchmarks demonstrate that our method achieves state-of-the-art performance among models with comparable or even larger parameter sizes, highlighting its effectiveness for high-resolution GUI understanding and practical GUI agent deployment.
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
