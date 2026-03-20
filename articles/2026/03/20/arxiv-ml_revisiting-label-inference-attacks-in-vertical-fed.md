---
title: "Revisiting Label Inference Attacks in Vertical Federated Learning: Why They Are Vulnerable and How to Defend"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18680"
published: "2026-03-20"
fetched: "2026-03-20T12:14:24.211776"
---

Computer Science > Machine Learning
[Submitted on 19 Mar 2026]
Title:Revisiting Label Inference Attacks in Vertical Federated Learning: Why They Are Vulnerable and How to Defend
View PDF HTML (experimental)Abstract:Vertical federated learning (VFL) allows an active party with a top model, and multiple passive parties with bottom models to collaborate. In this scenario, passive parties possessing only features may attempt to infer active party's private labels, making label inference attacks (LIAs) a significant threat. Previous LIA studies have claimed that well-trained bottom models can effectively represent labels. However, we demonstrate that this view is misleading and exposes the vulnerability of existing LIAs. By leveraging mutual information, we present the first observation of the "model compensation" phenomenon in VFL. We theoretically prove that, in VFL, the mutual information between layer outputs and labels increases with layer depth, indicating that bottom models primarily extract feature information while the top model handles label mapping. Building on this insight, we introduce task reassignment to show that the success of existing LIAs actually stems from the distribution alignment between features and labels. When this alignment is disrupted, the performance of LIAs declines sharply or even fails entirely. Furthermore, the implications of this insight for defenses are also investigated. We propose a zero-overhead defense technique based on layer adjustment. Extensive experiments across five datasets and five representative model architectures indicate that shifting cut layers forward to increase the proportion of top model layers in the entire model not only improves resistance to LIAs but also enhances other defenses.
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
