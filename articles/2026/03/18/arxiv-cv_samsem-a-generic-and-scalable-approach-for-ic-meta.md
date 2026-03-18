---
title: "SAMSEM -- A Generic and Scalable Approach for IC Metal Line Segmentation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16548"
published: "2026-03-18"
fetched: "2026-03-18T18:23:30.099433"
---

Computer Science > Cryptography and Security
[Submitted on 17 Mar 2026]
Title:SAMSEM -- A Generic and Scalable Approach for IC Metal Line Segmentation
View PDFAbstract:In light of globalized hardware supply chains, the assurance of hardware components has gained significant interest, particularly in cryptographic applications and high-stakes scenarios. Identifying metal lines on scanning electron microscope (SEM) images of integrated circuits (ICs) is one essential step in verifying the absence of malicious circuitry in chips manufactured in untrusted environments. Due to varying manufacturing processes and technologies, such verification usually requires tuning parameters and algorithms for each target IC. Often, a machine learning model trained on images of one IC fails to accurately detect metal lines on other ICs. To address this challenge, we create SAMSEM by adapting Meta's Segment Anything Model 2 (SAM2) to the domain of IC metal line segmentation. Specifically, we develop a multi-scale segmentation approach that can handle SEM images of varying sizes, resolutions, and magnifications. Furthermore, we deploy a topology-based loss alongside pixel-based losses to focus our segmentation on electrical connectivity rather than pixel-level accuracy. Based on a hyperparameter optimization, we then fine-tune the SAM2 model to obtain a model that generalizes across different technology nodes, manufacturing materials, sample preparation methods, and SEM imaging technologies. To this end, we leverage an unprecedented dataset of SEM images obtained from 48 metal layers across 14 different ICs. When fine-tuned on seven ICs, SAMSEM achieves an error rate as low as 0.72% when evaluated on other images from the same ICs. For the remaining seven unseen ICs, it still achieves error rates as low as 5.53%. Finally, when fine-tuned on all 14 ICs, we observe an error rate of 0.62%. Hence, SAMSEM proves to be a reliable tool that significantly advances the frontier in metal line segmentation, a key challenge in post-manufacturing IC verification.
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
