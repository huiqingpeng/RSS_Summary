---
title: "Complementary Text-Guided Attention for Zero-Shot Adversarial Robustness"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18598"
published: "2026-03-20"
fetched: "2026-03-20T15:12:32.386916"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 19 Mar 2026]
Title:Complementary Text-Guided Attention for Zero-Shot Adversarial Robustness
View PDF HTML (experimental)Abstract:Due to the impressive zero-shot capabilities, pre-trained vision-language models (e.g., CLIP), have attracted widespread attention and adoption across various domains. Nonetheless, CLIP has been observed to be susceptible to adversarial examples. Through experimental analysis, we have observed a phenomenon wherein adversarial perturbations induce shifts in text-guided attention. Building upon this observation, we propose a simple yet effective strategy: Text-Guided Attention for Zero-Shot Robustness (TGA-ZSR). This framework incorporates two components: Local Attention Refinement Module and Global Attention Constraint Module. Our goal is to maintain the generalization of the CLIP model and enhance its adversarial robustness. Additionally, the Global Attention Constraint Module acquires text-guided attention from both the target and original models using clean examples. Its objective is to maintain model performance on clean samples while enhancing overall robustness. However, we observe that the method occasionally focuses on irrelevant or spurious features, which can lead to suboptimal performance and undermine its robustness in certain scenarios. To overcome this limitation, we further propose a novel approach called Complementary Text-Guided Attention (Comp-TGA). This method integrates two types of foreground attention: attention guided by the class prompt and reversed attention driven by the non-class prompt. These complementary attention mechanisms allow the model to capture a more comprehensive and accurate representation of the foreground. The experiments validate that TGA-ZSR and Comp-TGA yield 9.58% and 11.95% improvements respectively, in zero-shot robust accuracy over the current state-of-the-art techniques across 16 datasets.
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
