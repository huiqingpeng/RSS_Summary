---
title: "FACE-net: Factual Calibration and Emotion Augmentation for Retrieval-enhanced Emotional Video Captioning"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17455"
published: "2026-03-19"
fetched: "2026-03-19T15:11:08.608522"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:FACE-net: Factual Calibration and Emotion Augmentation for Retrieval-enhanced Emotional Video Captioning
View PDFAbstract:Emotional Video Captioning (EVC) is an emerging task, which aims to describe factual content with the intrinsic emotions expressed in videos. Existing works perceive global emotional cues and then combine with video content to generate descriptions. However, insufficient factual and emotional cues mining and coordination during generation make their methods difficult to deal with the factual-emotional bias, which refers to the factual and emotional requirements being different in different samples on generation. To this end, we propose a retrieval-enhanced framework with FActual Calibration and Emotion augmentation (FACE-net), which through a unified architecture collaboratively mines factual-emotional semantics and provides adaptive and accurate guidance for generation, breaking through the compromising tendency of factual-emotional descriptions in all sample learning. Technically, we firstly introduces an external repository and retrieves the most relevant sentences with the video content to augment the semantic information. Subsequently, our factual calibration via uncertainty estimation module splits the retrieved information into subject-predicate-object triplets, and self-refines and cross-refines different components through video content to effectively mine the factual semantics; while our progressive visual emotion augmentation module leverages the calibrated factual semantics as experts, interacts with the video content and emotion dictionary to generate visual queries and candidate emotions, and then aggregates them to adaptively augment emotions to each factual semantics. Moreover, to alleviate the factual-emotional bias, we design a dynamic bias adjustment routing module to predict and adjust the degree of bias of a sample.
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
