---
title: "V-Reflection: Transforming MLLMs from Passive Observers to Active Interrogators"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2604.03307"
published: "2026-04-07"
fetched: "2026-04-08T07:02:44.021954"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 31 Mar 2026]
Title:V-Reflection: Transforming MLLMs from Passive Observers to Active Interrogators
View PDF HTML (experimental)Abstract:Multimodal Large Language Models (MLLMs) have achieved remarkable success, yet they remain prone to perception-related hallucinations in fine-grained tasks. This vulnerability arises from a fundamental limitation: their reasoning is largely restricted to the language domain, treating visual input as a static, reasoning-agnostic preamble rather than a dynamic participant. Consequently, current models act as passive observers, unable to re-examine visual details to ground their evolving reasoning states. To overcome this, we propose V-Reflection, a framework that transforms the MLLM into an active interrogator through a "think-then-look" visual reflection mechanism. During reasoning, latent states function as dynamic probes that actively interrogate the visual feature space, grounding each reasoning step for task-critical evidence. Our approach employs a two-stage distillation strategy. First, the Box-Guided Compression (BCM) module establishes stable pixel-to-latent targets through explicit spatial grounding. Next, a Dynamic Autoregressive Compression (DAC) module maps the model's hidden states into dynamic probes that interrogate the global visual feature map. By distilling the spatial expertise of the BCM teacher into the DAC student, V-Reflection internalizes the ability to localize task-critical evidence. During inference, both modules remain entirely inactive, maintaining a purely end-to-end autoregressive decoding in the latent space with optimal efficiency. Extensive experiments demonstrate the effectiveness of our V-Reflection across six perception-intensive benchmarks, significantly narrowing the fine-grained perception gap. Visualizations confirm that latent reasoning autonomously localizes task-critical visual evidence.
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
ScienceCast (What is ScienceCast?)
Demos
Recommenders and Search Tools
Influence Flower (What are Influence Flowers?)
CORE Recommender (What is CORE?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
