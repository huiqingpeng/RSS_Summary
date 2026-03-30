---
title: "Wattchmen: Watching the Wattchers -- High Fidelity, Flexible GPU Energy Modeling"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.26435"
published: "2026-03-30"
fetched: "2026-03-31T07:16:40.372538"
---

Computer Science > Hardware Architecture
[Submitted on 27 Mar 2026]
Title:Wattchmen: Watching the Wattchers -- High Fidelity, Flexible GPU Energy Modeling
View PDF HTML (experimental)Abstract:Modern GPU-rich HPC systems are increasingly becoming energy-constrained. Thus, understanding an application's energy consumption becomes essential. Unfortunately, current GPU energy attribution techniques are either inaccurate, inflexible, or outdated. Therefore, we propose Wattchmen, a flexible methodology for measuring, attributing, and predicting GPU energy consumption. We construct a per-instruction energy model using a diverse set of microbenchmarks to systematically quantify the energy consumption of GPU instructions, enabling finer-grain prediction and energy consumption breakdowns for applications. Compared with the state-of-the-art systems like AccelWattch (32%) and Guser (25%), across 16 popular GPGPU, graph analytics, HPC, and ML workloads, Wattchmen reduces the mean absolute percent error (MAPE) to 14% on V100 GPUs. Furthermore, we show that Wattchmen provides similar MAPEs for water-cooled V100s (15%) and extends to later architectures, including air-cooled A100 (11%) and H100 (12%) GPUs. Finally, to further demonstrate Wattchmen's value, we apply it to applications such as Backprop and QMCPACK, where Wattchmen's insights enable energy reductions of up to 35%.
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
