---
title: "TuneShift-KD: Knowledge Distillation and Transfer for Fine-tuned Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24518"
published: "2026-03-27"
fetched: "2026-03-28T07:11:08.873716"
---

Computer Science > Machine Learning
[Submitted on 25 Mar 2026]
Title:TuneShift-KD: Knowledge Distillation and Transfer for Fine-tuned Models
View PDFAbstract:To embed domain-specific or specialized knowledge into pre-trained foundation models, fine-tuning using techniques such as parameter efficient fine-tuning (e.g. LoRA) is a common practice. However, as new LLM architectures and pre-trained models emerge, transferring this specialized knowledge to newer models becomes an important task. In many scenarios, the original specialized data may be unavailable due to privacy or commercial restrictions, necessitating distillation and transfer of this specialized knowledge from the fine-tuned base model to a different pre-trained model. We present TuneShift-KD, a novel approach that automatically distills specialized knowledge from a fine-tuned model to a target model using only a few examples representative of the specialized information. Our key insight is that specialized knowledge can be identified through perplexity differences between base and fine-tuned models: prompts where the fine-tuned model responds confidently (low perplexity), but the base model struggles (high perplexity), indicate queries corresponding to the specialized knowledge learned by the fine-tuned model. TuneShift-KD leverages this insight to create a synthetic training dataset to transfer the specialized knowledge. Using an iterative process, TuneShift-KD generates more prompts similar to those that generated responses with specialized knowledge. TuneShift-KD does not require training discriminators or access to training datasets. It is an automated approach that only requires the initial fine-tuned and base models and a few representative prompts. Our experiments demonstrate that models fine-tuned using TuneShift-KD achieve higher accuracy than prior approaches, enabling ease of deployment and more effective transfer of the specialized knowledge.
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
