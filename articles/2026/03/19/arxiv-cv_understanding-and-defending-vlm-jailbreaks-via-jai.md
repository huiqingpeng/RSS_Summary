---
title: "Understanding and Defending VLM Jailbreaks via Jailbreak-Related Representation Shift"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17372"
published: "2026-03-19"
fetched: "2026-03-19T15:09:11.275596"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:Understanding and Defending VLM Jailbreaks via Jailbreak-Related Representation Shift
View PDF HTML (experimental)Abstract:Large vision-language models (VLMs) often exhibit weakened safety alignment with the integration of the visual modality. Even when text prompts contain explicit harmful intent, adding an image can substantially increase jailbreak success rates. In this paper, we observe that VLMs can clearly distinguish benign inputs from harmful ones in their representation space. Moreover, even among harmful inputs, jailbreak samples form a distinct internal state that is separable from refusal samples. These observations suggest that jailbreaks do not arise from a failure to recognize harmful intent. Instead, the visual modality shifts representations toward a specific jailbreak state, thereby leading to a failure to trigger refusal. To quantify this transition, we identify a jailbreak direction and define the jailbreak-related shift as the component of the image-induced representation shift along this direction. Our analysis shows that the jailbreak-related shift reliably characterizes jailbreak behavior, providing a unified explanation for diverse jailbreak scenarios. Finally, we propose a defense method that enhances VLM safety by removing the jailbreak-related shift (JRS-Rem) at inference time. Experiments show that JRS-Rem provides strong defense across multiple scenarios while preserving performance on benign tasks.
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
