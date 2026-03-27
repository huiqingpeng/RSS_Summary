---
title: "DCARL: A Divide-and-Conquer Framework for Autoregressive Long-Trajectory Video Generation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.24835"
published: "2026-03-27"
fetched: "2026-03-28T07:17:20.954055"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 25 Mar 2026]
Title:DCARL: A Divide-and-Conquer Framework for Autoregressive Long-Trajectory Video Generation
View PDF HTML (experimental)Abstract:Long-trajectory video generation is a crucial yet challenging task for world modeling primarily due to the limited scalability of existing video diffusion models (VDMs). Autoregressive models, while offering infinite rollout, suffer from visual drift and poor controllability. To address these issues, we propose DCARL, a novel divide-and-conquer, autoregressive framework that effectively combines the structural stability of the divide-and-conquer scheme with the high-fidelity generation of VDMs. Our approach first employs a dedicated Keyframe Generator trained without temporal compression to establish long-range, globally consistent structural anchors. Subsequently, an Interpolation Generator synthesizes the dense frames in an autoregressive manner with overlapping segments, utilizing the keyframes for global context and a single clean preceding frame for local coherence. Trained on a large-scale internet long trajectory video dataset, our method achieves superior performance in both visual quality (lower FID and FVD) and camera adherence (lower ATE and ARE) compared to state-of-the-art autoregressive and divide-and-conquer baselines, demonstrating stable and high-fidelity generation for long trajectory videos up to 32 seconds in length.
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
