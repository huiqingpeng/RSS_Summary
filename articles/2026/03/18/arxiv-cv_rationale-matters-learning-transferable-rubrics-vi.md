---
title: "Rationale Matters: Learning Transferable Rubrics via Proxy-Guided Critique for VLMReward Models"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16600"
published: "2026-03-18"
fetched: "2026-03-18T18:15:39.267293"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:Rationale Matters: Learning Transferable Rubrics via Proxy-Guided Critique for VLMReward Models
View PDF HTML (experimental)Abstract:Generative reward models (GRMs) for vision-language models (VLMs) often evaluate outputs via a three-stage pipeline: rubric generation, criterion-based scoring, and a final verdict. However, the intermediate rubric is rarely optimized directly. Prior work typically either treats rubrics as incidental or relies on expensive LLM-as-judge checks that provide no differentiable signal and limited training-time guidance. We propose Proxy-GRM, which introduces proxy-guided rubric verification into Reinforcement Learning (RL) to explicitly enhance rubric quality. Concretely, we train lightweight proxy agents (Proxy-SFT and Proxy-RL) that take a candidate rubric together with the original query and preference pair, and then predict the preference ordering using only the rubric as evidence. The proxy's prediction accuracy serves as a rubric-quality reward, incentivizing the model to produce rubrics that are internally consistent and transferable. With ~50k data samples, Proxy-GRM reaches state-of-the-art results on the VL-Reward Bench, Multimodal Reward Bench, and MM-RLHF-Reward Bench, outperforming the methods trained on four times the data. Ablations show Proxy-SFT is a stronger verifier than Proxy-RL, and implicit reward aggregation performs best. Crucially, the learned rubrics transfer to unseen evaluators, improving reward accuracy at test time without additional training. Our code is available at this https URL.
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
