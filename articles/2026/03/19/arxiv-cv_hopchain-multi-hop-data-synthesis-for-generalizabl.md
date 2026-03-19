---
title: "HopChain: Multi-Hop Data Synthesis for Generalizable Vision-Language Reasoning"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17024"
published: "2026-03-19"
fetched: "2026-03-19T15:03:42.367354"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:HopChain: Multi-Hop Data Synthesis for Generalizable Vision-Language Reasoning
View PDF HTML (experimental)Abstract:VLMs show strong multimodal capabilities, but they still struggle with fine-grained vision-language reasoning. We find that long CoT reasoning exposes diverse failure modes, including perception, reasoning, knowledge, and hallucination errors, which can compound across intermediate steps. However, most existing vision-language data used for RLVR does not involve complex reasoning chains that rely on visual evidence throughout, leaving these weaknesses largely unexposed. We therefore propose HopChain, a scalable framework for synthesizing multi-hop vision-language reasoning data specifically for RLVR training of VLMs. Each synthesized multi-hop query forms a logically dependent chain of instance-grounded hops, where earlier hops establish the instances, sets, or conditions needed for later hops, while the final answer remains a specific, unambiguous number suitable for verifiable rewards. We add the multi-hop data synthesized by HopChain to the original RLVR data used to train Qwen3.5-35B-A3B and Qwen3.5-397B-A17B, and compare against RLVR on the original RLVR data alone across 24 benchmarks spanning STEM and Puzzle, General VQA, Text Recognition and Document Understanding, and Video Understanding. Although this multi-hop data is not synthesized to target any specific benchmark, adding it improves 20 out of 24 benchmarks on both models, indicating broad and generalizable gains. To demonstrate that full chained queries are important, we replace them with half-multi-hop or single-hop variants, reducing the 24-benchmark average accuracy by 5.3 and 7.0 points, respectively. Multi-hop training also strengthens long-CoT vision-language reasoning, with gains peaking at more than 50 accuracy points in the ultra-long-CoT regime. These experiments establish HopChain as an effective, scalable framework for synthesizing multi-hop data that improves generalizable vision-language reasoning.
Current browse context:
cs.CV
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
