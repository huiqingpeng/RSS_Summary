---
title: "How to Achieve Prototypical Birth and Death for OOD Detection?"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15650"
published: "2026-03-18"
fetched: "2026-03-18T15:32:51.783697"
---

Computer Science > Machine Learning
[Submitted on 6 Mar 2026]
Title:How to Achieve Prototypical Birth and Death for OOD Detection?
View PDF HTML (experimental)Abstract:Out-of-Distribution (OOD) detection is crucial for the secure deployment of machine learning models, and prototype-based learning methods are among the mainstream strategies for achieving OOD detection. Existing prototype-based learning methods generally rely on a fixed number of prototypes. This static assumption fails to adapt to the inherent complexity differences across various categories. Currently, there is still a lack of a mechanism that can adaptively adjust the number of prototypes based on data complexity. Inspired by the processes of cell birth and death in biology, we propose a novel method named PID (Prototype bIrth and Death) to adaptively adjust the prototype count based on data complexity. This method relies on two dynamic mechanisms during the training process: prototype birth and prototype death. The birth mechanism instantiates new prototypes in data regions with insufficient representation by identifying the overload level of existing prototypes, thereby meticulously capturing intra-class substructures. Conversely, the death mechanism reinforces the decision boundary by pruning prototypes with ambiguous class boundaries through evaluating their discriminability. Through birth and death, the number of prototypes can be dynamically adjusted according to the data complexity, leading to the learning of more compact and better-separated In-Distribution (ID) embeddings, which significantly enhances the capability to detect OOD samples. Experiments demonstrate that our dynamic method, PID, significantly outperforms existing methods on benchmarks such as CIFAR-100, achieving State-of-the-Art (SOTA) performance, especially on the FPR95 metric.
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
