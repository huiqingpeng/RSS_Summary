---
title: "On the Dynamics & Transferability of Latent Generalization during Memorization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19865"
published: "2026-03-23"
fetched: "2026-03-24T07:23:01.780030"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:On the Dynamics & Transferability of Latent Generalization during Memorization
View PDF HTML (experimental)Abstract:Deep networks have been known to have extraordinary generalization abilities, via mechanisms that aren't yet well understood. It is also known that upon shuffling labels in the training data to varying degrees, deep networks, trained with standard methods, can still achieve perfect or high accuracy on this corrupted training data. This phenomenon is called memorization, and typically comes at the cost of poorer generalization to true labels. Our recent work has demonstrated, that the internal representations of such models retain significantly better latent generalization abilities than is directly apparent from the model. In particular, it has been shown that such latent generalization can be recovered via simple probes (called MASC probes) on the layer-wise representations of the model. However, the origin and dynamics over training of this latent generalization during memorization is not well understood. Here, we track the training dynamics, empirically, and find that latent generalization abilities largely peak early in training, with model generalization. Next, we investigate to what extent the specific nature of the MASC probe is critical for our ability to extract latent generalization from the model's layerwise outputs. To this end, we first examine the mathematical structure of the MASC probe and show that it is a quadratic classifier, i.e. is non-linear. This brings up the question of the extent to which this latent generalization might be linearly decodable from layerwise outputs. To investigate this, we designed a new linear probe for this setting. Next, we consider the question of whether it is possible to transfer latent generalization to model generalization by directly editing model weights. To this end, we devise a way to transfer the latent generalization present in last-layer representations to the model using the new linear probe.
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
