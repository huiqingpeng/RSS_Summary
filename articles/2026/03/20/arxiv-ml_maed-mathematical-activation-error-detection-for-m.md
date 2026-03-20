---
title: "MAED: Mathematical Activation Error Detection for Mitigating Physical Fault Attacks in DNN Inference"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18120"
published: "2026-03-20"
fetched: "2026-03-20T13:09:31.958997"
---

Computer Science > Cryptography and Security
[Submitted on 18 Mar 2026]
Title:MAED: Mathematical Activation Error Detection for Mitigating Physical Fault Attacks in DNN Inference
View PDF HTML (experimental)Abstract:The inference phase of deep neural networks (DNNs) in embedded systems is increasingly vulnerable to fault attacks and failures, which can result in incorrect predictions. These vulnerabilities can potentially lead to catastrophic consequences, making the development of effective mitigation techniques essential. In this paper, we introduce MAED (Mathematical Activation Error Detection), an algorithm-level error detection framework that exploits mathematical identities to continuously validate the correctness of non-linear activation function computations at runtime. To the best of our knowledge, this work is the first to integrate algorithm-level error detection techniques to defend against both malicious fault injection attacks and naturally occurring faults in critical DNN components in embedded systems. The evaluation is conducted on three widely adopted activation functions, namely ReLu, sigmoid, and tanh which serve as fundamental building blocks for introducing non-linearity in DNNs and can lead to mispredictions when subjected to natural faults or fault attacks. We assessed the proposed error detection scheme via fault model simulation, achieving close to 100% error detection while mitigating existing fault attacks on DNN inference. Additionally, the overhead introduced by integrating the proposed scheme with the baseline implementation (i.e., without error detection) is validated through implementations on an AMD/Xilinx Artix-7 FPGA and an ATmega328P microcontroller, as well as through integration with TensorFlow. On the microcontroller, the proposed error detection incurs less than 1% clock cycle overhead, while on the FPGA it requires nearly zero additional area, at the cost of approximately a 20% increase in latency for sigmoid and tanh.
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
