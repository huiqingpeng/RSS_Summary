---
title: "When Thinking Hurts: Mitigating Visual Forgetting in Video Reasoning via Frame Repetition"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16256"
published: "2026-03-18"
fetched: "2026-03-18T18:09:33.504609"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:When Thinking Hurts: Mitigating Visual Forgetting in Video Reasoning via Frame Repetition
View PDF HTML (experimental)Abstract:Recently, Multimodal Large Language Models (MLLMs) have demonstrated significant potential in complex visual tasks through the integration of Chain-of-Thought (CoT) reasoning. However, in Video Question Answering, extended thinking processes do not consistently yield performance gains and may even lead to degradation due to ``visual anchor drifting'', where models increasingly rely on self-generated text, sidelining visual inputs and causing hallucinations. While existing mitigations typically introduce specific mechanisms for the model to re-attend to visual inputs during inference, these approaches often incur prohibitive training costs and suffer from poor generalizability across different architectures. To address this, we propose FrameRepeat, an automated enhancement framework which features a lightweight repeat scoring module that enables Video-LLMs to autonomously identify which frames should be reinforced. We introduce a novel training strategy, Add-One-In (AOI), that uses MLLM output probabilities to generate supervision signals representing repeat gain. This can be used to train a frame scoring network, which guides the frame repetition behavior. Experimental results across multiple models and datasets demonstrate that FrameRepeat is both effective and generalizable in strengthening important visual cues during the reasoning process.
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
