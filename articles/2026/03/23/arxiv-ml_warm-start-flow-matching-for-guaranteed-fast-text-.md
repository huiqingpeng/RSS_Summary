---
title: "Warm-Start Flow Matching for Guaranteed Fast Text/Image Generation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19360"
published: "2026-03-23"
fetched: "2026-03-24T07:18:03.944238"
---

Computer Science > Machine Learning
[Submitted on 19 Mar 2026]
Title:Warm-Start Flow Matching for Guaranteed Fast Text/Image Generation
View PDF HTML (experimental)Abstract:Current auto-regressive (AR) LLMs, diffusion-based text/image generative models, and recent flow matching (FM) algorithms are capable of generating premium quality text/image samples. However, the inference or sample generation in these models is often very time-consuming and computationally demanding, mainly due to large numbers of function evaluations corresponding to the lengths of tokens or the numbers of diffusion steps. This also necessitates heavy GPU resources, time, and electricity. In this work we propose a novel solution to reduce the sample generation time of flow matching algorithms by a guaranteed speed-up factor, without sacrificing the quality of the generated samples. Our key idea is to utilize computationally lightweight generative models whose generation time is negligible compared to that of the target AR/FM models. The draft samples from a lightweight model, whose quality is not satisfactory but fast to generate, are regarded as an initial distribution for a FM algorithm. Unlike conventional usage of FM that takes a pure noise (e.g., Gaussian or uniform) initial distribution, the draft samples are already of decent quality, so we can set the starting time to be closer to the end time rather than 0 in the pure noise FM case. This will significantly reduce the number of time steps to reach the target data distribution, and the speed-up factor is guaranteed. Our idea, dubbed {\em Warm-Start FM} or WS-FM, can essentially be seen as a {\em learning-to-refine} generative model from low-quality draft samples to high-quality samples. As a proof of concept, we demonstrate the idea on some synthetic toy data as well as real-world text and image generation tasks, illustrating that our idea offers guaranteed speed-up in sample generation without sacrificing the quality of the generated samples.
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
IArxiv Recommender
(What is IArxiv?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
