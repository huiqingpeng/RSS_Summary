---
title: "A Security-Aware Nonlinearity Study of FPGA-Based Time-to-Digital Converters for Quantum Key Distribution Systems"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2604.00229"
published: "2026-04-02"
fetched: "2026-04-03T07:15:03.941035"
---

Quantum Physics
[Submitted on 31 Mar 2026]
Title:A Security-Aware Nonlinearity Study of FPGA-Based Time-to-Digital Converters for Quantum Key Distribution Systems
View PDF HTML (experimental)Abstract:Intrinsic nonlinearity in FPGA-based time-to-digital converters (TDCs) is often treated as a calibration issue and evaluated mainly through post-correction metrics. In quantum key distribution (QKD), however, raw delay-line nonuniformity can affect coincidence timing and thereby influence accidental-coincidence rate and Quantum Bit Error Rate (QBER). This paper analyzes how measured FPGA-TDC nonlinearity propagates to QKD timing metrics using a conservative system-level model that combines random timing uncertainty and deterministic nonlinearity. We also propose fabric-level mitigation strategies based on LUT-assisted delay shaping and placement constraints to reduce severe bin-width irregularities without statistical calibrations. The method is evaluated by reproducing two open-source TDCs implemented on a low-cost Zynq-7000 FPGA. We observe reductions of 14\%-21\% in integral nonlinearity (INL) compared with the non-optimized design, leading to a reduced QBER contribution and an improvement by 3.7\%-14.2\% in the estimated secret fraction. These results suggest that raw FPGA-TDC nonlinearity deserves explicit consideration in timing-sensitive QKD implementations.
Current browse context:
quant-ph
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
