---
title: "APreQEL: Adaptive Mixed Precision Quantization For Edge LLMs"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23575"
published: "2026-03-26"
fetched: "2026-03-27T07:15:17.366793"
---

Computer Science > Machine Learning
[Submitted on 24 Mar 2026]
Title:APreQEL: Adaptive Mixed Precision Quantization For Edge LLMs
View PDF HTML (experimental)Abstract:Today, large language models have demonstrated their strengths in various tasks ranging from reasoning, code generation, and complex problem solving. However, this advancement comes with a high computational cost and memory requirements, making it challenging to deploy these models on edge devices to ensure real-time responses and data privacy. Quantization is one common approach to reducing memory use, but most methods apply it uniformly across all layers. This does not account for the fact that different layers may respond differently to reduced precision. Importantly, memory consumption and computational throughput are not necessarily aligned, further complicating deployment decisions. This paper proposes an adaptive mixed precision quantization mechanism that balances memory, latency, and accuracy in edge deployment under user-defined priorities. This is achieved by analyzing the layer-wise contribution and by inferring how different quantization types behave across the target hardware platform in order to assign the most suitable quantization type to each layer. This integration ensures that layer importance and the overall performance trade-offs are jointly respected in this design. Our work unlocks new configuration designs that uniform quantization cannot achieve, expanding the solution space to efficiently deploy the LLMs on resource-constrained devices.
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
