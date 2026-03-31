---
title: "A Switch-Centric In-Network Architecture for Accelerating LLM Inference in Shared-Memory Network"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.28239"
published: "2026-03-31"
fetched: "2026-04-01T07:16:21.194862"
---

Computer Science > Hardware Architecture
[Submitted on 30 Mar 2026]
Title:A Switch-Centric In-Network Architecture for Accelerating LLM Inference in Shared-Memory Network
View PDF HTML (experimental)Abstract:In-network computing techniques, exemplified by NVLink Sharp (NVLS), offer a promising approach to addressing the communication bottlenecks in LLM inference by offloading collective operations, such as All-Reduce, to switches. However, the accelerator-centric architecture of NVLS suffers from two fundamental limitations: 1) it relies on GPU load instructions to trigger reduction operations, which means that the data reduced in the switch must be additionally transferred back to the initiating GPU rather than being broadcast directly, thereby introducing unnecessary communication overhead; 2) due to its architectural constraints, NVLS cannot offload operators that are not decomposable into memory-semantic instructions, such as the in-network quantization (INQ) proposed in this work. As a result, All-Reduce in NVLS must operate at FP16/BF16 precision, leading to substantial bandwidth this http URL address these limitations, we propose SCIN, the first switch-centric in-network architecture for shared-memory networks of AI accelerators, enabling both low-latency and high-bandwidth All-Reduce. Specifically, we introduce an in-switch accelerator (ISA) capable of initiating memory-semantic operations for in-network processing, together with a co-designed communication fabric that incurs negligible protocol overhead. By eliminating redundant data movement, SCIN delivers lower All-Reduce latency than NVLS. Moreover, by integrating a quantization module into the ISA, SCIN enables INQ for All-Reduce, reducing its precision to 8 bits and nearly doubling bandwidth with negligible accuracy loss. We also present a prototype of SCIN on a multi-FPGA system to demonstrate its feasibility and effectiveness. Experimental results show that our design accelerates All-Reduce by up to 8.7x for small messages and 3.8x for large messages, leading up to 1.74x faster TTFT and 1.34x faster TPOT on LLaMA-2 models.
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
