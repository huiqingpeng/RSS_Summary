---
title: "VolTune: A Fine-Grained Runtime Voltage Control Architecture for FPGA Systems"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.26147"
published: "2026-03-30"
fetched: "2026-03-31T07:16:31.895943"
---

Computer Science > Hardware Architecture
[Submitted on 27 Mar 2026]
Title:VolTune: A Fine-Grained Runtime Voltage Control Architecture for FPGA Systems
View PDF HTML (experimental)Abstract:The rapid emergence of edge computing platforms and large-scale data centers has made power efficiency a primary design constraint, particularly for data-intensive and AI-driven workloads. Field-programmable gate arrays (FPGAs) are increasingly adopted due to their flexibility and potential for energy-efficient acceleration. However, FPGA supply voltages are typically fixed at design time using conservative margins, limiting the ability to adapt power consumption to runtime conditions.
This paper presents VolTune, an open-source runtime voltage control architecture that enables runtime tuning of FPGA supply voltages through FPGA-integrated control logic that abstracts low-level PMBus operations. VolTune provides both hardware-based and software-based control paths, allowing designers to balance deterministic low-latency operation against programmability.
In the presented prototype, the hardware-based control path achieves a measured end-to-end voltage transition latency of 2.3 ms, while the controller adds under 2% static power overhead and under 2% FPGA resource overhead. As a representative case study, VolTune is evaluated on the GTX transceiver supply rail of a Kintex-7 platform. The results show that runtime voltage tuning exposes a bounded operating region with clear trade-offs between energy efficiency and reliability, and achieves up to approximately 29.3% rail-power reduction at 10.0 Gbps when allowing BER up to 10e-6. These results show that FPGA-integrated runtime voltage control can provide practical energy savings with low integration overhead.
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
