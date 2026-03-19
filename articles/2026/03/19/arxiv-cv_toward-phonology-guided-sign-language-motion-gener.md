---
title: "Toward Phonology-Guided Sign Language Motion Generation: A Diffusion Baseline and Conditioning Analysis"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17388"
published: "2026-03-19"
fetched: "2026-03-19T15:09:49.007250"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:Toward Phonology-Guided Sign Language Motion Generation: A Diffusion Baseline and Conditioning Analysis
View PDF HTML (experimental)Abstract:Generating natural, correct, and visually smooth 3D avatar sign language motion conditioned on the text inputs continues to be very challenging. In this work, we train a generative model of 3D body motion and explore the role of phonological attribute conditioning for sign language motion generation, using ASL-LEX 2.0 annotations such as hand shape, hand location and movement. We first establish a strong diffusion baseline using an Human Motion MDM-style diffusion model with SMPL-X representation, which outperforms SignAvatar, a state-of-the-art CVAE method, on gloss discriminability metrics. We then systematically study the role of text conditioning using different text encoders (CLIP vs. T5), conditioning modes (gloss-only vs. gloss+phonological attributes), and attribute notation format (symbolic vs. natural language). Our analysis reveals that translating symbolic ASL-LEX notations to natural language is a necessary condition for effective CLIP-based attribute conditioning, while T5 is largely unaffected by this translation. Furthermore, our best-performing variant (CLIP with mapped attributes) outperforms SignAvatar across all metrics. These findings highlight input representation as a critical factor for text-encoder-based attribute conditioning, and motivate structured conditioning approaches where gloss and phonological attributes are encoded through independent pathways.
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
