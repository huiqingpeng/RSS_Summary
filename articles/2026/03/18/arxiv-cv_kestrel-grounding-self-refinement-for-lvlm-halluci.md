---
title: "Kestrel: Grounding Self-Refinement for LVLM Hallucination Mitigation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16664"
published: "2026-03-18"
fetched: "2026-03-18T18:17:14.979680"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:Kestrel: Grounding Self-Refinement for LVLM Hallucination Mitigation
View PDF HTML (experimental)Abstract:Large vision-language models (LVLMs) have become increasingly strong but remain prone to hallucinations in multimodal tasks, which significantly narrows their deployment. As training these LVLMs to avoid hallucinations becomes prohibitively expensive for larger models, training-free methods offer a cheap and flexible solution to this problem, yet existing approaches based on decoding or tool use often bring limited gains and/or weak interpretability. We propose Kestrel, a training-free framework for LVLM hallucination mitigation that combines an explicit visual-grounding agent with evidence-verified self-refinement mechanism. In detail, Kestrel first collects explicit visual evidence and converts tool outputs into reusable and structured textual evidence. Second, to take full advantage of these evidence, Kestrel verifies them via an LVLM judge for evidence checking, then iteratively self-refine answers based on verified evidence to reduce the risk of over-correction. Extensive experiments show that Kestrel improves performance over strong baselines across hallucination benchmarks (e.g., average +3.31% on POPE and +28.34 on MME-Hallucination with Qwen3-VL), while providing transparent verification traces for hallucination diagnosis and analysis -- e.g., both the integrated self-refinement module and grounding agent contributing an average +2.0% gain on POPE.
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
