---
title: "A Scalable Open-Source QEC System with Sub-Microsecond Decoding-Feedback Latency"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.16203"
published: "2026-03-18"
fetched: "2026-03-18T14:52:33.512153"
---

Quantum Physics
[Submitted on 17 Mar 2026]
Title:A Scalable Open-Source QEC System with Sub-Microsecond Decoding-Feedback Latency
View PDF HTML (experimental)Abstract:Quantum error correction (QEC) is essential for realizing large-scale, fault-tolerant quantum computation, yet its practical implementation remains a major engineering challenge. In particular, QEC demands precise real-time control of a large number of qubits and low-latency, high-throughput and accurate decoding of error syndromes. While most prior work has focused primarily on decoder design, the overall performance of any QEC system depends critically on all its subsystems including control, communication, and decoding, as well as their integration.
To address this challenge, we present an open-source, fully integrated QEC system built on RISC-Q, a generator for RISC-V-based quantum control architectures. Implemented on RFSoC FPGAs, our system prototype integrates real-time qubit control, a scalable distributed multi-board architecture, and the state-of-the-art hardware QEC decoder within a low-latency, high-throughput decoding pipeline, forming a complete hardware platform ready for deployment with superconducting qubits.
Experimental evaluation on a three-board prototype based on AMD ZCU216 RFSoCs demonstrates an end-to-end QEC decoding-feedback latency of 446 ns for a distance-3 surface code, including syndrome aggregation, network communication, syndrome decoding, and error distribution. Extrapolating from measured subsystem performance and state-of-the-art decoder benchmarks, the architecture can achieve sub-microsecond decoding-feedback latency up to a distance-21 surface code ($\sim$881 physical qubits) when scaled to larger hardware configurations.
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
